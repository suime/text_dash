import sys
import os

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QColorDialog, QFormLayout, QGridLayout,
                               QGroupBox, QHeaderView, QLabel, QPushButton,
                               QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget, QMainWindow, QStatusBar, QTabWidget, QHBoxLayout,
                               QTableView, QFileDialog, QMessageBox, QDateEdit)

from PySide6.QtWebEngineWidgets import QWebEngineView

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline


from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# ^ ---
import components.data as data
import components.Menu
import components.read_df
import components.style

# ^ UI components
from ui.Chart import Ui_Chart
from ui.TextMining import Ui_TextMining
from ui.FileInput import Ui_FileInput
from ui.Dictionary import Ui_Dictionary

# Main window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    # @ init UI
    def init_ui(self):
        self.setWindowTitle("Text분석")
        self.setMinimumSize(1000, 600)
        self.setMaximumSize(1920, 1280)
        self.setGeometry(100, 100, 1000, 700)
        self.setMenuBar(components.Menu.MenuBar())
        self.setStatusBar(QStatusBar())

    # ^ 변수 생성
        self.data = data.data(self)

    # ^ 탭 구조 생성
        self.main = QTabWidget()
        self.main.setDocumentMode(True)
        self.setCentralWidget(self.main)

    # ^ 탭 1: 파일 입력
        tab1 = FileInputTab(main=self)
        self.main.addTab(tab1, "파일 입력")

    # ^ 탭 2: 탐색적 분석
        # tab2 = ChartTab()
        # self.main.addTab(tab2, "통계 차트 생성")

    # ^ 탭 3: 텍스트 마이닝
        self.tab3 = TextMiningTab(self.data)
        self.main.addTab(self.tab3, "텍스트 마이닝")

    # ^ 탭 4: 사전
        tab4 = DictionaryTab()
        self.main.addTab(tab4, "사전")

    # ^ 탭 6:
        # tab6 = QTabWidget()
        # self.main.addTab(tab6, "TEST")

        self.show()

    def set_status(self):
        self.statusBar().showMessage(
            f"파일명 : {self.data.fileName}  일자열 : {self.data.cols['date']}  텍스트열 : {self.data.cols['text']}  카테고리 : {self.data.cols['category1']}")
    # 공통 필터


# ui 불러오기

# & tab1 파일 입력 탭


class FileInputTab(QWidget):
    def __init__(self, main: QMainWindow) -> None:
        super().__init__()
        self.ui = Ui_FileInput()
        self.ui.setupUi(self)

        # ^ 파일 입력 버튼
        self.ui.fileBtn.clicked.connect(lambda: self.selectFile(main))

        # ^ 설정하기 버튼
        # * 누르면 데이터프레임 열에 맞게 타입 캐스트 하고, 중복 등 간단한 처리 하기
        self.ui.setCols.clicked.connect(
            lambda: main.data.set_col_manual(self.get_options()))

        self.ui.setCols.clicked.connect(main.set_status)
        self.ui.setCols.clicked.connect(lambda: self.show_df(main.data.fdf))
        self.ui.setCols.clicked.connect(
            lambda: main.tab3.init_filter(main.data))

    def selectFile(self, main):
        file, _ = QFileDialog.getOpenFileName(self, "텍스트 파일 열기",
                                              "data/", "엑셀 파일 (*.xlsx *.xls *.csv);;텍스트 파일 (*.csv *.txt);;데이터프레임(*.parquet);")
        if file:
            df = components.read_df.read_df(file)

            if df is not None:
                main.data.set_df(df, file)
                main.set_status()
                self.set_cols(main)
                self.show_df(main.data.df)
                QMessageBox.information(self, "파일 열기", "파일이 성공적으로 열렸습니다.")
            else:
                QMessageBox.warning(self, "파일 열기", "파일을 읽을 수 없습니다.")

    def get_options(self):
        column = {'date': self.ui.DateCol.currentText(),
                  'text': self.ui.TextCol.currentText(),
                  'category1': self.ui.category1ComboBox.currentText(),
                  'category2': self.ui.category2ComboBox.currentText(),
                  'category3': self.ui.category3ComboBox.currentText()}
        na = self.ui.removeNanCheckBox.isChecked()
        duplicate = self.ui.removeDupCheckBox.isChecked()
        print(column)
        return {"column_config": column, "rm_na": na, "rm_duplicate": duplicate}

    def set_cols(self, main):
        col_list = main.data.get_col()
        for combo_box, col in zip([self.ui.DateCol, self.ui.TextCol, self.ui.category1ComboBox, self.ui.category2ComboBox, self.ui.category3ComboBox], ['date', 'text', 'category1', 'category2', 'category3']):
            combo_box.clear()
            combo_box.addItems(col_list)
            combo_box.setCurrentText(main.data.cols[col])

    def show_df(self, df):
        self.ui.tableView.setModel(data.PandasModel(df))

