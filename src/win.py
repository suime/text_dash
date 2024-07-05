import sys
from typing import Optional

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
                               QGroupBox, QHeaderView, QLabel, QPushButton,
                               QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget, QMainWindow, QStatusBar, QTabWidget, QHBoxLayout,
                               QTableView, QFileDialog, QMessageBox, QDateEdit) 

from PySide6.QtWebEngineWidgets import QWebEngineView

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as plt
from polars import head

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
        tab2 = ChartTab()
        self.main.addTab(tab2, "통계 차트 생성")

    # ^ 탭 3: 텍스트 마이닝
        tab3 = TextMiningTab(self.data)
        self.main.addTab(tab3, "텍스트 마이닝")

    # ^ 탭 4: 사전
        tab4 = DictionaryTab()
        self.main.addTab(tab4, "사전")

    # ^ 탭 6:
        tab6 = QTabWidget()
        self.main.addTab(tab6, "TEST")

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
        self.init_filter(data)
        self.ui.initTable.clicked.connect(lambda: self.init_just_table(data))

    def init_filter(self, data):
        data_filter = filterComponent(self.ui, data)

    def init_just_table(self, data):
        view = self.ui.tablePlot
        df = data.df
        cols = list(data.cols.values())
        
        fig = go.Figure(data=[go.Table(
            header=dict(values=df.columns[[0, 1, 2]],
                        align='center'),
            cells=dict(values=[df[cols[0]], df[cols[1]], df[cols[2]],])
        )])
        html = plt.plot(fig, include_plotlyjs='cdn', output_type='div')
        view.setHtml(html)



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

        # ^ 필터 적용하기
        ui.applyFilter.clicked.connect(lambda: self.get_filter(ui))

    # ^ 최초 필터의 기본값을 초기화 하는 과정
    # ^ 데이터프레임 변경 또는 필터 초기화 버튼을 눌렀을때 실행
    def init_ui(self, ui, data):
        # * 일자열 설정
        # * 일자열이 없으면 비활성화
        print(f"필터 초기화 되었습니다. {data.cols['date']}")
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
        placeholder_text = "ex) 한국, 도로, 공사" if text_enabled else "입력 탭에서 문자열을 설정하세요."
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
        startDate = ui.startDate.dateTime().toString()
        endDate = ui.endDate.dateTime().toString(Qt.ISODate)
        print(startDate)
        return [startDate, endDate]


# @ Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("텍스트 분석 대시 보드")
    main_window.setWindowIcon(QIcon('src/public/Icon.png'))
    main_window.show()
    sys.exit(app.exec())
