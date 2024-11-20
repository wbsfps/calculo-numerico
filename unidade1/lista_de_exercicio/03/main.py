import math

CP = 1.1  # Calor específico kJ/ (Kg.K)


def funcao(t):
    return (0.99403) + (1.671e-4 * t) + (9.7215e-8 * (t ** 2)) - (9.5838e-11 * (t ** 3)) + (1.9520e-14 * (t ** 4))


def derivada(t):
    return - ((5 * (2 * (h ** 2)) - (12 * h) + 9) / (math.sqrt((-h**2) + (6**h)))) - 3 * math.cos(1)


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


def secante(x0, x1, precisao):
    while abs(funcao(x1)) >= precisao:
        x_novo = x1 - funcao(x1) * (x1 - x0) / (funcao(x1) - funcao(x0))
        if abs(x_novo - x1) < precisao:
            break
        x0, x1 = x1, x_novo
    print(f'Raiz encontrada: {x_novo}')


bisseccao(xa=0.01, xb=0.2, precisao=0.00001)
newton(0.1, 0.00001)
secante(0.1, 0.2, 0.00001)
