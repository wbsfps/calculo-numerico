import math


def funcao(t):
    return (9 * math.e**-t) * (math.sin(2 * math.pi * t)) - 3.5


def derivada(t):
    return 9*(6.2318*math.e**-t * math.cos(6.2318*t) - math.e**-t * math.sin(6.2318*t))


def bisseccao(xa, xb, precisao):
    if not (funcao(xa) * funcao(xb) < 0):
        xa = float(input('Digite um novo valor para Xa: '))
        xb = float(input('Digite um novo valor para Xb: '))

    while abs(xb - xa) >= precisao:
        xm = (xa + xb) / 2
        if abs(funcao(xm)) < precisao:
            return print(f'{xm} = raiz')
        if funcao(xa) * funcao(xm) < 0:
            xb = xm
        else:
            xa = xm
    return print(f'Raiz encontrada: {xm}')


def newton(x, precisao):
    while abs(funcao(x)) >= precisao:
        x_novo = x - funcao(x) / derivada(x)
        if abs(x_novo - x) < precisao:
            break
        x = x_novo
    print(f'Raiz encontrada: {x}')


bisseccao(xa=0.01, xb=0.5, precisao=0.00001)
newton(0.1, 0.00001)
