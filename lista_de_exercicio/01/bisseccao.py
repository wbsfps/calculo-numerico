# Você comprou um veículo de R$ 35.000,00 sem entrada e pagando R$ 8.500,00 por ano por
# 7 anos. Determine a taxa de juros que você está pagando. A equação que relaciona o valor do
# veículo P, os pagamentos anuais A, o número de anos n e a taxa de juros i, é:

# A = P * (i * (1 + i)^n)/ (((1 + i)^n) - 1)


import numpy as np
from matplotlib import pyplot as plt


import math

# Definindo as variáveis fornecidas
P = 35000  # Valor do veículo
A = 8500   # Pagamento anual
n = 7      # Número de anos


def f(i):
    return P * (i * (1 + i)**n) / ((1 + i)**n - 1) - A


def bissecao(i_low, i_high, tol=1e-6, max_iter=1000):
    for _ in range(max_iter):
        i_mid = (i_low + i_high) / 2
        f_low = f(i_low)
        f_mid = f(i_mid)

        if abs(f_mid) < tol:
            return i_mid

        if f_low * f_mid < 0:
            i_high = i_mid
        else:
            i_low = i_mid
    return i_mid


i_init = 0.1  # Chute inicial para o método de Newton
i_low = 0.01  # Limite inferior para a bisseção
i_high = 0.2  # Limite superior para a bisseção

i_bissecao = bissecao(i_low, i_high)
print(f"Taxa de juros encontrada pelo método da Bisseção: {
      i_bissecao * 100:.6f}%")