# & tab2 통계 차트 탭


class ChartTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Chart()
        self.ui.setupUi(self)

# & tab3 텍스트 마이닝 탭


class TextMiningTab(QWidget):
    def __init__(self, data) -> None:
        # * data = main.data
        super().__init__()
        self.ui = Ui_TextMining()
        self.ui.setupUi(self)
        self.figure = Figure(figsize=(6, 5), dpi=300)
        self.canvas = FigureCanvas(self.figure)
        self.ui.WClayout.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)  # 초기 axes 생성
        self.ax.axis('off')
        self.init_filter(data)

        # ^ 데이터프레임 표 생성
        self.ui.initDf.clicked.connect(lambda: self.init_data_tab(data))
        self.ui.saveData.clicked.connect(lambda: to_excel(data.get_sdf()))

        # ^ 통계표 차트 생성
        self.ui.initTable.clicked.connect(lambda: self.init_just_table(data))

        # ^ 통계표 차트 저장
        self.ui.saveStat.clicked.connect(lambda: to_image(self.ui.tablePlot))

        # ^ tf 생성
        self.ui.initTF.clicked.connect(lambda: self.init_TF(data))
        self.ui.saveTf.clicked.connect(lambda: to_excel(data.set_tf()))

        # ^ wc 생성
        self.ui.initWC.clicked.connect(lambda: self.init_WC(data))
        self.ui.saveWC.clicked.connect(lambda: to_image(self.canvas))

        # ^ network 생성
        self.ui.initNetwork.clicked.connect(lambda: self.init_network(data))
        self.ui.saveNetwork.clicked.connect(
            lambda: to_image(self.ui.networkPlot))

    def init_filter(self, data):
        self.filter = filterComponent(self.ui, data)
        self.option = optionComponent(self.ui, data)

    def init_data_tab(self, data):
        view = self.ui.dfplot
        df = self.filter.apply_filter(self.ui, data)
        fig = get_table_plot(df.head(100))
        html = set_plot(fig)
        view.setHtml(html)

    def init_just_table(self, data):
        self.filter.apply_filter(self.ui, data)
        view = self.ui.tablePlot
        df = data.get_sdf()
        cols = list(data.cols.values())
        df_grouped = df.groupby([cols[2], cols[3], cols[4]]).agg(
            건수=(cols[1], 'count')).reset_index()
        self.fig_stat = get_table_plot(df_grouped)
        html_stat = set_plot(self.fig_stat)
        view.setHtml(html_stat)

    def init_TF(self, data):
        self.filter.apply_filter(self.ui, data)
        option = self.option.get_option(self.ui)
        view = self.ui.TFplot

        self.tf = data.set_tf(
            ngram=option['ngram'], topn=option['topn'],
            stopwords=option['stopword'])
        self.fig_tf = get_table_plot(self.tf)
        html_tf = set_plot(self.fig_tf)
        view.setHtml(html_tf)

    def init_WC(self, data):
        self.filter.apply_filter(self.ui, data)
        option = self.option.get_option(self.ui)

        try:
            font = r"C:\Windows\Fonts\malgun.ttf"
            self.ax.clear()
            wc = data.set_wc(
                font_path=font, background_color=option['bgcolor'])
            self.tf = data.set_tf(ngram=option['ngram'], topn=option['topn'],
                                  stopwords=option['stopword'])
            wc.generate_from_frequencies(
                dict(zip(self.tf['단어'], self.tf['빈도'])))
            self.ax.imshow(wc, interpolation='bilinear')
            self.ax.axis('off')

            # 레이아웃 조정 및 캔버스 업데이트
            self.figure.tight_layout()
            self.canvas.draw()

        except Exception as e:
            QMessageBox.warning(self, "워드클라우드 생성 중 오류", f"{e}")

    def init_network(self, data):
        self.filter.apply_filter(self.ui, data)
        option = self.option.get_option(self.ui)
        view = self.ui.networkPlot

        self.network = data.set_network(
            ngram=option['ngram'], topn=option['topn'])
        view.setHtml(self.network)


# & tab4 딕셔너리
class DictionaryTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dictionary()
        self.ui.setupUi(self)


