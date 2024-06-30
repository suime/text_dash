import sys
from PySide6.QtWidgets import (QApplication, QFileDialog, QLabel, QLineEdit, QMainWindow, QMenu,
                               QPushButton, QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QStatusBar,
                               QMessageBox, QTableView)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QAction
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
import sys

import pandas as pd
import polars as pl

#^ ---
import page
import components.session as data
import components.Menu
import components.read_df


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    #@ init UI
    def init_ui(self):
        self.setWindowTitle("Text분석")
        self.setMaximumSize(1920, 1280)
        self.setGeometry(100, 100, 1000, 800)
        self.setMenuBar(components.Menu.MenuBar())
        self.setStatusBar(QStatusBar())

    #^ 변수 생성 
        self.data = data.session(self)

    #^ 탭 구조 생성
        self.main = QTabWidget()
        self.setCentralWidget(self.main)

    #^ 탭 1: 파일 입력
        tab1 = page.main.FileInput()
        self.main.addTab(tab1, "\udb82\ude23  파일 입력")

    #^ 탭 2: 차트 생성
        tab2 = page.EDA.LineChart()
        self.main.addTab(tab2, "\udb85\udd4d  차트 생성")

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
        self.main.addTab(tab3, "\uf15c  텍스트 마이닝")

    #^ 탭 4: AI
        tab4 = QWidget()
        self.main.addTab(tab4, "\udb85\udea3  AI 분석")
        layout4 = QVBoxLayout(tab4)
        self.status_label = QLabel('CSV 파일을 불러와주세요.', self)
        layout4.addWidget(self.status_label)

    #^ 탭 5: 설명서
        tab5 = QWidget()
        self.main.addTab(tab5, "\udb81\udc77  사용설명서")
        layout5 = QVBoxLayout(tab5)
        layout5.addWidget(QLabel("메뉴얼을 만드는 곳 "))
    
    #^ 탭 6: Test 
        tab6 = QTabWidget()
        tab6.setTabPosition(QTabWidget.West)
        tab6.setMovable(True)
        self.main.addTab(tab6, "TEST")
        # for _, color in enumerate(["red", "green", "blue", "yellow"]):
        #     tab6.addTab(QWidget(), color)
        tab6.addTab(file_input(self.data, main_window=self), '파일 인풋')
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

class file_input(QWidget):
    def __init__(self, session, main_window):
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
            self.main_window.set_status(f"현재 열린 파일 : {self.session.fileName}")
            print(file)
            if df is not None:
                self.session.set_df(df)
                model = PandasModel(df)
                self.table_widget.setModel(model)
                QMessageBox.information(self, "파일 열기", "파일이 성공적으로 열렸습니다.")
            else:
                QMessageBox.warning(self, "파일 열기", "파일을 읽을 수 없습니다.")

class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """
    def __init__(self, dataframe: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe
    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return str(self._dataframe.iloc[index.row(), index.column()])

        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._dataframe.columns[section])

            if orientation == Qt.Vertical:
                return str(self._dataframe.index[section])

        return None
        

style_sheet = """
    QFrame#ContainerFrame{ /* Style border for TaskContainer class */
        background-color: #A0A0A0;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px
    }
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("텍스트 분석 보드")
    main_window.show()
    app.setStyleSheet(style_sheet)
    sys.exit(app.exec())
