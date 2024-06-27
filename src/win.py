import sys
from PySide6.QtWidgets import (QApplication, QFileDialog, QLabel, QLineEdit, QMainWindow, QMenu,
                               QPushButton, QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QStatusBar)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QAction
import pandas as pd
import polars as pl



#^ ---
import page

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    #^ 변수 생성 
        self.df = pl.DataFrame()
        self.filename =''

    #^ 탭 구조 생성
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

    #^ 탭 1: 파일 입력
        tab1 = page.main.FileInput()
        self.tab_widget.addTab(tab1, "\uf0c7  파일 입력")

    #^ 탭 2: 차트 생성
        tab2 = page.EDA.LineChart()
        self.tab_widget.addTab(tab2, "\udb85\udd4d  차트 생성")

        # table_widget = QTableWidget()
        # layout2.addWidget(table_widget)
        # button_load = QPushButton("Load")
        # file_label = QLabel(self.filename)
        # button_load.clicked.connect(
        #     lambda state, widget=table_widget: self.slot_button_load(state, widget, label = file_label))
        # layout2.addWidget(file_label)
        # layout2.addWidget(button_load)

    #^ 탭 3: 텍스트 마이닝 
        tab3 = MW()
        self.tab_widget.addTab(tab3, "\uf15c  텍스트 마이닝")
        # 여기에 필요한 위젯을 추가하세요.

    #^ 탭 4: AI
        tab4 = QWidget()
        self.tab_widget.addTab(tab4, "파일 입출력")
        layout4 = QVBoxLayout(tab4)

        self.status_label = QLabel('CSV 파일을 불러와주세요.', self)
        layout4.addWidget(self.status_label)

    def init_ui(self):
        self.setWindowTitle("Text분석")
        self.setMaximumSize(1920, 1280)
        self.setGeometry(100, 100, 800, 600)
        self.create_actions()       # menu bar 생성. 앞서 생성된 action들을 활용.
        menubar = self.menuBar()
        menu = QMenu('File', self)
        menu.addAction(QAction("open file", self))
        menubar.addMenu(menu)
        self.setStatusBar(QStatusBar())
        self.show()

    def create_actions(self):
        self.quit_act = QAction("Quit")
        self.quit_act.setShortcut("Ctrl+X")
        self.quit_act.triggered.connect(self.close)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("텍스트 분석 보드")
    main_window.show()
    sys.exit(app.exec())