# & filter component
class filterComponent():
    def __init__(self, ui, data) -> None:
        self.init_ui(ui, data)

        # ^ 필터 초기화
        ui.resetFilter.clicked.connect(lambda: self.init_ui(ui, data))

    # ^ 최초 필터의 기본값을 초기화 하는 과정
    # ^ 데이터프레임 변경 또는 필터 초기화 버튼을 눌렀을때 실행

    def init_ui(self, ui, data):
        # * 일자열 설정
        # * 일자열이 없으면 비활성화
        if data.cols['date'] != '':
            ui.startDate.setDisabled(False)
            ui.endDate.setDisabled(False)
            min_date = data.df[data.cols['date']].min()
            max_date = data.df[data.cols['date']].max()
            ui.startDate.setDate(
                QDate(min_date.year, min_date.month, min_date.day))
            ui.endDate.setDate(
                QDate(max_date.year, max_date.month, max_date.day))
        else:
            ui.startDate.setDisabled(True)
            ui.endDate.setDisabled(True)

        # * 문자열 설정
        # * 문자열 없으면 비활성화
        text_enabled = data.cols['text'] != ''
        if text_enabled:
            placeholder_text = "쉼표와 줄바꿈으로 구분하여 입력하세요."
        else:
            placeholder_text = "입력 탭에서 문자열을 설정하세요."
        ui.inText.setDisabled(not text_enabled)
        ui.inText.setPlaceholderText(placeholder_text)
        ui.inText.clear()
        ui.exText.setDisabled(not text_enabled)
        ui.exText.setPlaceholderText(placeholder_text)
        ui.exText.clear()

        # * 카테고리열 설정
        for category, ui_element in [
            ('category1', ui.category1),
            ('category2', ui.category2),
            ('category3', ui.category3)
        ]:
            if data.cols[category] != '':
                ui_element.setDisabled(False)
                ui_element.clear()
                ui_element.addItems(data.get_unique_value(data.cols[category]))
                ui_element.setCurrentIndex(0)
            else:
                ui_element.setDisabled(True)

    # * 현재 필터 옵션 가져오기

    def get_filter(self, ui):
        try:
            startDate = ui.startDate.date().toString("yyyy-MM-dd")
            endDate = ui.endDate.date().toString("yyyy-MM-dd")
        except Exception as e:
            startDate = ''
            endDate = ''
            print(f"{e} 에러 발생해서 변수 설정안됨.")

        try:
            inText = ui.inText.toPlainText()
            exText = ui.exText.toPlainText()
        except Exception as e:
            inText = ""
            exText = ""
            print(f"{e} 에러 발생해서 변수 설정안됨.")

        category1 = ui.category1.currentText()
        category2 = ui.category2.currentText()
        category3 = ui.category3.currentText()

        result = dict(startDate=startDate, endDate=endDate,
                      inText=inText, exText=exText,
                      category1=category1, category2=category2,
                      category3=category3)
        print(result)
        return result

    def apply_filter(self, ui, data):
        df = data.fdf.copy()
        config = self.get_filter(ui)
        cols = data.cols

        if config['startDate'] != '' and config['endDate'] != '':
            df = df[df[cols['date']].dt.date.between(
                pd.to_datetime(config['startDate']).date(),
                pd.to_datetime(config['endDate']).date())]

        if config['inText'] != '':
            df = df[df[cols['text']].str.contains(
                to_regex(config['inText']), case=False, na=False)]
        if config['exText'] != '':
            df = df[~df[cols['text']].str.contains(
                to_regex(config['exText']), case=False, na=False)]

        if config['category1'] != '' and config['category1'] != '전체':
            df = df[df[cols['category1']] == config['category1']]
        if config['category2'] != '' and config['category2'] != '전체':
            df = df[df[cols['category2']] == config['category2']]
        if config['category3'] != '' and config['category3'] != '전체':
            df = df[df[cols['category3']] == config['category3']]

        data.set_sdf(df)
        print('적용완료')
        return df


#
class optionComponent():
    def __init__(self, ui, data) -> None:
        self.init_ui(ui, data)
        self.color = '#000'
        self.bgcolor = '#fff'
        self.font = r'C:\Windows\Fonts\malgun.ttf'

    def init_ui(self, ui, data):
        self.init_text_option(ui, data)
        self.init_design_option(ui)

    def init_text_option(self, ui, data):
        pass

    def init_design_option(self, ui):
        self.fontPicker = FontSelector()
        self.fontPicker.setMinimumWidth(150)
        self.fontPicker.combo_box.setCurrentText('Malgun Gothic')
        self.fontPicker.setSizePolicy(
            QSizePolicy.Expanding,  QSizePolicy.Fixed)
        ui.designBox.layout().addWidget(self.fontPicker, 0, 1)

        ui.colorPicker.clicked.connect(
            lambda: self.set_color(ui.colorPicker, 'color'))
        ui.bgcolorPicker.clicked.connect(
            lambda: self.set_color(ui.bgcolorPicker, 'bgcolor'))
        ui.colorPicker.clicked.connect(
            lambda: self.change_color(ui.colorPicker, self.color))
        ui.bgcolorPicker.clicked.connect(
            lambda: self.change_color(ui.bgcolorPicker, self.bgcolor))

    def set_color(self, widget: QWidget, obj: str):
        color = QColorDialog.getColor()
        setattr(self, obj, color.name())

    def change_color(self, widget, color):
        widget.setStyleSheet(f"background-color: {color};")
        widget.setText(f"{color}")

    def get_option(self, ui):

        topn = ui.topnCount.value()
        ngram = tuple(sorted((ui.ngram_0.value(), ui.ngram_1.value())))
        stopword = to_regex(ui.stopwordsEdit.toPlainText())

        # > 일단 폰트는 아직
        options = dict(topn=topn, ngram=ngram, stopword=stopword, font=self.font,
                       color=self.color, bgcolor=self.bgcolor)
        return options

    def apply_option(self, ui, data):

        pass


