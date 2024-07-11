"""
# Elements
여러군데서 재사용되는 요소들 집합입니다.
"""
import os
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QMenuBar, QMenu, QApplication, QWidget, QVBoxLayout, QComboBox
from PySide6.QtGui import QAction, QFontDatabase
import pandas as pd


class MenuBar(QMenuBar):
    def __init__(self) -> None:
        super().__init__()
        self.init_menu()

    # 메뉴 전체
    def init_menu(self):
        self.init_app()
        self.init_file()

    # 앱 메뉴
    def init_app(self):
        menu = QMenu('텍스트 분석보드', self)
        # ^ 도움말
        menu_help = QAction("도움말", self)
        menu_help.setShortcut("Alt+H")

        # ^ 종료하기
        menu_quit = QAction("종료하기", self)
        menu_quit.setShortcut("Ctrl+Q")
        menu_quit.triggered.connect(QApplication.instance().quit)
        #> 메뉴가 아니라 메인 윈도우가 꺼지도록 

        menu.addAction(menu_help)
        menu.addSeparator()
        menu.addAction(menu_quit)
        # *
        # * 프로그램 정보
        # *
        # *
        # * 기본설정
        # * 종료하기
        self.addMenu(menu)

    # 파일 메뉴
    def init_file(self):
        menu = QMenu('파일', self)

        # ^ 파일 열기
        c_open_file = QAction("파일 열기", self)
        c_open_file.triggered.connect(self.close)

        menu.addAction(c_open_file)
        menu.addSeparator()

        # * 파일 열기
        # * 파일 초기화
        self.addMenu(menu)


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


class FontSelector(QWidget):
    def __init__(self, font_path=r"C:\Windows\Fonts"):
        super().__init__()
        self.font_path = font_path
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.combo_box = QComboBox(self)
        self.load_fonts()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.combo_box)
        self.setLayout(layout)

    def load_fonts(self):
        font_files = [f for f in os.listdir(
            self.font_path) if f.endswith(('.ttf', '.otf'))]

        for font_file in font_files:
            font_path = os.path.join(self.font_path, font_file)
            font_id = QFontDatabase.addApplicationFont(font_path)
            if font_id != -1:
                font_families = QFontDatabase.applicationFontFamilies(font_id)
                for family in font_families:
                    self.combo_box.addItem(family)
