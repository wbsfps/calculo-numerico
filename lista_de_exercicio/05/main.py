
import math

#  math.log == ln
#  math.log10 == log


def funcao(t):
    return 9 * (math.e * - t) * math.sin(2 * math.pi * t) - 3.5


def derivada(t):
    return (23400 / (-13 * t + 800)) - 9.81


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


def newton(x, precisao):
    while abs(funcao(x)) >= precisao:
        x_novo = x - funcao(x) / derivada(x)
        if abs(x_novo - x) < precisao:
            break
        x = x_novo
    print(f'Raiz encontrada: {x};')


def secante(x0, x1, precisao):
    while abs(funcao(x1)) >= precisao:
        x_novo = x1 - funcao(x1) * (x1 - x0) / (funcao(x1) - funcao(x0))
        if abs(x_novo - x1) < precisao:
            break
        x0, x1 = x1, x_novo
    print(f'Raiz encontrada: {x_novo};')


bisseccao(20, 30, 10e-10)
newton(25, 10e-10)
secante(20, 30, 10e-10)
# Alunos: William Batista e João Alfredo
