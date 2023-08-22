import numpy as np

def show(m, o):
    print(m, o.ndim, o.size, o.shape, o.dtype,'\n', o,'\n')

def main():
    a = np.arange(20).reshape(4,5)
    b = a 
    c = a.view()
    d = a.copy()
    print( b is a )
    show("a: ", a)
    show("b: ", b)
    show("c: ", c)
    show("d: ", d)
    b[0] = 7000
    show("a: ", a)
    show('c: ', c)
    show("d: ", d)
if __name__ == '__main__':
    main()