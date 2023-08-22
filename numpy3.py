import numpy as np

def show(m, o):
    print(m, o.ndim, o.size, o.shape, o.dtype,'\n', o,'\n')

def main():
    a0 = np.linspace(1, 12, 12)
    a1 = np.linspace(1, 12, 12).reshape((2,3,2))
    a2 = np.zeros_like(a1)
    a3 = np.zeros((5,5,5))
    show('a0: ', a0)
    show('a1: ', a1)
    show('a2: ', a2)
    show('a3: ', a3)
    print(a1[1][2][1])
    print(a1[1, 2, 1])
    

if __name__ == '__main__':
    main()