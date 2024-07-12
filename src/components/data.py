import pandas as pd
import re
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import *
import plotly.graph_objects as go
import plotly.express as px
from wordcloud import WordCloud


class data():
    def __init__(self) -> None:
        self.init_df()

    def init_df(self):
        self.df = pd.DataFrame()
        self.fdf = pd.DataFrame()
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
        try:
            for col in self.df.columns:
                if re.search(r'(일자)', col):
                    self.df[col] = pd.to_datetime(self.df[col])
                    self.cols['date'] = col
                    print(f"{col} : 일자열 설정 완료!")
                    break
        except ValueError:
            print("데이터에 일자 형식의 열을 확인할 수 없습니다. 수동으로 지정해주세요.")

    def set_category_col(self):
        for col in self.df.columns:
            if re.search(r'대', col):
                self.cols['category1'] = col
                print(f"{col} : category1 열 설정 완료!")
            elif re.search(r'중', col):
                self.cols['category2'] = col
                print(f"{col} : category2 열 설정 완료!")
            elif re.search(r'소', col):
                self.cols['category3'] = col

    def set_text_col(self):
        for col in self.df.columns:
            if re.search(r'(내용|메모|단어)', col):
                self.cols['text'] = col
                print(f"{col} : 문자열 설정 완료!")
                break
            else:
                self.cols['text'] = ''
                print("데이터에 일자 형식의 열을 확인할 수 없습니다. 수동으로 지정해주세요.")

    # todo : 나중에 세팅 값에서 받아올수 있도록 하기
    def set_col_manual(self, config: dict):
        configs = config['column_config']
        rm_na = config['rm_na']
        rm_duplicate = config['rm_duplicate']

        for key in configs:
            if configs[key].strip() != '' and configs[key] != '미설정':
                self.cols[key] = configs[key]
            else:
                self.cols[key] = ''

        columns = [col for col in self.cols.values() if col != '']
        print(f"칼럼값 : {self.cols.values()}")
        df = self.df[columns].copy()
        if rm_na:
            df = df.dropna(how='all')
        if rm_duplicate:
            df = df.drop_duplicates()
        setattr(self, 'fdf', df)
        print('df 설정함')

    def set_vectorizer(self, ngram: tuple[float, float] = (2, 2), topn: int = 40):
        from sklearn.feature_extraction.text import CountVectorizer
        if hasattr(self, 'vectorizer'):
            return self.vectorizer
        else:
            print("vectorizer 생성중 ...")
            df = self.get_sdf().copy()
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
            print("tf 생성중 ...")
            vectorizer = self.set_vectorizer(
                topn=topn, ngram=ngram)
            df = self.get_sdf().copy()
            col = self.cols['text']
            df = df[col]
            X = vectorizer.fit_transform(df)
            term_freq_df = pd.DataFrame({
                '단어': vectorizer.get_feature_names_out(),
                '빈도': X.toarray().sum(axis=0)})\
                .sort_values('빈도', ascending=False).head(topn)

        if stopwords.strip() != '':
            term_freq_df['단어'] = term_freq_df['단어'].str.replace(
                self._to_regex(stopwords), '', regex=True)
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
                                font_step=1,
                                colormap=colormap,
                                max_words=100,
                                max_font_size=100)
            return self.wc

    def set_network(self, ngram: tuple[float, float] = (2, 2), topn: int = 40):
        import os
        import numpy as np
        from pyvis.network import Network
        import networkx as nx
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()

        print("1---")
        vectorizer = self.set_vectorizer(topn=topn, ngram=ngram)
        df = self.get_sdf().copy()
        col = self.cols['text']
        data = df[col].apply(self._clean_text_for_cp949)
        X = vectorizer.fit_transform(data)

        print("2---")
        adjacency_matrix = (X.T * X).toarray()
        np.fill_diagonal(adjacency_matrix, 0)

        G = nx.from_numpy_array(adjacency_matrix)
        nt = Network(width="100%", height="500px",
                     notebook=False, cdn_resources='in_line')
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
            # i['face'] = 'Gong gothic'

        nt.nodes = N.to_dict(orient='records')
        # 엣지수정
        print("5---")
        E = pd.DataFrame(nt.edges)
        E['width'] = scaler.fit_transform(E[['width']])*20
        nt.edges = E.to_dict(orient='records')
        if not os.path.exists(r"dash_chart"):
            os.makedirs(r"dash_chart")
        network = nt.generate_html(name=r'dash_chart\network.html')
        network = re.sub('style="width: 100%"',
                         'style="width: 100%; height: 100%;"', network)
        network = re.sub('height: 500px;',
                         'height: 100%;', network)
        self.network = network
        with open(r'dash_chart\network.html', 'w', encoding='utf-8') as file:
            file.write(network)
        html_path = os.path.realpath(r'dash_chart\network.html')
        html_path = QUrl.fromLocalFile(html_path)
        return html_path

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

    def _clean_text_for_cp949(self, text):
        return text.encode('cp949', errors='replace').decode('cp949')

    def _to_regex(self, text: str):
        import re
        pattern = re.sub(r'\s*[,\n]\s*', '|', text)
        pattern = re.sub(r'\|+', '|', pattern)
        pattern = pattern.strip('|')
        return pattern

    def apply_filter(self, config: dict):
        if hasattr(self, 'fdf') :
            df = self.fdf
        else: 
            df = self.df

        cols = self.cols
        if config['startDate'] != '' and config['endDate'] != '':
            df = df[df[cols['date']].dt.date.between(
                pd.to_datetime(config['startDate']).date(),
                pd.to_datetime(config['endDate']).date())]

        if config['inText'] != '':
            df = df[df[cols['text']].str.contains(
                self._to_regex(config['inText']), case=False, na=False)]
        if config['exText'] != '':
            df = df[~df[cols['text']].str.contains(
                self._to_regex(config['exText']), case=False, na=False)]

        if config['category1'] != '' and config['category1'] != '전체':
            df = df[df[cols['category1']] == config['category1']]
        if config['category2'] != '' and config['category2'] != '전체':
            df = df[df[cols['category2']] == config['category2']]
        if config['category3'] != '' and config['category3'] != '전체':
            df = df[df[cols['category3']] == config['category3']]

        self.set_sdf(df)

        return self.sdf
