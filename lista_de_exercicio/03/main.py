import numpy as np
import matplotlib.pyplot as plt

# Definindo a função e sua derivada


def Cp(T):
    return 0.99403 + 1.671e-4*T + 9.7215e-8*T**2 - 9.5838e-11*T**3 + 1.9520e-14*T**4


def dCp_dT(T):
    return 1.671e-4 + 1.9443e-7*T - 2.8751e-10*T**2 + 7.808e-14*T**3

# Método de Newton


def newton(f, df, x0, tol):
    x = x0
    while abs(f(x)) > tol:
        x = x - f(x)/df(x)
    return x

# Método da Bissecção


def bissecao(f, a, b, tol):
    while abs(b-a) > tol:
        c = (a+b)/2
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return (a+b)/2


# Valores iniciais e precisão
x0 = 1000  # Chute inicial para o método de Newton
a = 0
b = 1200
tol = 1e-5

# Encontrando a raiz
raiz_newton = newton(lambda T: Cp(T)-1.1, dCp_dT, x0, tol)
raiz_bissecao = bissecao(lambda T: Cp(T)-1.1, a, b, tol)

# Plotando o gráfico
T = np.linspace(0, 1200, 1000)
plt.plot(T, Cp(T))
plt.xlabel('Temperatura (K)')
plt.ylabel('Calor Específico (kJ/kg.K)')
plt.title('Calor Específico do Ar Seco')
plt.grid(True)
plt.show()

print("Raiz encontrada pelo método de Newton:", raiz_newton)
print("Raiz encontrada pelo método da Bissecao:", raiz_bissecao)
