# https://www.youtube.com/watch?v=A9eIj_DwUcs

import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return (2 * x * np.exp(x) - 3)


def secante(x0, x1, erro, it_max):
    it = 0
    er = 1
    xa1 = x0
    x = x1

    while (er >= erro and it < it_max):
        xa2 = xa1
        xa1 = x
        x = xa1 - f(xa1) * (xa2 - xa1) / ((f(xa2) - f(xa1)))
        er = np.abs((x - xa1) / x)
        it += 1

    return (x, er, it)


x0 = 3
x1 = 3.5
erro = 10**-5
it_max = 10

res = secante(x0, x1, erro, it_max)

print(f'Valor da raíz {res[0]}')
print(f'Valor do erro {res[1]}')
print(f'Valor de interações máximas {res[2]}')
