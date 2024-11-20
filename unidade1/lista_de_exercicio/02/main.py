import numpy as np
import matplotlib.pyplot as plt

# Definindo as constantes fornecidas
q = 1.7e-19  # Carga do elétron em coulombs
ni = 6.21e9  # Densidade intrínseca em cm^-3
T0 = 300  # Temperatura de referência em K
T = 1000  # Temperatura em K
mu0 = 1360  # Mobilidade de referência em cm^2/Vs
rho_desejada = 6.5e6  # Resistividade desejada em Ohm.cm

# Função para calcular n(N)


def calc_n(N, ni):
    return 0.5 * (N + np.sqrt(N**2 + 4 * ni**2))

# Função para calcular a mobilidade mu(T)


def calc_mu(T, T0, mu0):
    return mu0 * (T / T0) ** -2.42

# Função de resistividade rho(N) - Reescrevendo o problema em termos de N


def calc_resistividade(N, T, T0, mu0, q, ni):
    n = calc_n(N, ni)
    mu = calc_mu(T, T0, mu0)
    return 1 / (q * n * mu)

# Definindo a função f(N) = resistividade(N) - resistividade desejada


def f(N):
    return calc_resistividade(N, T, T0, mu0, q, ni) - rho_desejada

# Derivada da função f(N) para o método de Newton


def df(N, T, T0, mu0, q, ni):
    n = calc_n(N, ni)
    # Derivada de n em relação a N
    dn_dN = 0.5 * (1 + N / np.sqrt(N**2 + 4 * ni**2))
    mu = calc_mu(T, T0, mu0)
    d_rho_dN = -(1 / (q * mu * n**2)) * dn_dN  # Derivada de rho em relação a N
    return d_rho_dN

# Implementando o método da bisseção


def bissecao(f, a, b, tol):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError(
            "A função não muda de sinal no intervalo dado. Tente outro intervalo.")

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)

        if fc == 0:
            return c  # Achou a raiz exata
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2

# Implementando o método de Newton


def newton(f, df, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x, T, T0, mu0, q, ni)
        if dfx == 0:
            raise ValueError(
                "Derivada é zero, não é possível continuar com o método de Newton.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError(
        "Número máximo de iterações excedido no método de Newton.")


# Gerando o gráfico da função f(N)
N_values = np.linspace(1e15, 1e18, 500)
f_values = [f(N) for N in N_values]

plt.figure(figsize=(10, 6))
plt.plot(N_values, f_values,
         label='f(N) = Resistividade(N) - Resistividade Desejada', color='b')
plt.axhline(0, color='r', linestyle='--')
plt.xlabel('N (cm^-3)')
plt.ylabel('f(N)')
plt.title('Gráfico da função f(N)')
plt.grid(True)
plt.legend()
plt.show()

# Intervalo inicial para o método da bisseção
a = 1e15
b = 1e18
tol = 1e-5

# Aplicando o método da bisseção para encontrar N
N_bissecao = bissecao(f, a, b, tol)
print(f'O valor de N encontrado pelo método da bisseção é: {N_bissecao}')

# Parâmetros para o método de Newton
x0 = 1e16
max_iter = 100

# Aplicando o método de Newton para encontrar N
N_newton = newton(f, df, x0, tol, max_iter)
print(f'O valor de N encontrado pelo método de Newton é: {N_newton}')
