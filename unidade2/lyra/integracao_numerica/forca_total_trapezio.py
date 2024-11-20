import numpy as np


def f(z, H):
    return 200 * (z / 5 + z) * np.exp(-2 * z / H)


def trapezoidal_rule(func, a, b, n, H):
    h = (b - a) / n
    integral = 0.5 * (func(a, H) + func(b, H))
    for i in range(1, n):
        integral += func(a + i * h, H)
    integral *= h
    return integral


# Parâmetros
H = 30  # altura do mastro (m)
a = 0  # limite inferior da integral
b = H  # limite superior da integral

# Calcular a força com 10 subintervalos
n10 = 10
F_10 = trapezoidal_rule(f, a, b, n10, H)

# Calcular a força com 100 subintervalos
n100 = 100
F_100 = trapezoidal_rule(f, a, b, n100, H)


print(f"Força com 10 subintervalos: {F_10:.4f} N")
print(f"Força com 100 subintervalos: {F_100:.4f} N")
