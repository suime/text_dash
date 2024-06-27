import pandas as pd

def read_df(fileName:str):
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
