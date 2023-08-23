import numpy as np 
import pandas as pd

def main():
    s3 = pd.Series(['부장', '차장', '대리', '사원', '인턴'])
    index =['a', 'b', 'c', 'd', 'e']
    s3.index = index
    print(s3)
    print(s3[['b', 'c', 'e']])

if __name__ == '__main__':
    main()