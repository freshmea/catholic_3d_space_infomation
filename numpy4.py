import numpy as np

def show(m, o):
    print(m, o.ndim, o.size, o.shape, o.dtype,'\n', o,'\n')

def main():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    a2 = np.linspace(5, 6, a1.size)
    a3 = np.arange(30).reshape((5,6))
    a4 = np.arange(6)
    b1 = a1 - a2
    b2 = a1 + 5
    b3 = a3 + 5
    b4 = a3 + a4
    show('a1: ', a1)
    show('a2: ', a2)
    show('a3: ', a3)
    show('b1: ', b1)
    show('b2: ', b2)
    show('b3: ', b3)
    show('b4: ', b4)

if __name__ == '__main__':
    main()