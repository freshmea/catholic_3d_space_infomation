import numpy as np
show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

a = np.arange(24).reshape(3, 2, 4)

result = np.vsplit(a, 3)
print(type(result))

b1, b2, b3 = np.vsplit(a, 3)
b4, b5 = np.vsplit(a, np.array([1]))
c1, c2 = np.hsplit(a, 2)

show("a", a)
show("b1", b1) ; show("b2", b2) ; show("b3", b3) ; show("b4", b4) ; show("b5", b5)
show("c1", c1) ; show("c2", c2)
