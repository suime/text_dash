import sys
import os
from time import sleep

from PySide6.QtCore import QDate
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QColorDialog, QWidget, QMainWindow, QStatusBar, QTabWidget,
                               QFileDialog, QMessageBox)

import pandas as pd
import plotly.graph_objects as go
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# ^ ---
# ^ components func <- 함수같은거 있는거
# ^ components elements <- 메뉴바, qwidget 같은거, (필터, 옵션 )

# from components import elements, read_df, MenuBar, data
from components import *

# ^ UI components
from ui.FileInput import Ui_FileInput
from ui.Plot import Ui_Plot
from ui.TextMining import Ui_TextMining
from ui.Dictionary import Ui_Dictionary

# Main window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        app_start()
        print('앱시작 중입니다...')

    # @ init UI
    def init_ui(self):
        self.setWindowTitle("Text분석")
        self.setMinimumSize(1000, 600)
        self.setMaximumSize(1920, 1280)
        self.setGeometry(100, 100, 1000, 700)
        # self.setMenuBar(MenuBar())
        self.setStatusBar(QStatusBar())

    # ^ 변수 생성
        self.data = data()

    # ^ 탭 구조 생성
        self.main = QTabWidget()
        self.main.setDocumentMode(True)
        self.setCentralWidget(self.main)

    # ^ 탭 2: 플롯
        self.tab2 = ChartTab(self.data)
    # ^ 탭 3: 텍스트 마이닝
        self.tab3 = TextMiningTab(self.data)
    # ^ 탭 1: 파일 입력
        self.tab1 = FileInputTab(main=self)

        self.main.addTab(self.tab1, "파일 입력")
        self.main.addTab(self.tab3, "텍스트 마이닝")
        self.main.addTab(self.tab2, "통계 분석")


    # ^ 탭 4: 사전
        tab4 = DictionaryTab()
        self.main.addTab(tab4, "텍스트 옵션")

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
            lambda: main.tab3.filter.init_ui(main.tab3.ui, main.data))
        
        self.ui.setCols.clicked.connect(lambda: main.tab2.reset_filter(main.data))
        self.ui.setCols.clicked.connect(main.tab2.reset_option)

    def selectFile(self, main):
        file, _ = QFileDialog.getOpenFileName(self, "텍스트 파일 열기",
                                              "data/", "엑셀 파일 (*.xlsx *.xls *.csv);;텍스트 파일 (*.csv *.txt);;데이터프레임(*.parquet);")
        if file:
            df = read_df(file)

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
        dp = self.ui.removeDupCheckBox.isChecked()
        return {"column_config": column, "rm_na": na, "rm_duplicate": dp}

    def set_cols(self, main):
        col_list = main.data.get_col()
        for combo_box, col in zip([self.ui.DateCol, self.ui.TextCol,
                                   self.ui.category1ComboBox,
                                   self.ui.category2ComboBox,
                                   self.ui.category3ComboBox],
                                  ['date', 'text', 'category1', 'category2', 'category3']):
            combo_box.clear()
            combo_box.addItems(col_list)
            combo_box.setCurrentText(main.data.cols[col])

    def show_df(self, df):
        self.ui.tableView.setModel(elements.PandasModel(df))

# & tab2 통계 차트 탭


