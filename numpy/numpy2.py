import numpy as np

def show(m, o):
    print(m, o.ndim, o.size, o.shape, o.dtype,'\n', o,'\n')

def main():
    array1 = np.arange(27, dtype=np.int8)
    show('array1', array1)
    array2 = np.arange(1, 10+1, 0.1)
    show('array2', array2)
    array3 = np.linspace(1, 10, 19)
    show('array3', array3)

if __name__ == '__main__':
    main()