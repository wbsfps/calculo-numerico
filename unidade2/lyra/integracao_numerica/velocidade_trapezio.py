import numpy as np


def f(z, H):
    return 200 * (z / 5 + z) * np.exp(-2 * z / H)


def simpson_1_3(f, a, b, n, H):
    h = (b - a) / n  # Tamanho do subintervalo
    z = np.linspace(a, b, n + 1)
    f_values = f(z, H)

    integral = f_values[0] + f_values[-1]  # f(z_0) + f(z_n)
    integral += 4 * np.sum(f_values[1:-1:2])  # 4 * f(z_1, z_3, z_5, ...)
    integral += 2 * np.sum(f_values[2:-2:2])  # 2 * f(z_2, z_4, z_6, ...)

    integral *= h / 3
    return integral


# Definindo o intervalo e altura do mastro
a = 0  # Elevação inicial
b = 30  # Elevação final
H = 30  # Altura do mastro

F_10_subintervalos = simpson_1_3(f, a, b, 10, H)

F_100_subintervalos = simpson_1_3(f, a, b, 100, H)

print(f"Força com 10 subintervalos: {F_10_subintervalos:.4f} N")
print(f"Força com 100 subintervalos: {F_100_subintervalos:.4f} N")
