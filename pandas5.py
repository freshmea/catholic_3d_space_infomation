import numpy as np 
import pandas as pd

def main():
    ex = pd.read_excel('catholic_3d_space_infomation/data/scientists_edit_ed.xlsx', sheet_name='sci_edit', engine='openpyxl')
    # ex = ex.sort_values(by='age_days_dt', ascending=True)
    # print(ex)
    cond = (ex['age_days_dt']>20000)
    print(ex.loc[cond])

if __name__ == '__main__':
    main()