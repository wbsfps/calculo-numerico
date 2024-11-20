import numpy as np


def f(x):
    return np.exp(x) * x**2  # Exemplo: função quadrática

# Método Simples do Trapézio


def trapezio_simples(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

# Método Composto do Trapézio


def trapezio_composto(f, a, b, n):
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n):
        soma += 2 * f(a + i * h)
    return (h / 2) * soma


# Exemplo de uso
a = 0  # Limite inferior
b = 1  # Limite superior
n = 4  # Número de subintervalos (par para Simpson composto)

print("Trapézio Simples:", trapezio_simples(f, a, b))
print("Trapézio Composto:", trapezio_composto(f, a, b, n))
