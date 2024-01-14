import numpy as np

show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

a1 = np.fromfunction(lambda x, y, z: x + y + z, (2, 5, 4), dtype=int)

a2 = np.arange(1, (1*5*4)+1).reshape((1, 5, 4)) * 10
a3 = np.vstack((a1[0, ...], a2[0, ...]))
a4 = np.hstack((a1[1, ...], a2[0, ...]))
a5 = np.concatenate((a1, a2), 0)
show("a1", a1) ; show("a2", a2)
show("a3", a3) ; show("a4", a4) ; show("a5", a5)
