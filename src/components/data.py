from typing import Optional
import polars as pl
import pandas as pd
import re
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QRadioButton


class data():
    def __init__(self, main_window) -> None:
        self.df = pl.DataFrame()
        self.fileName = ''
        self.cols = dict(date='', text=[], category=[])

    def set_df(self, df):
        self.df = pl.DataFrame(df)
        self.set_col_auto()

    def get_col(self):
        cols = self.df.columns
        cols.insert(0, "미설정")
        return cols

    def set_col_auto(self):
        for col in self.df.columns:
            # ^ 날짜열 설정
            try:
                self.df = self.df.with_columns(
                    pl.col(col).str.to_date(r"%Y.%m.%d"))
                self.cols['date'] = col
                print(f"{col} : 일자열 설정 완료!")
            except:
                print(f"{col}은 날짜 타입이 아닙니다.")

        # ^ 카테고리열 설정
        self.cols['category'] = [col for col in self.df.columns if any(
            keyword in col for keyword in ['분류', '대', '중', '소'])]
        print(self.cols['category'])

        # ^ 텍스트열 설정
        # todo : 나중에 세팅 값에서 받아올수 있도록 하기
        self.cols['text'] = [col for col in self.df.columns if any(
            keyword in col for keyword in ['메모', '내용'])]
        print(self.cols['text'])


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
