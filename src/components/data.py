from numpy import vectorize
import pandas as pd
import re
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QRadioButton
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from wordcloud import WordCloud


class data():
    def __init__(self, main) -> None:
        self.init_df()

    def init_df(self):
        self.df = pd.DataFrame()
        self.fileName = ''
        self.cols = dict(date='', text='', category1='',
                         category2='', category3='')

    def set_df(self, df, filename: str = ''):
        self.init_df()
        self.df = pd.DataFrame(df)
        self.fileName = filename
        self.set_col_auto()

    def set_sdf(self, df):
        self.sdf = df
        try:
            del self.vectorizer
            del self.tf
            del self.wc
            del self.network
        except Exception:
            pass

    def get_sdf(self):
        if hasattr(self, 'sdf'):
            return self.sdf
        else:
            return self.fdf

    def get_col(self):
        cols = self.df.columns.to_list()
        cols.insert(0, "미설정")
        return cols

    def get_unique_value(self, col, all: bool = True):
        result = list(self.df[col].unique())
        if all:
            result.insert(0, "전체")
        return result

    def set_col_auto(self):
        self.set_date_col()
        self.set_category_col()
        self.set_text_col()

    def set_date_col(self):
        for col in self.df.columns:
            try:
                self.df[col] = pd.to_datetime(self.df[col])
                self.cols['date'] = col
                print(f"{col} : 일자열 설정 완료!")
                break
            except ValueError:
                print(f"{col}은 날짜 타입이 아닙니다.")

    def set_category_col(self):
        for col in self.df.columns:
            if re.search(r'대', col):
                self.cols['category1'] = col
            elif re.search(r'중', col):
                self.cols['category2'] = col
            elif re.search(r'소', col):
                self.cols['category3'] = col

    def set_text_col(self):
        for col in self.df.columns:
            if re.search(r'(내용|메모)', col):
                self.cols['text'] = col
                break
            else:
                self.cols['text'] = ''
        print(self.cols['text'])

    # todo : 나중에 세팅 값에서 받아올수 있도록 하기
    def set_col_manual(self, config: dict):
        column_config = config['column_config']
        rm_na = config['rm_na']
        rm_duplicate = config['rm_duplicate']

        for key in column_config:
            if column_config[key].strip() != '' and column_config[key] != '미설정':
                self.cols[key] = column_config[key]
            else:
                self.cols[key] = ''

        columns = [col for col in self.cols.values() if col != '']
        print(f"칼럼값 : {self.cols.values()}")
        df = self.df[columns].copy()
        if rm_na:
            df = df.dropna(how='all')
        if rm_duplicate:
            df = df.drop_duplicates()
        self.fdf = df

        print('수동으로 설정함')

    def set_vectorizer(self, ngram: tuple[float, float] = (2, 2), topn: int = 40):
        from sklearn.feature_extraction.text import CountVectorizer
        if hasattr(self, 'vectorizer'):
            return self.vectorizer
        else:
            print("vectorizer가 없어서 생성합니다.")
            df = self.get_sdf()
            col = self.cols['text']
            df = df[col]

            vectorizer = CountVectorizer(ngram_range=ngram, max_features=topn)
            self.vectorizer = vectorizer
            return self.vectorizer

    def set_tf(self,
               ngram: tuple[float, float] = (2, 2),
               topn: int = 40, stopwords: str = ''):
        if hasattr(self, 'tf'):
            return self.tf
        else:
            print("tf가 없어서 생성합니다.")
            vectorizer = self.set_vectorizer(
                topn=topn, ngram=ngram)
            df = self.get_sdf()
            col = self.cols['text']
            df = df[col]
            X = vectorizer.fit_transform(df)
            term_freq_df = pd.DataFrame({
                '단어': vectorizer.get_feature_names_out(),
                '빈도': X.toarray().sum(axis=0)})\
                .sort_values('빈도', ascending=False).head(topn)

        if stopwords.strip() != '':
            term_freq_df['단어'] = term_freq_df['단어'].str.replace(
                to_regex(stopwords), '', regex=True)
        self.tf = term_freq_df

        return self.tf

    def set_wc(self,
               font_path='',
               colormap='Set2',
               background_color='#FFF'):
        if hasattr(self, 'wc'):
            return self.wc
        else:
            self.wc = WordCloud(font_path=font_path,
                                width=800,
                                height=600,
                                prefer_horizontal=1,
                                background_color=background_color,
                                mode="RGBA",
                                font_step=0.1,
                                colormap=colormap,
                                max_words=100,
                                max_font_size=100)
            return self.wc

    def set_network(self, ngram: tuple[float, float] = (2, 2), topn: int = 40):
        if hasattr(self, 'network'):
            return self.network
        else:
            print("network가 없어서 생성합니다.")

        import numpy as np
        from pyvis.network import Network
        import networkx as nx
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()

        print("1---")
        vectorizer = self.set_vectorizer(topn=topn, ngram=ngram)
        df = self.get_sdf().copy()
        col = self.cols['text']
        data = df[col].apply(clean_text_for_cp949)
        X = vectorizer.fit_transform(data)

        print("2---")
        adjacency_matrix = (X.T * X).toarray()
        np.fill_diagonal(adjacency_matrix, 0)

        G = nx.from_numpy_array(adjacency_matrix)
        nt = Network(width="100%", height="500px",
                     notebook=False, cdn_resources='remote')
        print("3---")
        nt.from_nx(G)
        print("4---")
        # 노드 및 엣지 수정
        for n in nt.nodes:
            n["font"] = {"size": 10}
        N = pd.DataFrame(nt.nodes).sort_values('id')
        nt.options = nt.options.set(self.set_network_option())

        # 노드 수정하기
        N['label'] = vectorizer.get_feature_names_out()
        N['size'] = np.sum(adjacency_matrix, axis=1)
        N['size'] = scaler.fit_transform(N[['size']])*15 + 1
        N['labelHighlightBold'] = True

        N.sort_index(inplace=True)
        for n, i in enumerate(N['font']):
            i['size'] = round(N['size'][n], 1) + 10
            i['face'] = 'Gong gothic'

        nt.nodes = N.to_dict(orient='records')
        # 엣지수정
        print("5---")
        E = pd.DataFrame(nt.edges)
        E['width'] = scaler.fit_transform(E[['width']])*20
        nt.edges = E.to_dict(orient='records')
        nt.generate_html()
        nt.html.replace("width: 800px;", "width: 100%;")
        nt.html.replace('style="width: 100%"',
                        'style="width: 100%; height: 100%;"')
        #> text 용 
        nt.html = '<script charset="utf-8" src="C:\\Users\\Administrator\\bootstrap.bundle.min.js"></script>' + nt.html
        nt.html = '<script charset="utf-8" src="C:\\Users\\Administrator\\vis-network.min.js"></script>' + nt.html
        nt.html = '<link rel="stylesheet" href="C:\\Users\\Administrator\\vis-network.min.css">' + nt.html
        nt.html = '<link rel="stylesheet" href="C:\\Users\\Administrator\\bootstrap.min.css">' + nt.html
        self.network = nt.html
        return self.network

    def set_network_option(self, solver: str = 'hierarchicalRepulsion'):
        option = f""" 
            const options = {{
            "nodes": {{
                "borderWidth": 3,
                "borderWidthSelected": 1,
                "opacity": 1,
                "shape": "dot",
                "font": {{
                    "strokeWidth": 4
                }}
            }},
            "edges": {{
                "color": {{
                    "opacity": 0.3
                }},
                "selfReference": {{
                    "angle": 0.785
                }},
                "smooth": {{
                "type": "cubicBezier",
                "forceDirection": "none",
                "roundness": 0.6
                }}
            }},
            "physics": {{
                "maxVelocity": 30,
                "minVelocity": 0.75,
                "solver": "{solver}",
                
                "{solver}": {{
                "centralGravity": 0,
                "nodeDistance": 100,
                "avoidOverlap": 1,
                "springLength": 100
                }}
                }}
            }}"""
        return option


class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """

    def __init__(self, dataframe: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe

    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return str(self._dataframe.iloc[index.row(), index.column()])

        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._dataframe.columns[section])

            if orientation == Qt.Vertical:
                return str(self._dataframe.index[section])

        return None


def to_regex(text: str):
    pattern = re.sub(r'\s*[,\n]\s*', '|', text)
    pattern = re.sub(r'\|+', '|', pattern)
    pattern = pattern.strip('|')
    return pattern


def clean_text_for_cp949(text):
    return text.encode('cp949', errors='replace').decode('cp949')
