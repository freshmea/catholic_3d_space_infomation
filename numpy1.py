import numpy as np

def show(m, o):
    print(m, o.ndim, o.size, o.shape, o.dtype,'\n', o,'\n')

def main():
    array1 = np.array([1, 2, 3, 4, 5], dtype=np.int8)
    show('a1: ', array1)

    li1 = [1,2,3,4,5]
    print(li1)

if __name__ == '__main__':
    main()