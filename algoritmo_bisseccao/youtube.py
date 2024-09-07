# https://www.youtube.com/watch?v=I4ZeLngZBvA&t=1033s
# (2 * x * np.exp(x) - 3)

import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return (2 * x * np.exp(x) - 3)


def bissec(a, b, erro, it_max):
    it = 0
    x = 0

    Er = 1

    while (Er >= erro and it < it_max):
        xold = x
        x = (a + b) / 2
        Er = np.abs((x - xold) / x)

        if (f(a) * f(x) < 0):
            b = x
        else:
            a = x
        it += 1
    return (x, Er, it)


a = 3
b = 6

m = np.arange(a, b, 1)
plt.plot(m, f(m))
plt.show()

erro = 10**-5
it_max = 6

res = bissec(a, b, erro, 10)

print('O valor da raiz é ', res[0])
print("O erro relativo foi", res[1])
print("Número de iterações", res[2])
