import numpy as np
show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

print(np.pi)
print(np.sin(30 * np.pi / 180), np.cos(3 * np.pi / 2), end='\n\n')
a1 = np.degrees([np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4])
a2 = np.radians(a1)
a3 = np.sin(a1 * np.pi / 180)
a4 = np.cos(a2)
show("a1", a1) ; show("a2", a2) ; show("a3", a3) ; show("a4", a4)
