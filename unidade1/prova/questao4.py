
import math


def funcao(c):
    return 9.8 * 110 * (1 - (math.e ** - 7 * (c / 110))) / (c) - 40


def bisseccao(xa, xb, precisao):
    if funcao(xa) * funcao(xb) > 0:
        print(
            'Não tem como garantir que tem raiz.')

    while abs(xb - xa) >= precisao:
        xm = (xa + xb) / 2
        if abs(funcao(xm)) < precisao:
            return print(f'Raiz = {xm};')
        if funcao(xa) * funcao(xm) < 0:
            xb = xm
        else:
            xa = xm
    return print(f'Raiz encontrada: {xm};')


bisseccao(15, 18.807, 0.000001)  # Raiz encontrada: 18.80699909234047;
