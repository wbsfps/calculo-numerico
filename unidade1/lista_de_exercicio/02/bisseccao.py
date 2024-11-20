# A resistividade  do silício dopado é baseada na carga q de um elétron, na densidade eletrônica
# n e na mobilidade do elétron μ. A densidade eletrônica é dada em termos da densidade da
# dopagem N e da densidade de transporte intrínseca ni. A mobilidade do elétron é descrita pela
# temperatura T, pela temperatura de referência T0 e pela mobilidade de referência μ0. As
# equações necessárias para o cálculo da resistividade são

#  p = 1 / (q * n * u)

# onde n

# determine N dados T0 = 300K, T = 1000K, u0 = 1360cm^2(V.s)^-1, q = 1.7 * 10^-19C, ni = 6.21 * 10^9 cm-3 e uma resistência desejada de p = 6.5 ** 10^6

import numpy as np
from matplotlib import pyplot as plt


def for_n(x):
    return (1/2) * (x + np.sqrt(x ** 2 + (4 * 6.21 * 10 ** 9)))


def for_u(x):
    return x * ((1000 / 300) ** -2.42)


def f(x):
    return 1 * ((1.7 * 10 ** -19) * for_n(x) * for_u(x))


def bissec(a, b, erro, it_max):
    it = 0
    x = 0

    Er = 1

    while (Er >= erro and it < it_max):
        xold = x
        x = (a + b) / 2
        Er = np.abs((x - xold) / x)

        if (f(a) * f(x) < 0):
            b = x
        else:
            a = x
        it += 1
    return (x, Er, it)


a = 3
b = 6

m = np.arange(a, b, 1)
plt.plot(m, f(m))
plt.show()

erro = 10**-5
it_max = 6

res = bissec(a, b, erro, 100)

print('O valor da raiz é ', res[0])
print("O erro relativo foi", res[1])
print("Número de iterações", res[2])
