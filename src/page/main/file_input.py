from PySide6.QtWebEngineWidgets import QWebEngineView
import plotly.graph_objects as go
import plotly.offline as plt
import pandas as pd

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class FileInput(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        view = QWebEngineView()
        view.setHtml(self.get_html())
        layout.addWidget(view)
        layout.addWidget(QLineEdit('텍스트'))

    def get_html(self):
        df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 11, 12, 13]})
        fig = go.Figure(data=go.Scatter(
            x=df['x'], y=df['y'], mode='lines+markers'))
        fig.update_layout(title='Simple Line Chart',
                        xaxis_title='X Axis', yaxis_title='Y Axis')

        # html = fig.to_html(include_plotlyjs="cdn")
        html = plt.plot(fig, include_plotlyjs='cdn', output_type='div')

        # ^ min.plotly를 로컬에서 저장하고 해당거를 참조하는 태그를 추가해서 plotly를 구현한다.
        html = '<script charset="utf-8" src="C:\\Users\\Administrator\\plotly.min.js"></script>' + html

        return html

