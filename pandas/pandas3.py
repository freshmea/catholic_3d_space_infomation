import numpy as np 
import pandas as pd

def main():
    df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['가', '나', '다'])
    print(df)
    data = {'name':['kim', 'Lee', 'Park'], 'age':[34, 24, 50], 'children':[2, 1, 3]}
    df2 = pd.DataFrame(data)
    print(df2)
    
if __name__ == '__main__':
    main()