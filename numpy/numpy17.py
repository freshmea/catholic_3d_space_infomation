import numpy as np
show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

a1 = np.array([[2, -1, 5], [-5, 2, 2], [2, 1, 3]])
a2 = np.array([[0, 1, 0], [1, 0, 1], [1, 1, 0]])
a3 = np.array([1, -1, 1])
a4 = np.array([1, 0, 1]).reshape((3,1))

b1 = np.dot(a1, a2)
b2 = a1.dot(a3)
b3 = a1 @ a4

show("a1:", a1) ; show("a2:", a2) ; show("a3:", a3) ; show("a4:", a4)
show("b1:", b1) ; show("b2:", b2) ; show("b3:", b3)