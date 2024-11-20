import math
import numpy as np
from scipy.integrate import simpson, trapezoid
# Função para a velocidade v(t)


def f(z, h=30):
    return 200 * (z / (5 + z)) * math.exp((-2 * z) / h)
# Método dos Trapézios


def trapezios(f, a, b, n):
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n):
        soma += 2 * f(a + i * h)
    return (h / 2) * soma

# Método de Simpson (1/3)


def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("O número de subintervalos n deve ser par.")
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)
    for i in range(2, n, 2):
        soma += 2 * f(a + i * h)
    return (h / 3) * soma


a = 0
b = 30
subintervalos = [10, 100]

print("Cálculo da força: \n")
for valor in subintervalos:
    forca_trapezios = trapezios(f, a, b, valor)
    forca_simpson = simpson(f, a, b, valor)
    print(f"Subintervalos: {valor}")
    print(f"Método dos Trapézios: {forca_trapezios:.6f} N")
    print(f"Método de Simpson: {forca_simpson:.6f} N\n")


H = 30  # Altura do mastro em metros

# Função da força


def forca(z, H):
    return 200 * (z / (5 + z)) * np.exp(-2 * z / H)


# Discretização para os métodos
n_values_q2 = [10, 100]  # Número de subintervalos para questão 2
z_values_q2 = [np.linspace(0, H, n+1)
               for n in n_values_q2]  # Valores de z (intervalos)
f_values_q2 = [forca(z, H) for z in z_values_q2]  # Valores da função força

# Cálculos da questão 2
resultados_q2 = {
    "Trapézios": [trapezoid(f, z) for f, z in zip(f_values_q2, z_values_q2)],
    # Adicionar x=z
    "Simpson": [simpson(f, x=z) for f, z in zip(f_values_q2, z_values_q2)],
}

# Resultados
print("\nQuestão 2: Força total no mastro do veleiro")
print(f"Trapézios (n=10): {resultados_q2['Trapézios'][0]:.2f} N")
print(f"Trapézios (n=100): {resultados_q2['Trapézios'][1]:.2f} N")
print(f"Simpson (n=10): {resultados_q2['Simpson'][0]:.2f} N")
print(f"Simpson (n=100): {resultados_q2['Simpson'][1]:.2f} N")
