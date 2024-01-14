import numpy as np

show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

def foo(n):
    return id(n)
 
a = np.arange(20).reshape(4, 5)
b = a
c = a.view()
print(id(a))
print(b is a, id(a) == foo(a)) 
print(c is a, c.flags.owndata) # .flags.owndata 데이터 유무

d = c.reshape((2, 10))
show("d", d) ; show("a", a)
s = a[: 1:3]
s[:] = -1
show("a", a)
e = a.copy()
print(e is a)
d[1, 2] = 2_000_000
show("e", e) ; show("a", a)
m = np.arange(1_000_000)
n = m[:100].copy()
del m
