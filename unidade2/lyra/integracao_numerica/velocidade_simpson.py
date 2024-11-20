import numpy as np

# constantes
g = 9.81  # m/s^2 (aceleração devido à gravidade)
m = 68.1  # kg (massa do objeto)
cd = 0.25  # kg/m (coeficiente de arrasto)


def v(t):
    return np.sqrt((g * m) / cd) * np.tanh(np.sqrt((g * cd) / m) * t)


def simpson_1_3(f, a, b, n):
    h = (b - a) / n  # Tamanho do subintervalo
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = y[0] + y[-1]  # f(x_0) + f(x_n)
    integral += 4 * np.sum(y[1:-1:2])  # 4 * f(x_1, x_3, x_5, ...)
    integral += 2 * np.sum(y[2:-2:2])  # 2 * f(x_2, x_4, x_6, ...)

    integral *= h / 3
    return integral


# Intervalo
a = 0  # tempo inicial
b = 10  # tempo final


dist_2_subintervalos = simpson_1_3(v, a, b, 2)


dist_10_subintervalos = simpson_1_3(v, a, b, 10)

print(dist_2_subintervalos, dist_10_subintervalos)
