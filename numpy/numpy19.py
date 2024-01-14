import numpy as np
show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

a1 = np.random.random(6)
a2 = np.random.random((2, 3))
a3 = np.random.uniform(1.0, 2.0, (2, 3))
d = np.random.randint(10)
a4 = np.random.randint(1, 10, (2, 3))

show("a1", a1) ; show("a2", a2) ; show("a3", a3)
print("d:", d) ; show("a4", a4)
