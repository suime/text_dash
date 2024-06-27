import sys
from PySide6.QtWidgets import (QApplication, QFileDialog, QLabel, QLineEdit, QMainWindow, QMenu,
                               QPushButton, QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QStatusBar)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
import plotly.graph_objects as go
import pandas as pd
import plotly.offline as plt
import sys

import page


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # 탭 위젯 생성
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # 탭 1: Plotly 차트
        tab1 = QWidget()
        self.tab_widget.addTab(tab1, "플롯틀리 차트")
        layout1 = QVBoxLayout(tab1)
        view1 = QWebEngineView()


        html = page.main.FileInput()
        view1.setHtml(html.get_html())

        layout1.addWidget(view1)
        layout1.addWidget(QLineEdit('텍스트'))

        # 탭 2: 추가될 내용
        tab2 = QWidget()
        self.tab_widget.addTab(tab2, "1번 내용")
        layout2 = QVBoxLayout(tab2)

        table_widget = QTableWidget()
        layout2.addWidget(table_widget)
        button_load = QPushButton("Load")
        button_load.clicked.connect(
            lambda state, widget=table_widget: self.slot_button_load(state, widget))
        layout2.addWidget(button_load)

        # 여기에 필요한 위젯을 추가하세요.
        layout2.addWidget(QLabel('차트 추가할 예정 '))

        # 탭 3: 추가될 내용
        tab3 = MW()
        self.tab_widget.addTab(tab3, "2번 내용")
        # 여기에 필요한 위젯을 추가하세요.

    def init_ui(self):
        self.setWindowTitle("Plotly in PySide6 Example")
        self.setMaximumSize(1920, 1280)
        self.setGeometry(100, 100, 800, 600)
        self.create_actions()       # menu bar 생성. 앞서 생성된 action들을 활용.
        menubar = self.menuBar()
        menu = QMenu('File', self)
        menu.addAction(QAction("open fiel", self))
        menubar.addMenu(menu)

        self.setStatusBar(QStatusBar())
        self.show()

    def create_actions(self):
        self.quit_act = QAction("Quit")
        self.quit_act.setShortcut("Ctrl+X")
        # self.quit_act.setIcon(QIcon("img/exit.png"),"Quit") #action의 icon과 이름을 한번에 지정.
        self.quit_act.triggered.connect(self.close)

    def slot_button_load(self, state, widget):
        filename = QFileDialog.getOpenFileName(self, 'Open file', './')

        if filename[0]:
            df = pd.read_csv(filename[0], index_col=0)
            self.create_table_widget(widget, df)

    def create_table_widget(self, widget, df):
        widget.setRowCount(len(df.index))
        widget.setColumnCount(len(df.columns))
        widget.setHorizontalHeaderLabels(df.columns)
        widget.setVerticalHeaderLabels(df.index)

        for row_index, row in enumerate(df.index):
            for col_index, column in enumerate(df.columns):
                value = df.loc[row][column]
                item = QTableWidgetItem(value)
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
