import math

PRECISAO = 0.00001


def f(x) -> float:
    return math.sin(10 * x) + math.cos(3 * x)


def bisseccao(f, a, b, precisao):

    if f(a) * f(b) >= 0:
        print("Não é possível ter raíz nesse intervalo informado")
        return a, b

    while abs(f(((a + b) / 2))) > precisao:
        m = (a + b) / 2
        if (f(a) * f(m)) < 0:
            b = m
            print(a, b)
        else:
            a = m
            print(a, b)

    return (a + b) / 2


raiz = bisseccao(f, 3, 6, PRECISAO)

print(f"A raíz é igual a {raiz:.5f}")
