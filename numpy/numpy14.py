import numpy as np
show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

d1 = np.exp(1)
a1 = np.exp([i for i in range(1, 10 + 1, 2)])
d2 = np.log(np.e)
a2 = np.log(a1)

print("d1:", d1)
print("d2:", d2)
show("a1", a1)
show("a2", a2)
