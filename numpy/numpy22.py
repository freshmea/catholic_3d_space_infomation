import numpy as np
show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

a1 = np.arange(360+1)
a2 = np.sin(a1 * np.pi / 180)
show("a1", a1)
show("a2", a2)
np.savez_compressed("data/sin_sample", x=a1, y=a2)
a3 = np.load("data/sin_sample.npz")
# print((a3['x'] == a1).all()) # a3[‘x’] == a1의 결과는 불 배열이며, all()은 전체 요소가 같은지 검사
# print((a3['y'] == a2).all())
b1 = a3['x']
b2 = a3['y']
a3.close()

print(b1)
