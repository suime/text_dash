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
                                QTableView, QFileDialog, QMessageBox)

from PySide6.QtWebEngineWidgets import QWebEngineView

import pandas as pd
import polars as pl

# ^ ---
import page
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
        tab3 = TextMiningTab()
        self.main.addTab(tab3, "텍스트 마이닝")

    # ^ 탭 4: 사전 
        tab4 = DictionaryTab()
        self.main.addTab(tab4, "사전")

    # ^ 탭 6: 
        tab6 = QTabWidget()
        self.main.addTab(tab6, "TEST")
        self.show()

    def set_status(self, text):
        self.statusBar().showMessage(text)


# 공통 필터


class dataFilter(QWidget):
    def __init__(self, config: dict = dict(date='', text='')):
        super().__init__()
        layout = QVBoxLayout()
        # ^ 기간 필터

        # ^ 텍스트 필터
        text_in = QTextEdit()
        text_ex = QTextEdit()
        if config['date'] != '':
            radio1 = QRadioButton('Radio1')
        if config['text'] != '':
            text_in.setDisabled(False)
            text_ex.setDisabled(False)

            text_in.setPlaceholderText("포함될 단어를 쉼표로 구분해서 넣으세요.")
            text_ex.setPlaceholderText("제외될 단어를 쉼표로 구분해서 넣으세요.")
        else:
            # pass
            text_in.setDisabled(True)
            text_ex.setDisabled(True)
        layout.addWidget(text_in)
        layout.addWidget(text_ex)
        self.setLayout(layout)
        self.show()

## ui 불러오기

# & tab1 파일 입력 탭


class FileInputTab(QWidget):
    def __init__(self, main: QMainWindow) -> None:
        super().__init__()
        self.ui = Ui_FileInput()
        self.ui.setupUi(self)
        self.ui.fileBtn.clicked.connect(lambda: self.selectFile(main))

    def selectFile(self, main):
        file, _ = QFileDialog.getOpenFileName(self, "텍스트 파일 열기",
                                              "data/", "엑셀 파일 (*.xlsx *.xls *.csv);;텍스트 파일 (*.csv *.txt);;데이터프레임(*.parquet);")
        if file:
            df = components.read_df.read_df(file)
            main.data.fileName = str(file)
            
            if df is not None:
                main.data.set_df(df)
                main.set_status(f"현재 열린 파일 : {main.data.fileName} \t \
                                일자열 : {main.data.cols['date']}")
                self.ui.tableView.setModel(data.PandasModel(df))
                QMessageBox.information(self, "파일 열기", "파일이 성공적으로 열렸습니다.")

                self.set_cols(main)
            else:
                QMessageBox.warning(self, "파일 열기", "파일을 읽을 수 없습니다.")
    
    def set_cols(self, main):
        col_list = main.data.get_col()

        self.ui.DateCol.clear()
        self.ui.DateCol.addItems(col_list)
        self.ui.DateCol.setCurrentText(main.data.cols['date'])
        
        self.ui.TextCol.clear()
        self.ui.TextCol.addItems(col_list)
        self.ui.TextCol.setCurrentText(main.data.cols['text'])




# & tab2 통계 차트 탭


class ChartTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Chart()
        self.ui.setupUi(self)

# & tab3 텍스트 마이닝 탭


class TextMiningTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_TextMining()
        self.ui.setupUi(self)

#& tab4 딕셔너리 
class DictionaryTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dictionary()
        self.ui.setupUi(self)


# @ Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("텍스트 분석 대시 보드")
    main_window.show()
    # app.setStyleSheet(components.style.style_sheet().default())
    sys.exit(app.exec())
