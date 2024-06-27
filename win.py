import sys
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QTabWidget, QVBoxLayout, QWidget, QStatusBar)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
import plotly.graph_objects as go
import pandas as pd
import plotly.offline as plt

from src.page.main import file_input

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

        df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 11, 12, 13]})
        fig = go.Figure(data=go.Scatter(
            x=df['x'], y=df['y'], mode='lines+markers'))
        fig.update_layout(title='Simple Line Chart',
                          xaxis_title='X Axis', yaxis_title='Y Axis')

        # html = fig.to_html(include_plotlyjs="cdn")
        html = plt.plot(fig, include_plotlyjs='cdn', output_type='div')
        
        #^ min.plotly를 로컬에서 저장하고 해당거를 참조하는 태그를 추가해서 plotly를 구현한다.
        html = '<script charset="utf-8" src="C:\\Users\\Administrator\\plotly.min.js"></script>' + html
        view1 = QWebEngineView()

        view1.setHtml(html)
        layout1.addWidget(view1)
        layout1.addWidget(QLineEdit('텍스트'))

        # 탭 2: 추가될 내용
        tab2 = QWidget()
        self.tab_widget.addTab(tab2, "1번 내용")
        layout2 = QVBoxLayout(tab2)

        # 여기에 필요한 위젯을 추가하세요.
        layout2.addWidget(QLabel('What is most important?'))
        layout2.addWidget(QLabel('What is most important?2'))

        # 탭 3: 추가될 내용
        tab3 = MW()
        self.tab_widget.addTab(tab3, "2번 내용")
        # 여기에 필요한 위젯을 추가하세요.

    def init_ui(self):
        self.setWindowTitle("Plotly in PySide6 Example")
        self.setMaximumSize(1920, 1280)
        self.setGeometry(100, 100, 800, 600)
        self.create_actions()       # menu bar 생성. 앞서 생성된 action들을 활용.
        self.setStatusBar(QStatusBar())
        self.show()

    def create_actions(self):
        self.quit_act = QAction("Quit")
        self.quit_act.setShortcut("Ctrl+X")
        # self.quit_act.setIcon(QIcon("img/exit.png"),"Quit") #action의 icon과 이름을 한번에 지정.
        self.quit_act.triggered.connect(self.close)


class MW (QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ex: QVBoxLayout and QSizePolicy")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        lm = QVBoxLayout()

        self.label0 = QLabel('Enter text!')
        lm.addWidget(self.label0)

        lm.addSpacing(10)  # fixed spacing

        self.label1 = QLabel('--------')
        lm.addWidget(self.label1)

        lm.addSpacing(20)  # fixed spacing

        self.line_edit = QLineEdit()
        # —————————————————————————————————-
        # sizePolicy attribute를 변경한 효과를 보기 위해선
        # 다음 주석을 해제해볼 것 (lm.addStrech 등을 반드시 주석처리할 것.)
        # self.line_edit.setSizePolicy(
        #     QSizePolicy.Policy.Preferred,
        #     QSizePolicy.Policy.Preferred)

        # ———————————————————————————————-
        # 아래는 Expanding으로 sizePolicy를 설정한 경우임.
        # 역시 lm.addStrech를 주석처리해야 한다.
        # self.line_edit.setSizePolicy(
        #     QSizePolicy.Policy.Expanding,
        #     QSizePolicy.Policy.Expanding)
        lm.addWidget(self.line_edit)

        # sizePolicy 효과를 보기 위해서는 아래 라인 주석처리 필요.
        lm.addStretch(1)

        self.label2 = QLabel('--------')
        lm.addWidget(self.label2)

        # sizePolicy 효과를 보기 위해서는 아래 라인 주석처리 필요.
        lm.addStretch(2)

        self.push_button = QPushButton("Check")
        # 아래는 Expanding으로 sizePolicy를 설정한 경우임.
        # 역시 lm.addStrech를 주석처리해야 한다.
        # self.push_button.setSizePolicy(
        #     QSizePolicy.Policy.Expanding,
        #     QSizePolicy.Policy.Expanding)
        lm.addWidget(self.push_button)
        # self.print_qsize()
        self.setLayout(lm)

    def print_qsize(self):

        print('==============================')
        # print("label0's ideal size (=sizeHint)     :", self.label0.sizeHint())
        # print("label1's ideal size (=sizeHint)     :", self.label1.sizeHint())
        # print("label2's ideal size (=sizeHint)     :", self.label2.sizeHint())
        # print("line_edit's ideal size (=sizeHint)  :", self.line_edit.sizeHint())
        # print("push_button's ideal size (=sizeHint):",
        #       self.push_button.sizeHint())
        # print('==============================')
        # print("label0's size      :", self.label0.size(), "/", self.label0     .sizePolicy(
        # ).verticalPolicy(), "/", self.label0     .sizePolicy().horizontalPolicy())
        # print("label1's size      :", self.label1.size(), "/", self.label1     .sizePolicy(
        # ).verticalPolicy(), "/", self.label1     .sizePolicy().horizontalPolicy())
        # print("label2's size      :", self.label2.size(), "/", self.label2     .sizePolicy(
        # ).verticalPolicy(), "/", self.label2     .sizePolicy().horizontalPolicy())
        # print("line_edit's size   :", self.line_edit.size(), "/", self.line_edit  .sizePolicy(
        # ).verticalPolicy(), "/", self.line_edit  .sizePolicy().horizontalPolicy())
        # print("push_button's size :", self.push_button.size(), "/", self.push_button.sizePolicy(
        # ).verticalPolicy(), "/", self.push_button.sizePolicy().horizontalPolicy())

    # resize event handler
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.print_qsize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("텍스트 분석 보드")
    main_window.show()
    sys.exit(app.exec())
