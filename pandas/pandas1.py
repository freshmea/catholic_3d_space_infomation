import numpy as np 
import pandas as pd

def main():
    a = np.arange(100, 105, dtype=np.int8)
    print(a)
    s1 = pd.Series(a)
    s2 = pd.Series(a, dtype='int32')
    print(s1)
    print(s2)
    s3 = pd.Series(['부장', '차장', '대리', '사원', '인턴'])
    print(s3)
    print(s3[1:3])
    print(s1 > 102)
    print(s1[s1 > 102])

if __name__ == '__main__':
    main()