class ChartTab(QWidget):
    def __init__(self, data) -> None:
        super().__init__()
        self.ui = Ui_Plot()
        self.ui.setupUi(self)
        self.set_btn(data)

        self._fonts = 'Malgun Gothic'
        self._theme = 'base'
        self._color = '#000000'
        self._bgcolor = '#fff'

    def set_btn(self, data):

        self.ui.resetFilter.clicked.connect(lambda: self.reset_filter(data))
        self.ui.resetOption.clicked.connect(self.reset_option)

        self.ui.initTreemap.clicked.connect(lambda: self.set_treemap(data))
        self.ui.initPie.clicked.connect(lambda: self.set_pie(data))
        self.ui.initHbar.clicked.connect(lambda: self.set_Hbar(data))
        # self.ui.initLine.clicked.connect(lambda: self.set_Line(data))
        # self.ui.initBar.clicked.connect(lambda: self.set_Bar(data))
        # self.ui.initSankey.clicked.connect(lambda: self.set_Sankey(data))
        # self.ui.initStat.clicked.connect(lambda: self.set_Stat(data))

    def reset_filter(self, data):
        if data.cols['date'] != '':
            self.ui.startDate.setDisabled(False)
            self.ui.endDate.setDisabled(False)
            min_date = data.df[data.cols['date']].min()
            max_date = data.df[data.cols['date']].max()
            self.ui.startDate.setDate(
                QDate(min_date.year, min_date.month, min_date.day))
            self.ui.endDate.setDate(
                QDate(max_date.year, max_date.month, max_date.day))
        else:
            self.ui.startDate.setDisabled(True)
            self.ui.endDate.setDisabled(True)

        text_enabled = data.cols['text'] != ''
        if text_enabled:
            placeholder_text = "쉼표와 줄바꿈으로 구분하여 입력하세요."
        else:
            placeholder_text = "입력 탭에서 문자열을 설정하세요."
        self.ui.inText.setDisabled(not text_enabled)
        self.ui.inText.setPlaceholderText(placeholder_text)
        self.ui.inText.clear()
        self.ui.exText.setDisabled(not text_enabled)
        self.ui.exText.setPlaceholderText(placeholder_text)
        self.ui.exText.clear()

        # * 카테고리열 설정
        for category, ui_element in [
            ('category1', self.ui.category1),
            ('category2', self.ui.category2),
            ('category3', self.ui.category3)
        ]:
            if data.cols[category] != '':
                ui_element.setDisabled(False)
                ui_element.clear()
                unique_values = data.get_unique_value(data.cols[category])
                unique_values.insert(1, '--제외--')
                ui_element.addItems(unique_values)
                ui_element.setCurrentIndex(0)
            else:
                ui_element.setDisabled(True)

    def reset_option(self):
        self.ui.text_title.clear()
        self.ui.text_sub.clear()
        self.ui.text_unit.clear()

        self._fonts = 'Malgun Gothic'
        self._theme = 'base'
        self._color = '#000000'
        self._bgcolor = '#fff'

    def get_filter(self):
        if self.ui.startDate.isEnabled() and self.ui.endDate.isEnabled():
            startDate = self.ui.startDate.date().toString("yyyy-MM-dd")
            endDate = self.ui.endDate.date().toString("yyyy-MM-dd")
        else:
            startDate, endDate = '', ''

        try:
            inText = self.ui.inText.toPlainText()
            exText = self.ui.exText.toPlainText()
        except Exception:
            inText, exText = "", ""

        category1 = self.ui.category1.currentText()
        category2 = self.ui.category2.currentText()
        category3 = self.ui.category3.currentText()

        result = dict(startDate=startDate, endDate=endDate,
                      inText=inText, exText=exText,
                      category1=category1,
                      category2=category2,
                      category3=category3)
        print(result)
        return result

    def get_option(self):
        title = self.ui.text_title.text()
        sub = self.ui.text_sub.text()
        unit = self.ui.text_unit.text()
        font = self.ui.fontComboBox.currentFont().family()
        theme = self._theme
        min_size = self.ui.minFontSize.value()

        # > 수정
        color = self._color
        bgcolor = self._bgcolor

        result = dict(title=title, sub=sub, unit=unit, font=font,
                      theme=theme, color=color, bgcolor=bgcolor,
                      min_size=min_size)
        print(result)
        return result

    def set_treemap(self, data):
        html = data.set_treemap(filter=self.get_filter(),
                                option=self.get_option())
        self.ui.qtTreemap.setUrl(html)

    def set_pie(self, data):
        html = data.set_pie(filter=self.get_filter(),
                            option=self.get_option())
        self.ui.qtPie.setUrl(html)

    def set_Hbar(self, data):
        html = data.set_Hbar(filter=self.get_filter(),
                            option=self.get_option())
        self.ui.qtHbar.setUrl(html)


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

        # ^ 데이터프레임 표 생성
        self.ui.initDf.clicked.connect(lambda: self.init_data_tab(data))
        self.ui.saveData.clicked.connect(lambda: to_excel(data.get_sdf()))

        # ^ 통계표 차트 생성
        self.ui.initTable.clicked.connect(lambda: self.init_just_table(data))
        self.ui.saveStat.clicked.connect(lambda: to_excel(self.df_grouped))

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

        self.filter = filterComponent(self.ui, data)
        self.option = optionComponent(self.ui, data)

    def init_data_tab(self, data):
        view = self.ui.dfplot
        df = self.filter.apply_filter(self.ui, data)
        fig = get_table_plot(df.head(100), data.cols['text'])
        html = set_plot(fig, 'data')
        view.setUrl(html)

    def init_just_table(self, data):
        view = self.ui.tablePlot
        df = self.filter.apply_filter(self.ui, data)
        cols = list(data.cols.values())
        self.df_grouped = df.groupby([cols[2], cols[3], cols[4]]).agg(
            건수=(cols[1], 'count')).reset_index()
        self.fig_stat = get_table_plot(self.df_grouped, data.cols['text'])
        html_stat = set_plot(self.fig_stat, 'stat')
        view.setUrl(html_stat)

    def init_TF(self, data):
        self.filter.apply_filter(self.ui, data)
        view = self.ui.TFplot
        option = self.option.get_option(self.ui)
        self.tf = data.set_tf(
            ngram=option['ngram'], topn=option['topn'],
            stopwords=option['stopword'])
        self.fig_tf = get_table_plot(self.tf, data.cols['text'])
        html_tf = set_plot(self.fig_tf, 'tf')
        view.setUrl(html_tf)

    def init_WC(self, data):
        self.filter.apply_filter(self.ui, data)
        option = self.option.get_option(self.ui)
        self.ax.clear()
        wc = data.set_wc(
            font_path=option['font'], background_color=option['bgcolor'])
        self.tf = data.set_tf(ngram=option['ngram'], topn=option['topn'],
                              stopwords=option['stopword'])
        wc.generate_from_frequencies(
            dict(zip(self.tf['단어'], self.tf['빈도'])))
        self.ax.imshow(wc, interpolation='bilinear')
        self.ax.axis('off')

        # 레이아웃 조정 및 캔버스 업데이트
        self.figure.tight_layout()
        self.canvas.draw()

    def init_network(self, data):
        self.filter.apply_filter(self.ui, data)
        option = self.option.get_option(self.ui)
        view = self.ui.networkPlot
        self.network = data.set_network(
            ngram=option['ngram'], topn=option['topn'])
        view.setUrl(self.network)


