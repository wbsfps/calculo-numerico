
import numpy as np
import matplotlib.pyplot as plt

# Definindo o intervalo para o método da bissecção e o chute inicial para Newton
a, b = 0.1, 1.0  # Intervalo de busca (aproximado)
t_newton_start = 0.5  # Chute inicial para o método de Newton

# Resolução com precisão 10^-5
precision = 1e-5


def f(t):
    return 9 * np.exp(-t) * np.sin(2 * np.pi * t) - 3.5

# Derivada da função para o método de Newton


def df(t):
    return -9 * np.exp(-t) * np.sin(2 * np.pi * t) + 9 * np.exp(-t) * 2 * np.pi * np.cos(2 * np.pi * t)


def newton_method(f, df, x0, tol=1e-5, max_iter=1000):
    xn = x0
    for _ in range(max_iter):
        fxn = f(xn)
        if abs(fxn) < tol:
            return xn
        dfxn = df(xn)
        if dfxn == 0:
            raise ValueError('Derivada zero, sem solução encontrada.')
        xn = xn - fxn / dfxn
    raise ValueError('Número máximo de iterações alcançado.')


def bisection_method(f, a, b, tol=1e-5, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError('f(a) e f(b) devem ter sinais opostos')

    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol or (b - a) / 2 < tol:
            return c
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    raise ValueError('Número máximo de iterações alcançado.')


# Utilizando os métodos implementados
t_newton_start = 0.5  # Chute inicial para o método de Newton
a, b = 0.1, 1.0       # Intervalo de busca para o método da bissecção

# Encontrando as raízes
root_newton_manual = newton_method(f, df, t_newton_start, tol=precision)
root_bisect_manual = bisection_method(f, a, b, tol=precision)

t_vals = np.linspace(0, 2, 400)
I_vals = 9 * np.exp(-t_vals) * np.sin(2 * np.pi * t_vals)

plt.figure(figsize=(8, 6))
plt.plot(t_vals, I_vals, label=r'$9e^{-t} \sin(2\pi t)$')
plt.axhline(3.5, color='red', linestyle='--', label=r'$I = 3.5$')
plt.scatter([root_bisect_manual, root_newton_manual], [3.5, 3.5],
            color='green', zorder=5, label='Raízes encontradas manualmente')
plt.xlabel('t (segundos)')
plt.ylabel('I (corrente)')
plt.title('Corrente em função do tempo - Solução Manual')
plt.legend()
plt.grid(True)

# Mostrando o gráfico
plt.show()

print(f'Valor em newton: {
      root_newton_manual} / Valor com bissecção {root_bisect_manual}')
