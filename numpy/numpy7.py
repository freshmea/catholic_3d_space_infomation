import numpy as np

def show(m, o):
    print(m, o.ndim, o.size, o.shape, o.dtype,'\n', o,'\n')

def main():
    # a1 = np.random.randint(10, size=(3,3))
    # a2 = np.linalg.inv(a1)
    
    a3 = np.array([[2, 3, 4],[5, 6, 7],[1, 1 ,1]]) 
    # 2x + 3y + 4z = 4 , 5x + 6y + 7z = 7, x + y + z = 1
    a4 = np.array([4,7,1])
    a5 = np.linalg.solve(a3, a4)
    
    show('a5: ', a5)
if __name__ == '__main__':
    main()