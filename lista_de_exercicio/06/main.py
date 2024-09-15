import numpy as np
import matplotlib.pyplot as plt

# Definindo as constantes
v0 = 30  # Velocidade inicial (m/s)
g = 9.81  # Aceleração gravitacional (m/s^2)
x_total = 90  # Distância horizontal total (m)
y0 = 1.8  # Altura inicial (m)
y_final = 1  # Altura final (m)
precision = 1e-5  # Precisão para o método de Newton e bissecção

# Definindo a função para a equação da trajetória


def trajectory_eq(theta, x, v0, g, y0):
    return np.tan(theta) * x - (g / (2 * v0**2 * np.cos(theta)**2)) * x**2 + y0

# Definindo a função objetivo, queremos que f(theta) = y_final


def f(theta):
    return trajectory_eq(theta, x_total, v0, g, y0) - y_final

# Derivada da função (necessária para o método de Newton)


def df(theta):
    return (x_total / np.cos(theta)**2) - ((g * x_total**2) / (v0**2 * np.cos(theta)**3)) * np.sin(2 * theta)

# Método de Newton para encontrar o valor de theta


def newton_method(f, df, theta0, tol):
    theta = theta0
    while abs(f(theta)) > tol:
        theta = theta - f(theta) / df(theta)
    return theta

# Método da bissecção


def bisection_method(f, a, b, tol):
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2


# Aplicando o método de Newton e bissecção
theta_initial = np.radians(45)  # Chute inicial para o método de Newton
theta_newton = newton_method(f, df, theta_initial, precision)

# Usando a bissecção com um intervalo de [0, pi/2]
theta_bissection = bisection_method(f, 0, np.pi/2, precision)

# Gerando os dados da trajetória com o valor de theta encontrado
x_vals = np.linspace(0, x_total, 500)
y_vals_newton = trajectory_eq(theta_newton, x_vals, v0, g, y0)
y_vals_bissection = trajectory_eq(theta_bissection, x_vals, v0, g, y0)

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals_newton, label=f'Trajetória (Newton): θ = {
         np.degrees(theta_newton):.5f}°')
plt.plot(x_vals, y_vals_bissection, label=f'Trajetória (Bissecção): θ = {
         np.degrees(theta_bissection):.5f}°', linestyle='--')
plt.axhline(y=y_final, color='r', linestyle=':', label='Altura final (1 m)')
plt.axhline(y=y0, color='g', linestyle=':', label='Altura inicial (1.8 m)')
plt.axvline(x=x_total, color='b', linestyle=':', label='Distância (90 m)')
plt.xlabel('Distância horizontal (m)')
plt.ylabel('Altura (m)')
plt.title('Trajetória da Bola Lançada')
plt.legend()
plt.grid(True)
plt.show()

print(f'Valor em newton: {
      theta_newton} / Valor com bissecção {theta_bissection}')
