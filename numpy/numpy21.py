import numpy as np
show = lambda m, o : print(m, o.shape, o.dtype, '\n', o, '\n')

mu, sigma = 0, 0.1
a1 = np.random.normal(mu, sigma, 5000)
a2 = np.random.normal(4, 1.7, size=(3, 4)) # N(4, 2.89)
a3 = np.random.standard_normal(5000)
a4 = 4 + 1.7 * np.random.standard_normal((3,4)) # N(4, 2.89)
show("a1:", a1)
print("mean and standard deviation:", abs(mu - np.mean(a1)), sigma - np.std(a1, ddof=1), end="\n\n")
show("a2:", a2) ; show("a3", a3) ; show("a4", a4)
