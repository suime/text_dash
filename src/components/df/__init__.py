from unicodedata import category
import pandas as pd
import polars as pl

class df():
    def __init__(self, filename:str) -> None:
        if filename :
            self.read_df(filename)
        else:
            self.df = pl.DataFrame()

        self.col = dict(date="", category = [], text="")
        self.tf = None
        self.wc = None
    
    #^ 파일 읽기 
    def read_df(self, filename:str):
        """read_df 
        - 텍스트 파일 읽어드리는것 
        """
        file_extensions = {
            'xls': pd.read_excel,
            'xlsx': pd.read_excel,
            'csv': pd.read_csv,
            'parquet': pd.read_parquet
        }
        for ext, func in file_extensions.items():
            if filename.endswith(ext):
                self.df = func(filename)
    
    #^ 필터 
    def filter(self, config:dict):

        return pl.DataFrame()

    def to_wc(self, config:dict):

        return pl.DataFrame()
        

