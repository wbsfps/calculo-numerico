import math
import numpy as np
import matplotlib.pyplot as plt

# Função dada


def f(t):
    return 9 * math.exp(-t) * math.sin(2 * math.pi * t) - 3.5

# Derivada da função


def df(t):
    return -9 * math.exp(-t) * math.sin(2 * math.pi * t) + 18 * math.pi * math.exp(-t) * math.cos(2 * math.pi * t)

# Método da Bisseção


def bisection_method(f, a, b, tol=1e-5, max_iter=1000):
    if f(a) * f(b) >= 0:
        print("A função deve mudar de sinal em [a, b].")
        return None

    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

# Método de Newton


def newton_method(f, df, x0, tol=1e-5, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-10:
            print("Derivada próxima de zero, pode haver problemas.")
            return None
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new

    return x


# Definir intervalo e valor inicial
a = 0
b = 1
x0 = 0.5

# Encontrar raízes
root_bisection = bisection_method(f, a, b)
root_newton = newton_method(f, df, x0)

# Exibir resultados
if root_bisection is not None:
    print(f"Raiz encontrada pelo método da bisseção: {root_bisection:.5f}")
else:
    print("Método da bisseção não encontrou uma raiz.")

if root_newton is not None:
    print(f"Raiz encontrada pelo método de Newton: {root_newton:.5f}")
else:
    print("Método de Newton não encontrou uma raiz.")

# Gerar dados para o gráfico
t_values = np.linspace(0, 1, 400)
f_values = [f(t) for t in t_values]

# Plotar
plt.figure(figsize=(10, 6))
plt.plot(t_values, f_values, label='f(t) = 9*exp(-t)*sin(2*pi*t) - 3.5')
plt.axhline(0, color='black', linewidth=0.5)
if root_bisection is not None:
    plt.plot(root_bisection, f(root_bisection), 'ro',
             label=f'Raiz Bisseção: {root_bisection:.5f}')
if root_newton is not None:
    plt.plot(root_newton, f(root_newton), 'go',
             label=f'Raiz Newton: {root_newton:.5f}')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Gráfico da Função e Raízes Encontradas')
plt.legend()
plt.grid(True)
plt.show()
