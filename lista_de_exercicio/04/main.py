import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, bisect

# Dados fornecidos
r = 2  # raio em metros
L = 5  # comprimento em metros
V_given = 8  # volume em metros cúbicos

# Definir a função volume V(h) - o volume da equação fornecida


def volume_function(h, r, L):
    term1 = r**2 * np.arccos((r - h) / r)
    term2 = (r - h) * np.sqrt(2 * r * h - h**2)
    return (term1 - term2) * L

# Função objetivo para resolver V(h) = 8


def objective_function(h, r, L, V_given):
    return volume_function(h, r, L) - V_given


# Intervalo inicial para a bisseção [h_min, h_max] e precisão
h_min, h_max = 0, 2  # o valor de h varia entre 0 e o raio r
tolerance = 1e-5

# Resolução usando o método da bisseção
h_bissection = bisect(objective_function, h_min, h_max,
                      args=(r, L, V_given), xtol=tolerance)

# Resolução usando o método de Newton (precisamos fornecer um valor inicial)
h_newton = newton(objective_function, x0=1.5,
                  args=(r, L, V_given), tol=tolerance)

# Gerar gráfico da função volume em relação a h
h_values = np.linspace(0, 2, 500)
V_values = volume_function(h_values, r, L)

# Plotando a função Volume em função de h
plt.figure(figsize=(8, 6))
plt.plot(h_values, V_values, label='V(h)')
plt.axhline(y=V_given, color='red', linestyle='--', label=f'V = {V_given} m³')
plt.axvline(x=h_bissection, color='green', linestyle='--',
            label=f'h (bisseção) = {h_bissection:.5f} m')
plt.axvline(x=h_newton, color='orange', linestyle='--',
            label=f'h (Newton) = {h_newton:.5f} m')
plt.xlabel('Altura h (m)')
plt.ylabel('Volume V (m³)')
plt.title('Volume em função da altura h no cilindro')
plt.legend()
plt.grid(True)
plt.show()

# Resultados das alturas calculadas
print(f"Altura obtida (Método da bisseção): {h_bissection:.5f} m")
print(f"Altura obtida (Método de Newton): {h_newton:.5f} m")
