import matplotlib.pyplot as plt

P = 35000  # Valor do veículo
A = 8500   # Pagamento anual
n = 7      # Número de anos


def f(i):
    return P * (i * (1 + i)**n) / ((1 + i)**n - 1) - A


def f_prime(i):
    term1 = P * (n * (1 + i)**(n - 1) * i + (1 + i)**n) / ((1 + i)**n - 1)
    term2 = P * (i * (1 + i)**n) * n * (1 + i)**(n - 1) / ((1 + i)**n - 1)**2
    return term1 - term2


def newton_raphson(i_init, tol=1e-6, max_iter=1000):
    i = i_init
    iterations = []
    for _ in range(max_iter):
        f_val = f(i)
        f_prime_val = f_prime(i)
        iterations.append(i)
        if abs(f_val) < tol:
            break
        i = i - f_val / f_prime_val
    return i, iterations


def bissecao(i_low, i_high, tol=1e-6, max_iter=1000):
    iterations = []
    for _ in range(max_iter):
        i_mid = (i_low + i_high) / 2
        f_low = f(i_low)
        f_mid = f(i_mid)
        iterations.append(i_mid)

        if abs(f_mid) < tol:
            break

        if f_low * f_mid < 0:
            i_high = i_mid
        else:
            i_low = i_mid
    return i_mid, iterations


i_init = 0.1
i_low = 0.01
i_high = 0.2
tolerance = 1e-5

i_newton, newton_iterations = newton_raphson(i_init, tol=tolerance)
print(f"Taxa de juros encontrada pelo método de Newton: {i_newton * 100:.6f}%")

i_bissecao, bissecao_iterations = bissecao(i_low, i_high, tol=tolerance)
print(f"Taxa de juros encontrada pelo método da Bisseção: {
      i_bissecao * 100:.6f}%")


plt.figure(figsize=(10, 6))


plt.plot(newton_iterations, label='Newton-Raphson', marker='o')
plt.title('Convergência dos Métodos: Newton-Raphson e Bisseção')
plt.xlabel('Iteração')
plt.ylabel('Taxa de Juros (i)')
plt.grid(True)


plt.plot(bissecao_iterations, label='Bisseção', marker='x')

plt.legend()
plt.show()
