import pandas as pd
import glob
from openpyxl.workbook import Workbook

def merge_excels():
    all_data = pd.DataFrame()
    for files in glob.glob("YouFilePath/*.xlsx"):
        df = pd.read_excel(files)
        print(df)
        all_data = all_data.append(df,ignore_index=True)

    print(all_data.describe())
    all_data.head()
    all_data.to_excel("OutputExcelFile.xlsx")


if __name__ == '__main__':
    merge_excels()