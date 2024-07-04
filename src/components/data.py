from typing import Optional
import pandas as pd
import re
from PySide6.QtCore import *
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QRadioButton


class data():
    def __init__(self, main) -> None:
        self.init_df()

    def init_df(self):
        self.df = pd.DataFrame()
        self.fdf = pd.DataFrame()
        self.fileName = ''
        self.cols = dict(date='', text='', category1='',
                         category2='', category3='')

    def set_df(self, df, filename: str = ''):
        self.init_df()
        self.df = pd.DataFrame(df)
        self.fileName = filename
        self.set_col_auto()

    def get_col(self):
        cols = self.df.columns.to_list()
        cols.insert(0, "미설정")
        return cols

    def set_col_auto(self):
        self.set_date_col()
        self.set_category_col()
        self.set_text_col()

    def set_date_col(self):
        for col in self.df.columns:
            try:
                self.df[col] = pd.to_datetime(self.df[col])
                self.cols['date'] = col
                print(f"{col} : 일자열 설정 완료!")
                break
            except ValueError:
                print(f"{col}은 날짜 타입이 아닙니다.")

    def set_category_col(self):
        for col in self.df.columns:
            if re.search(r'대', col):
                self.cols['category1'] = col
            elif re.search(r'중', col):
                self.cols['category2'] = col
            elif re.search(r'소', col):
                self.cols['category3'] = col

    def set_text_col(self):
        for col in self.df.columns:
            if re.search(r'(내용|메모)', col):
                self.cols['text'] = col
                break
            else:
                self.cols['text'] = ''
        print(self.cols['text'])

    # todo : 나중에 세팅 값에서 받아올수 있도록 하기
    def set_col_manual(self, config: dict):
        column_config = config['column_config']
        rm_na = config['rm_na']
        rm_duplicate = config['rm_duplicate']

        for key in column_config:
            if column_config[key].strip() != '' and column_config[key] != '미설정':
                self.cols[key] = column_config[key]

        columns = [col for col in self.cols.values() if col != '']
        print(f"칼럼값 : {self.cols.values()}")
        df = self.df[columns].copy()
        if rm_na:
            df = df.dropna(how='all')
        if rm_duplicate:
            df = df.drop_duplicates()

        self.fdf = df
        print('set_col_manual')

    def start_df(self):
        pass


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
