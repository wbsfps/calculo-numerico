import math

R = 3  # valor do raio
V = 30  # valor do de armazenamento no tanque


def funcao(h):
    return math.pi * h**2 * ((3 * 3 - h) / 3) - 30


def derivada(h):
    return math.pi * h * (- h + 2*R)


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


bisseccao(xa=0.01, xb=0.2, precisao=0.00001)
newton(0.1, 0.00001)
