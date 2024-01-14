import numpy as np
show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

a1 = np.random.randint(10, size=(3, 3))
a2 = np.linalg.inv(a1)
a3 = np.array([[2, 3], [5, 6]])
a4 = np.array([4, 7])

a5 = np.linalg.solve(a3, a4)

# b1 = np.linalg.inv(a3)
# b2 = b1 @ a4

show("a1", a1) ; show("a2", a2)
show("a3", a3) ; show("a4", a4) ; show("a5", a5)
show("b1 : ", b1)
show("b2 :", b2)
