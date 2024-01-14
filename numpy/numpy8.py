import numpy as np

show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

a1 = np.arange(1, 10+1)**2
a2 = a1[2:9]
show('a1 : ', a1)
show('a2 : ', a2)
a1[3] = a1[1] + a1[2]
print(a1)
a2[:5:2] = 10_1000
for i in range(len(a1)):
    print(a1[ (i+1)*-1 ], end=', ')
print()