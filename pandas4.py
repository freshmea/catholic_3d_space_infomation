import numpy as np 
import pandas as pd

# python3 -m pip install openpyxl
def main():
    excel1 = pd.read_excel('catholic_3d_space_infomation/data/scientists_edit_ed.xlsx', sheet_name='sci_edit', engine='openpyxl')
    print(excel1)
    
if __name__ == '__main__':
    main()