import sys
from typing import Optional

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import QWebEngineView

import pandas as pd
import polars as pl

#^ ---
import page
import components.session as data
import components.Menu
import components.read_df
import components.style

#^ UI components
from ui.chart import Ui_Chart
from ui.textmining import Ui_TextMining
from ui.FileInput import Ui_FileInput

## Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        
    #@ init UI
    def init_ui(self):
        self.setWindowTitle("Text분석")
        self.setMinimumSize(1000, 800)
        self.setMaximumSize(1920, 1280)
        self.setGeometry(100, 100, 1000, 800)
        self.setMenuBar(components.Menu.MenuBar())
        self.setStatusBar(QStatusBar())

    #^ 변수 생성 
        self.data = data.session(self)

    #^ 탭 구조 생성
        self.main = QTabWidget()
        self.main.setDocumentMode(True)
        self.setCentralWidget(self.main)

    #^ 탭 1: 파일 입력
        tab1 = FileInputTab()
        self.main.addTab(tab1, "파일 입력")

    #^ 탭 2: 탐색적 분석 
        tab2 = ChartTab()
        self.main.addTab(tab2, "통계 차트 생성")

    #^ 탭 3: 텍스트 마이닝 
        tab3 = TextMiningTab()
        self.main.addTab(tab3, "텍스트 마이닝")
    
    #^ 
    #^ 탭 6: Test 
        tab6 = QTabWidget()
        self.main.addTab(tab6, "TEST")
        layout6 = QHBoxLayout(tab6)
        file_input_widget = file_input(self.data, main_window=self)
        # tab6.setMovable(True)
        # for _, color in enumerate(["red", "green", "blue", "yellow"]):
        #     tab6.addTab(QWidget(), color)
        layout6.addWidget(file_input_widget)
    
    #% tab 7
        # tab7 = myui()
        # self.main.addTab(tab7, "Chart")

        self.show()

    def set_status(self, text):
        self.statusBar().showMessage(text)

    def slot_button_load(self, state, widget, label):
        filename = QFileDialog.getOpenFileName(self, 'Open file', './')

        if filename[0]:
            try:
                self.df = pl.read_csv(filename[0])
                self.create_table_widget(widget, self.df)
                label.setText(filename[0])
            except:
                return None
            finally:
                label.setText(filename[0])

    def create_table_widget(self, widget, df):
        widget.setRowCount(df.shape[0])
        widget.setColumnCount(df.shape[1])
        widget.setHorizontalHeaderLabels(df.columns)
        # widget.setVerticalHeaderLabels(df.row_index)

        #^ polars
        for row_index, row in enumerate(df.iter_rows()):
            for col_index, column in enumerate(row):
                value = column
                item = QTableWidgetItem(str(value))
                widget.setItem(row_index, col_index, item)

class MW (QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        lm = QVBoxLayout()
        self.label0 = QLabel('Enter text!')

## 파일 인풋 
class file_input(QWidget):
    def __init__(self, session:data.session, main_window:QMainWindow):
        super().__init__()
        self.session = session
        self.main_window = main_window
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        self.table_widget = QTableView()
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setAcceptDrops(True)
        self.table_widget.setDragEnabled(True)
        select_file_button = QPushButton("텍스트 파일 선택")
        select_file_button.setFixedSize(150, 50)
        select_file_button.clicked.connect(self.selectFile)
        layout.addWidget(QLabel("민원 파일을 입력하세요."))
        layout.addWidget(select_file_button)
        layout.addWidget(self.table_widget)    
        self.setLayout(layout)
        self.show()


    def selectFile(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open Text", "data/",
            "엑셀 파일 (*.xlsx *.xls *.csv);;텍스트 파일 (*.csv *.txt);;데이터프레임(*.parquet);")
        if file:
            df = components.read_df.read_df(file)
            self.session.fileName = str(file)
            self.main_window.set_status(f"현재 열린 파일 : {self.session.fileName}\t\t 일자열 : {self.session.cols['date']}")
            print(file)
            if df is not None:
                self.session.set_df(df)
                model = data.PandasModel(df)
                self.table_widget.setModel(model)
                QMessageBox.information(self, "파일 열기", "파일이 성공적으로 열렸습니다.")
            else:
                QMessageBox.warning(self, "파일 열기", "파일을 읽을 수 없습니다.")

## 공통 필터
class dataFilter(QWidget):
    def __init__(self, config:dict=dict(date='', text='')):
        super().__init__()
        layout = QVBoxLayout()
        #^ 기간 필터 

        #^ 텍스트 필터 
        text_in = QTextEdit()
        text_ex = QTextEdit()
        if config['date'] != '' :
            radio1 = QRadioButton('Radio1')
        if config['text'] != '':
            text_in.setDisabled(False)
            text_ex.setDisabled(False)

            text_in.setPlaceholderText("포함될 단어를 쉼표로 구분해서 넣으세요.")
            text_ex.setPlaceholderText("제외될 단어를 쉼표로 구분해서 넣으세요.")
        else :
            # pass
            text_in.setDisabled(True)
            text_ex.setDisabled(True)
        layout.addWidget(text_in)
        layout.addWidget(text_ex)
        self.setLayout(layout)
        self.show()

## ui 불러오기 

#& tab1 파일 입력 탭 
class FileInputTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_FileInput()
        self.ui.setupUi(self)

#& tab2 통계 차트 탭 
class ChartTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Chart()
        self.ui.setupUi(self)

#& tab3 텍스트 마이닝 탭 
class TextMiningTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_TextMining()
        self.ui.setupUi(self)







#@ Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("텍스트 분석 대시 보드")
    main_window.show()
    # app.setStyleSheet(components.style.style_sheet().default())
    sys.exit(app.exec())
