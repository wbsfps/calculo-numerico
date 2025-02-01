import numpy as np


def f(x):
    return 35 * (2 + 0.9**x)


def integracao_trapezio(func, a, b, n):
    x = np.linspace(a, b, n+1)
    y = func(x)

    h = (b - a) / n
    integral = h / 2 * np.sum(y[:-1] + y[1:])

    return integral


a = 0
b = 24
quantidade_subintervalos = 20

resultado = integracao_trapezio(f, a, b, quantidade_subintervalos)
print(f"Questão 1 - Resultado: {resultado:.4f} metros")
