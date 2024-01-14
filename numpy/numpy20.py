import numpy as np
show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

np.random.seed(1)

a1 = np.arange(9)
np.random.shuffle(a1)

a2 = np.arange(3*3).reshape((3, 3))
np.random.shuffle(a2)

a3 = np.random.choice([4, 2, 6, 1], 3, False, [0.4, 0.2, 0.3, 0.1])

show("a1", a1)
show("a2", a2)
show("a3", a3)
