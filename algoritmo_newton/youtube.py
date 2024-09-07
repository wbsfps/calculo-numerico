# https://www.youtube.com/watch?v=2ySlhIQ_v00

import numpy as np
from matplotlib import pyplot as plt


def f(x):
    y = (2 * x * np.exp(x) - 3)
    return y


def g(x):
    z = (2 * np.exp(x)) + (2 * x * np.exp(x))
    return z


vetor = []
t = range(1, 10)

x = 4  # chute inicial
for n in range(1, 10):  # os 9 primeiros valores
    x = x - f(x)/g(x)

    vetor.append(x)


plt.plot(vetor, t)  # criando gráfico
plt.grid()
plt.xlabel("Valores de x")
plt.ylabel("Valores de y")
plt.title("Gráfico da função y = (2 * x * np.exp(x) - 3)")
plt.show()  # mostrando gráfico
