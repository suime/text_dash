from unicodedata import category
import polars as pl
import re 

class session():
    def __init__(self, main_window) -> None:
        self.df = pl.DataFrame()
        self.fileName = ''
        self.cols = dict(date='', text=[], category = [])

    def set_df(self, df):
        self.df = pl.DataFrame(df)
        self.set_col_auto()

    def set_col_auto(self):
        for col in self.df.columns:
            #^ 날짜열 설정 
            try: 
                self.df = self.df.with_columns(pl.col(col).str.to_date(r"%Y.%m.%d"))
                self.cols['date'] = col
                print(f"{col} : 일자열 설정 완료!")
            except:
                print(f"{col}은 날짜 타입이 아닙니다.")
                

        #^ 카테고리열 설정 
        self.cols['category'] = [col for col in self.df.columns if any(keyword in col for keyword in ['분류', '대', '중', '소'])]
        print(self.cols['category'])

        #^ 텍스트열 설정
        self.cols['text'] = [col for col in self.df.columns if any(keyword in col for keyword in ['메모', '내용'])]

