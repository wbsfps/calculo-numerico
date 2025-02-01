import numpy as np


def A(x):
    return 2.25 * (200 - x)**2


def simpson(func, a, b, n):
    if n % 2 != 0:
        n += 1

    x = np.linspace(a, b, n+1)
    y = func(x)

    h = (b - a) / n

    integral = h/3 * (y[0] + y[-1] +
                      4 * np.sum(y[1:-1:2]) +
                      2 * np.sum(y[2:-1:2]))
    return integral


a = 0    # altura inicial
b = 150  # altura total
n = 50   # subintervalos


def integral(x):
    return x * A(x)


integral_base = simpson(integral, a, b, n)

constante = 2014
trabalho_total = constante * integral_base

trabalho_de_cada_operario = 1.742 * 10 ** 8

num_operarios = trabalho_total / trabalho_de_cada_operario

print(f"Jornada total: {trabalho_total:.4f} kg.m")
print(f"Quantidade de operários: {num_operarios:.0f}")