# & tab4 딕셔너리asda
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
                unique_values = data.get_unique_value(data.cols[category])
                ui_element.addItems(unique_values)
                ui_element.setCurrentIndex(0)
            else:
                ui_element.setDisabled(True)

    # * 현재 필터 옵션 가져오기

    def get_filter(self, ui):
        if ui.startDate.isEnabled() and ui.endDate.isEnabled():
            try:
                startDate = ui.startDate.date().toString("yyyy-MM-dd")
                endDate = ui.endDate.date().toString("yyyy-MM-dd")
            except Exception as e:
                startDate = ''
                endDate = ''
                print(f"{e} 에러 발생해서 변수 설정안됨.")
        else:
            startDate = ''
            endDate = ''

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

        nlp = ui.NLPcheck.isChecked()

        topn = ui.topnCount.value()
        ngram = tuple(sorted((ui.ngram_0.value(), ui.ngram_1.value())))
        stopword = to_regex(ui.stopwordsEdit.toPlainText())

        result = dict(startDate=startDate, endDate=endDate,
                      inText=inText, exText=exText,
                      category1=category1, category2=category2,
                      category3=category3,
                      nlp=nlp, topn=topn, ngram=ngram, stopword=stopword)
        print(result)
        return result

    def apply_filter(self, ui, data):
        return data.apply_filter(self.get_filter(ui))


#
class optionComponent(QWidget):
    def __init__(self, ui, data) -> None:
        super().__init__()
        self.color = '#000'
        self.bgcolor = '#fff'
        self.font = r'C:\Windows\Fonts\malgun.ttf'
        self.init_design_option(ui)

    def init_design_option(self, ui):
        if not hasattr(self, 'colorPicker_connected'):
            ui.ChangeFont.clicked.connect(self.select_font)
            ui.colorPicker.clicked.connect(
                lambda: self.set_color(ui.colorPicker, 'color'))
            ui.bgcolorPicker.clicked.connect(
                lambda: self.set_color(ui.bgcolorPicker, 'bgcolor'))
            self.colorPicker_connected = True

    def select_font(self):
        file, _ = QFileDialog.getOpenFileName(self, "폰트 파일 열기",
                                              "", "폰트 파일 (*.ttf *.otf)")
        if file:
            if file is not None:
                self.font = file
            else:
                QMessageBox.warning(self, "파일 열기", "파일을 읽을 수 없습니다.")
        else:
            self.font = r'C:\Windows\Fonts\malgun.ttf'
            print(f"폰트 : {self.font}")

    def set_color(self, widget: QWidget, obj: str):
        color = QColorDialog.getColor()
        widget.setText(f"{color.name()}")
        widget.setStyleSheet(f"background-color: {color.name()};")
        setattr(self, obj, color.name())

    def get_option(self, ui):

        topn = ui.topnCount.value()
        ngram = tuple(sorted((ui.ngram_0.value(), ui.ngram_1.value())))
        stopword = to_regex(ui.stopwordsEdit.toPlainText())

        options = dict(topn=topn, ngram=ngram, stopword=stopword, font=self.font,
                       color=self.color, bgcolor=self.bgcolor)
        return options


# @ Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("텍스트 분석 대시 보드")
    main_window.setWindowIcon(QIcon('./src/public/icon.ico'))
    main_window.show()
    sys.exit(app.exec())
