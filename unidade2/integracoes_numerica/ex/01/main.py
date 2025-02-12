import math
import numpy as np
from scipy.integrate import simpson, trapezoid

# Função para a velocidade v(t)


def v(t, g=9.81, m=68.1, cd=0.25):
    return math.sqrt(g * m / cd) * math.tanh(math.sqrt(g * cd / m) * t)

# Método dos Trapézios


def trapezios(f, a, b, n):
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n):
        soma += 2 * f(a + i * h)
    return (h / 2) * soma

# Método de Simpson (1/3)


def simpson_(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("O número de subintervalos n deve ser par.")
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)
    for i in range(2, n, 2):
        soma += 2 * f(a + i * h)
    return (h / 3) * soma


# Parâmetros
a = 0  # Tempo inicial
b = 10  # Tempo final
subintervalos = [2, 10]  # Subintervalos para comparação

# Calculando a distância
print("Cálculo da distância percorrida pelo objeto:\n")
for n in subintervalos:
    distancia_trapezios = trapezios(v, a, b, n)
    distancia_simpson = simpson_(v, a, b, n)
    print(f"Subintervalos: {n}")
    print(f"Método dos Trapézios: {distancia_trapezios:.6f} m")
    print(f"Método de Simpson: {distancia_simpson:.6f} m\n")


# Dados da questão 1
g = 9.81  # m/s²
m = 68.1  # kg
cd = 0.25  # kg/m
t_final = 10  # segundos

# Função da velocidade


def velocidade(t):
    fator = np.sqrt(g * m / cd)
    return fator * np.tanh(np.sqrt(g * cd / m) * t)


# Discretização para os métodos
valores_do_subintervalo = [2, 10]
valores_do_tempo = [np.linspace(0, t_final, n+1)
                    for n in valores_do_subintervalo]
valores_da_velocidade = [velocidade(t) for t in valores_do_tempo]

# Cálculos da questão 1
resultados_q1 = {
    "Trapézios": [trapezoid(v, t) for v, t in zip(valores_da_velocidade, valores_do_tempo)],
    # x especificado corretamente
    "Simpson": [simpson(v, x=t) for v, t in zip(valores_da_velocidade, valores_do_tempo)],
}

# Resultados
print("Questão 1: Distância percorrida pelo objeto em queda livre")
print(f"Trapézios (n=2): {resultados_q1['Trapézios'][0]:.4f} m")
print(f"Trapézios (n=10): {resultados_q1['Trapézios'][1]:.4f} m")
print(f"Simpson (n=2): {resultados_q1['Simpson'][0]:.4f} m")
print(f"Simpson (n=10): {resultados_q1['Simpson'][1]:.4f} m")
