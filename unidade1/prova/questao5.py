import math


def funcao(x):
    return 4 + x * math.cos(x)


def derivada(x):
    return - x * math.sin(x) + math.cos(x)


def newton(x, precisao):
    while abs(funcao(x)) >= precisao:
        x_novo = x - funcao(x) / derivada(x)
        if abs(x_novo - x) < precisao:
            break
        x = x_novo
    print(f'Raiz encontrada: {x};')


newton(8, 0.00001)  # Raiz encontrada: 8.35332687900836;
newton(10, 0.00001)  # Raiz encontrada: 10.608976824275029;