def to_regex(text: str):
    import re
    pattern = re.sub(r'\s*[,\n]\s*', '|', text)
    pattern = re.sub(r'\|+', '|', pattern)
    pattern = pattern.strip('|')
    return pattern


def get_table_plot(df: pd.DataFrame):
    """
    Pandas DataFrame을 Plotly의 go.Table로 출력하는 함수

    Parameters:
    df (pd.DataFrame): 출력할 데이터 프레임

    Returns:
    fig (go.Figure): Plotly Figure 객체
    """
    # 데이터 프레임의 컬럼과 값을 리스트로 변환
    header = list(df.columns)

    # Plotly의 go.Table 객체 생성
    table = go.Table(
        header=dict(values=header, fill_color='grey',
                    align='center', line_color='darkslategray',
                    font=dict(color='white', size=13)),
        cells=dict(values=[df[col] for col in df.columns],
                   fill_color='white',
                   line_color='darkslategray',
                   align=['left', 'center'],
                   font=dict(color='black', size=12),
                   format=[None if df[col].dtype == 'object' else ',.0f' for col in df.columns]))

    # Figure 객체 생성
    fig = go.Figure(data=[table])
    return fig


def set_plot(fig: go.Figure,
             config: dict = {'bgcolor': 'white', 'font': '맑은 고딕'}):
    # 기본 플로틀리 차트
    # ^
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',
                      paper_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(margin=dict(r=5, l=5, t=20, b=0))

    html_config = dict(toImageButtonOptions={
        'format': 'png',  # one of png, svg, jpeg, webp
        'filename': r'C:\Users\Administrator\Downloads\차트',
        'height': 500,
        'width': 700,
    }, displaylogo=False)

    html = plotly.offline.plot(fig, include_plotlyjs='cdn',
                               output_type='div', config=html_config)
    html = '<script charset="utf-8" src="C:\\Users\\Administrator\\plotly.min.js"></script>' + html

    # todo: 오프라인에서도 되도록 cdn 변환 코드를 넣어야함
    return html


class FontSelector(QWidget):
    def __init__(self, font_path=r"C:\Windows\Fonts"):
        super().__init__()
        self.font_path = font_path
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.combo_box = QComboBox(self)
        self.load_fonts()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.combo_box)
        self.setLayout(layout)

    def load_fonts(self):
        font_files = [f for f in os.listdir(
            self.font_path) if f.endswith(('.ttf', '.otf'))]

        for font_file in font_files:
            font_path = os.path.join(self.font_path, font_file)
            font_id = QFontDatabase.addApplicationFont(font_path)
            if font_id != -1:
                font_families = QFontDatabase.applicationFontFamilies(font_id)
                for family in font_families:
                    self.combo_box.addItem(family)


def to_image(QWidget: QWidget, dir: str = ''):
    # 차트 위젯의 내용을 QPixmap으로 캡처
    pixmap = QWidget.grab()
    # 이미지 저장
    filename, _ = QFileDialog.getSaveFileName(
        None, "차트 저장", dir, "PNG 파일 (*.png);;JPEG 파일 (*.jpg *.jpeg)")
    if filename:
        pixmap.save(filename)
        print(f"이미지가 {filename}에 저장되었습니다.")


def to_excel(df: pd.DataFrame, dir: str = ''):
    # 파일 저장
    filename, _ = QFileDialog.getSaveFileName(
        None, "차트 저장", dir, "xlsx 파일 (*.xlsx *.xls);;csv 파일 (*.csv)")
    if filename:
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            df.to_excel(filename, index=False)
        elif filename.endswith('.csv'):
            df.to_csv(filename, encoding='UTF-8', index=False)
        print(f"데이터가 {filename}에 저장되었습니다.")


# @ Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("텍스트 분석 대시 보드")
    main_window.setWindowIcon(QIcon('src/public/Icon.png'))
    main_window.show()
    sys.exit(app.exec())
