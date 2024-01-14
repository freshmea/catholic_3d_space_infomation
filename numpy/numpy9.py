import numpy as np

show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

a1 = np.fromfunction(lambda x,y,z :x+y+z, (2,5,4), dtype=int)
a2 = a1[:, 1::2, :3]* 10
a2[1, ...] = -1

show('a1 :', a1)
for array in a2:
    print("out:\n", array)
