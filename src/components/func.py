"""
# Functions
여러 군데서 자주 쓰이는 각종 함수 집합입니다.
"""
import os

from PySide6.QtWidgets import (QWidget, QFileDialog)
from PySide6.QtCore import QUrl

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as plt


def read_df(fileName: str):
    file_extensions = {
        'xls': pd.read_excel,
        'xlsx': pd.read_excel,
        'csv': pd.read_csv,
        'parquet': pd.read_parquet
    }
    for ext, func in file_extensions.items():
        if fileName.endswith(ext):
            return func(fileName)
    return None


def to_regex(text: str):
    import re
    pattern = re.sub(r'\s*[,\n]\s*', '|', text)
    pattern = re.sub(r'\|+', '|', pattern)
    pattern = pattern.strip('|')
    return pattern


def get_table_plot(df: pd.DataFrame):
    """
    Pandas DataFrame을 Plotly의 go.Table로 출력하는 함수

    Parameters:
    df (pd.DataFrame): 출력할 데이터 프레임

    Returns:
    fig (go.Figure): Plotly Figure 객체
    """
    # 데이터 프레임의 컬럼과 값을 리스트로 변환
    header = list(df.columns)

    # Plotly의 go.Table 객체 생성
    table = go.Table(
        header=dict(values=header, fill_color='grey',
                    align='center', line_color='darkslategray',
                    font=dict(color='white', size=13)),
        cells=dict(values=[df[col] for col in df.columns],
                   fill_color='white',
                   line_color='darkslategray',
                   align=['left', 'center'],
                   font=dict(color='black', size=12),
                   format=[None if df[col].dtype == 'object' else ',.0f' for col in df.columns]))

    # Figure 객체 생성
    fig = go.Figure(data=[table])
    return fig


def set_plot(fig: go.Figure,
             name: str = 'temp',
             config: dict = {'bgcolor': 'white', 'font': '맑은 고딕'}
             ):
    # 기본 플로틀리 차트
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',
                      paper_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(margin=dict(r=5, l=5, t=20, b=0))

    html_config = dict(toImageButtonOptions={
        'format': 'png',  # one of png, svg, jpeg, webp
        'filename': f'dash_chart\\{name}.png',
        'height': 500,
        'width': 700,
    }, displaylogo=False)

    if not os.path.exists(r"dash_chart"):
        os.makedirs(r"dash_chart")
    filename = f"dash_chart\\{name}.html"
    plt.plot(fig, output_type='file', auto_open=False,
             filename=filename, config=html_config)
    html_path = os.path.realpath(filename)
    html_path = QUrl.fromLocalFile(html_path)
    return html_path


def to_image(QWidget: QWidget, dir: str = ''):
    # 차트 위젯의 내용을 QPixmap으로 캡처
    pixmap = QWidget.grab()
    # 이미지 저장
    filename, _ = QFileDialog.getSaveFileName(
        None, "차트 저장", dir, "PNG 파일 (*.png);;JPEG 파일 (*.jpg *.jpeg)")
    if filename:
        pixmap.save(filename)
        print(f"이미지가 {filename}에 저장되었습니다.")


def to_excel(df: pd.DataFrame, dir: str = ''):
    # 파일 저장
    filename, _ = QFileDialog.getSaveFileName(
        None, "차트 저장하기", dir, "xlsx 파일 (*.xlsx *.xls);;csv 파일 (*.csv)")
    if filename:
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            df.to_excel(filename, index=False)
        elif filename.endswith('.csv'):
            df.to_csv(filename, encoding='UTF-8', index=False)
        print(f"데이터가 {filename}에 저장되었습니다.")