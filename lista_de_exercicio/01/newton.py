# Você comprou um veículo de R$ 35.000,00 sem entrada e pagando R$ 8.500,00 por ano por
# 7 anos. Determine a taxa de juros que você está pagando. A equação que relaciona o valor do
# veículo P, os pagamentos anuais A, o número de anos n e a taxa de juros i, é:

# A = P * (i * (1 + i)^n)/ (((1 + i)^n) - 1)


import matplotlib.pyplot as plt

P = 35000
A = 8500
n = 7


def f(i):
    return P * (i * (1 + i)**n) / ((1 + i)**n - 1) - A


def f_prime(i):
    term1 = P * (n * (1 + i)**(n - 1) * i + (1 + i)**n) / ((1 + i)**n - 1)
    term2 = P * (i * (1 + i)**n) * n * (1 + i)**(n - 1) / ((1 + i)**n - 1)**2
    return term1 - term2


def newton_raphson(i_init, tol=1e-6, max_iter=1000):
    i = i_init
    for _ in range(max_iter):
        f_val = f(i)
        f_prime_val = f_prime(i)
        if abs(f_val) < tol:
            return i
        i = i - f_val / f_prime_val
    return i


i_init = 0.1  # Chute inicial para o método de Newton

i_newton, newton_iterations = newton_raphson(i_init)
print(f"Taxa de juros encontrada pelo método de Newton: {i_newton * 100:.6f}%")

plt.figure(figsize=(10, 6))

# Gráfico do Método de Newton-Raphson
plt.plot(newton_iterations, label='Newton-Raphson', marker='o')
