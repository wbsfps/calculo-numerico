import numpy as np


def f(x):
    return np.exp(x) * x**2


def simpson_simples(f, a, b):
    m = (a + b) / 2
    return (b - a) / 6 * (f(a) + 4 * f(m) + f(b))

# Método Composto de Simpson (1/3)


def simpson_composto(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("O número de subintervalos n deve ser par.")
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        soma += 2 * f(a + i * h)
    return (h / 3) * soma


# Exemplo de uso
a = 0  # Limite inferior
b = 1  # Limite superior
n = 4  # Número de subintervalos (par para Simpson composto)

print("Simpson Simples:", simpson_simples(f, a, b))
print("Simpson Composto:", simpson_composto(f, a, b, n))
