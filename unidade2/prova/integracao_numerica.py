# Alunos: William Batista e João Alfredo

import math


def f(x):
    return (math.exp(x) * math.sin(x)) / (1 + x ** 2)


def trapezios(f, a, b, n):
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n):
        soma += 2 * f(a + i * h)
    return (h / 2) * soma

# Método de Simpson (1/3)


def simpson_composto(f, a, b, n):
    if n % 2 != 0:
        return "A quantidade de subintervalos deve ser par."
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)
    for i in range(2, n, 2):
        soma += 2 * f(a + i * h)
    return (h / 3) * soma


a = 0
b = 2
intervalo_1 = 1
intervalo_2 = 5
intervalo_3 = 20

print("Trapézio Composto: intervalo 1", trapezios(f, a, b, intervalo_1))
print("Trapézio Composto: intervalo 5", trapezios(f, a, b, intervalo_2))
print("Trapézio Composto: intervalo 20", trapezios(f, a, b, intervalo_3))

print("Simpson Composto: intervalo 1", simpson_composto(f, a, b, intervalo_1))
print("Simpson Composto: intervalo 5", simpson_composto(f, a, b, intervalo_2))
print("Simpson Composto: intervalo 20", simpson_composto(f, a, b, intervalo_3))

"""
Resposta no terminal:

Trapézio Composto: 1.34376993948565
Trapézio Composto: 1.9220458129296027
Trapézio Composto: 1.9390076854864953

Simpson Composto: A quantidade de subintervalos deve ser par.
Simpson Composto: A quantidade de subintervalos deve ser par.
Simpson Composto: 1.9401319682083593

"""
