from math import sqrt, tanh


def v(t, g=9.81, m=6.81, cd=0.25):
    return sqrt(g * m / cd) * tanh(sqrt(g * cd / m) * t)


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
intervalo_1 = 2
intervalo_2 = 10

print("Trapézio Simples: ->", trapezio_simples(v, a, b))
print("Trapézio Composto: intervalo 1 ->",
      trapezio_composto(v, a, b, intervalo_1))
print("Trapézio Composto: intervalo 5 ->",
      trapezio_composto(v, a, b, intervalo_2))

print("Simpson Simples: ->", simpson_simples(v, a, b))
print("Simpson Composto: intervalo 2 ->",
      simpson_composto(v, a, b, intervalo_1))
print("Simpson Composto: intervalo 20 ->",
      simpson_composto(v, a, b, intervalo_2))
