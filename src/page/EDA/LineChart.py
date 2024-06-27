from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class LineChart(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('LineChart'))