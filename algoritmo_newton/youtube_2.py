# https://www.youtube.com/watch?v=A9eIj_DwUcs

import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return (2 * x * np.exp(x) - 3)


def derivada(x):
    z = (2 * np.exp(x)) + (2 * x * np.exp(x))
    return z


def newton(x0, erro, it_max):
    it = 0
    er = 1
    x = x0

    while (er >= erro and it < it_max):
        xold = x
        x = x - f(x) / derivada(x)
        er = np.abs((x - xold) / x)
        it += 1

    return (x, er, it)


x0 = 3
erro = 10**-5
it_max = 10

res = newton(x0, erro, it_max)

print(f'Valor da raíz {res[0]}')
print(f'Valor do erro {res[1]}')
print(f'Valor de interações máximas {res[2]}')
