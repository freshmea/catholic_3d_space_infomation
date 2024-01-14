import numpy as np
show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

a1 = np.array([-2.5, 1, -1.7, 5.1, 4.0, -0.2, 6.8])
a2 = np.absolute(a1)
a3 = np.ceil(a1)
a4 = np.floor(a1)
a5 = np.sqrt(a2)

show("a1", a1)
show("a2", a2)
show("a3", a3)
show("a4", a4)
show("a5", a5)
