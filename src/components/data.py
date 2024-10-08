import pandas as pd
import re
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import *
import plotly.graph_objects as go
import plotly.express as px
from wordcloud import WordCloud

from .func import *

EX_COL = "--제외--"


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
        self.df = pd.DataFrame(df).dropna(how='all')
        self.fileName = filename
        self.set_col_auto()

    def set_sdf(self, df):
        self.sdf = df
        for attr in ['vectorizer', 'tf', 'wc', 'network']:
            if hasattr(self, attr):
                delattr(self, attr)

    def get_sdf(self):
        if hasattr(self, 'sdf'):
            return self.sdf
        else:
            return self.fdf

    def get_col(self):
        cols = self.df.columns.to_list()
        cols.sort()
        cols.insert(0, "미설정")
        return cols

    def get_unique_value(self, col, all: bool = True):
        result = list(self.df[col].unique())
        result = [str(x) for x in result]  # Convert all elements to strings
        result.sort()
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
            df = df[col].dropna()
            X = vectorizer.fit_transform(df)
            term_freq_df = pd.DataFrame({
                '단어': vectorizer.get_feature_names_out(),
                '빈도': X.toarray().sum(axis=0)})\
                .sort_values('빈도', ascending=False).head(topn)

        if stopwords.strip() != '':
            return term_freq_df[~term_freq_df['단어'].str.contains(
                stopwords)]

        return term_freq_df

    def set_wc(self,
               font_path='',
               colormap='Set2',
               background_color='#FFF'):
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

        # nt.set_template("dash_chart/.network/template.html")
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
        return str(text).encode('cp949', errors='replace').decode('cp949')

    def _to_regex(self, text: str):
        text = text.strip()
        pattern = re.sub(r'\s*[,\n]\s*', '|', text)
        pattern = re.sub(r'\|+', '|', pattern)
        pattern = pattern.strip('|')
        return pattern

    def apply_filter(self, config: dict):
        """필터를 적용"""
        if hasattr(self, 'fdf'):
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

        for i in range(1, 4):
            category = config[f'category{i}']
            if category not in ['', '전체', EX_COL]:
                df = df[df[cols[f'category{i}']] == category]

        if config.get('nlp', False):
            try:
                df[cols['text']] = self.text_process(df[cols['text']])
            except Exception as e:
                print(f'자연어 처리에서 오류가 발생했습니다.\n {e}')

        self.set_sdf(df)
        return self.sdf

    def text_process(self, text: pd.Series, config: dict, stopwords=''):
        """텍스트 전처리 하는 함수"""
        from mecab import MeCab
        mecab = MeCab()

        def _del_sinmungo(text):
            # ^ 신문고 삭제
            pattern = re.compile(
                r'.*국민신문고 알림.*[민원 유입 경로]|.*제30조\(벌칙\)|안전신문고 신고파일.*|제\d*조|별표\s?\d*|접기펴기 - 현재 축소됨|시행령|비밀보장|아래 동영상 링크.*|사진|동영상|촬영|파일|철저|\[.*?\]|[^\w\s]'
            )
            return pattern.sub('', text)
        text = text.apply(_del_sinmungo)

        def _extract_noun(text, stopwords=stopwords, model=mecab):
            return " ".join(model.nouns(text))

        text = text.apply(_extract_noun, stopwords=stopwords, model=mecab)

        # ^ 영어, 한자 제거
        # ^ 개인정보 제거
        # ^ 국민신문고 제거

        # ^ 숫자 제거
        if config['num']:
            text = text.apply(lambda x: re.sub(r'\d*', '', x))
        # ^ 특수문자 제거
        if config['special']:
            text = text.apply(lambda x: re.sub(r'[\W\S]', '', x))

        return text

    def set_treemap(self, filter: dict, option: dict):
        df = self.apply_filter(filter)
        cols = self.cols

        cat = [filter['category1'], filter['category2'], filter['category3']]

        path = list()
        for i, a in enumerate(cat):
            if a != EX_COL:
                path.append(cols[f'category{str(i + 1)}'])
        if len(path) == 0:
            QMessageBox.warning(None, "설정 오류", "하나 이상의 분석할 데이터를 선택하세요.")
            return None
        df = df.dropna(subset=path)
        fig = px.treemap(df, path=path)

        fig.update_traces(textinfo="label+text+value+percent root",
                          texttemplate="%{label}<br>%{value:,.0f}건<br>%{percentRoot}",
                          marker=dict(
                              line=dict(color='rgba(0,0,0,0)', width=1)),
                          textfont=dict(color='white'))  # 폰트 색상을 흰색으로 설정
        
        html = set_plot(
            fig, "treemap", title=option['title'], sub=option['sub'], font=option['font'],
            min_size=option['min_size'])
        return html

    def set_pie(self, filter: dict, option: dict):
        """분류가 하나일때는 파이차트, 두개 이상이면 선버스트 차트 만들기"""
        df = self.apply_filter(filter)
        cols = self.cols

        cat = [filter['category1'], filter['category2'], filter['category3']]

        path = list()
        for i, a in enumerate(cat):
            if a != EX_COL:
                path.append(cols[f'category{str(i + 1)}'])
        if len(path) == 0:
            QMessageBox.warning(None, "설정 오류", "하나 이상의 분석할 데이터를 선택하세요.")
            return None

        # ^ 선버스트
        df = df.dropna(subset=path)
        fig = px.sunburst(df, path=path)
        fig.update_traces(textinfo="label+text+value+percent root",
                          texttemplate="%{label}<br>%{value:,.0f}건<br>%{percentRoot}",
                          marker=dict(line=dict(color='rgba(255,255,255,1)', width=1)))

        html = set_plot(fig, "pie", title=option['title'], sub=option['sub'],
                        font=option['font'], min_size=option['min_size'])
        return html

    def set_hbar(self, filter: dict, option: dict):
        """분류가 하나일때는 파이차트, 두개 이상이면 선버스트 차트 만들기"""
        df = self.apply_filter(filter)
        cols = self.cols

        cat = [filter['category1'], filter['category2'], filter['category3']]

        path = list()
        for i, a in enumerate(cat):
            if a != EX_COL:
                path.append(cols[f'category{str(i + 1)}'])
        if len(path) == 0:
            QMessageBox.warning(None, "설정 오류", "하나 이상의 분석할 데이터를 선택하세요.")
            return None

        # ^ 선버스트
        df = df.dropna(subset=path)
        fig = px.icicle(df, path=[px.Constant("전체")]+path)
        fig.update_traces(textinfo="label+text+value+percent root",
                          texttemplate="%{label}<br>%{value:,.0f}건<br>%{percentRoot}",
                          marker=dict(line=dict(color='rgba(255,255,255,1)', width=1)))

        html = set_plot(fig, "pie", title=option['title'], sub=option['sub'],
                        font=option['font'], min_size=option['min_size'])
        return html

    def set_sankey(self, filter: dict, option: dict):
        df = self.apply_filter(filter)
        cols = self.cols
        path = list()

        cat = [filter['category1'], filter['category2'], filter['category3']]

        for i, a in enumerate(cat):
            if a != EX_COL:
                path.append(cols[f'category{str(i + 1)}'])
        if len(path) == 0:
            QMessageBox.warning(None, "설정 오류", "하나 이상의 분석할 데이터를 선택하세요.")
            return None

        fig = px.parallel_categories(df, dimensions=path)
        html = set_plot(fig, "sankey", title=option['title'], sub=option['sub'],
                        font=option['font'], min_size=12)
        return html

    def _set_ts(self, filter: dict):
        df = self.apply_filter(filter)
        date = self.cols['date']

        if date == '':
            QMessageBox.warning(
                None, '오류 발생', '일자열이 선택되지 않았습니다. 시계열 분석은 일자열이 설정되어야 합니다.')
            return None

        if filter['group'] == 'd':
            grouped_df = df.groupby(
                df[date].dt.date).size().reset_index(name='건수')
        elif filter['group'] == 'w':
            grouped_df = df.groupby(pd.Grouper(
                key=date, freq='W')).size().reset_index(name='건수')
        elif filter['group'] == 'm':
            grouped_df = df.groupby(pd.Grouper(
                key=date, freq='M')).size().reset_index(name='건수')
        elif filter['group'] == 'y':
            grouped_df = df.groupby(pd.Grouper(
                key=date, freq='Y')).size().reset_index(name='건수')
        else:
            grouped_df = df

        return grouped_df

    def set_line(self, filter: dict, option: dict):
        df = self._set_ts(filter)
        cols = self.cols
        fig = px.line(df, x=cols['date'], y='건수')
        html = set_plot(fig, "line", title=option['title'], sub=option['sub'],
                        font=option['font'], min_size=12)
        return html

    def set_bar(self, filter: dict, option: dict):
        df = self._set_ts(filter)
        cols = self.cols
        fig = px.bar(df, x=cols['date'], y='건수')
        html = set_plot(fig, "line", title=option['title'], sub=option['sub'],
                        font=option['font'], min_size=12)
        return html

    def set_stat(self, filter, option):
        df = self.apply_filter(filter)

        html = set_plot(fig, 'stats',)
        return html
