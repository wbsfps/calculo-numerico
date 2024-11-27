# Alunos: William Batista

import math


def f(x):
    return (math.exp(x) * math.sin(x)) / (1 + x ** 2)


def trapezio_simples(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2


def trapezio_composto(f, a, b, n):
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n):
        soma += 2 * f(a + i * h)
    return (h / 2) * soma


def simpson_simples(f, a, b):
    m = (a + b) / 2
    return (b - a) / 6 * (f(a) + 4 * f(m) + f(b))

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

print("Trapézio Simples: ->", trapezio_simples(f, a, b))
print("Trapézio Composto: intervalo 1 ->",
      trapezio_composto(f, a, b, intervalo_1))
print("Trapézio Composto: intervalo 5 ->",
      trapezio_composto(f, a, b, intervalo_2))
print("Trapézio Composto: intervalo 20 ->",
      trapezio_composto(f, a, b, intervalo_3))

print()
print("Simpson Simples: ->", simpson_simples(f, a, b))
print("Simpson Composto: intervalo 1 ->",
      simpson_composto(f, a, b, intervalo_1))
print("Simpson Composto: intervalo 5 ->",
      simpson_composto(f, a, b, intervalo_2))
print("Simpson Composto: intervalo 20 ->",
      simpson_composto(f, a, b, intervalo_3))

"""
Resposta no terminal:

Trapézio Simples: -> 1.34376993948565
Trapézio Composto: intervalo 1 -> 1.34376993948565
Trapézio Composto: intervalo 5 -> 1.9220458129296027
Trapézio Composto: intervalo 20 -> 1.9390076854864953

Simpson Simples: -> 1.9728268379477782
Simpson Composto: intervalo 1 -> A quantidade de subintervalos deve ser par.
Simpson Composto: intervalo 5 -> A quantidade de subintervalos deve ser par.
Simpson Composto: intervalo 20 -> 1.9401319682083593

"""
