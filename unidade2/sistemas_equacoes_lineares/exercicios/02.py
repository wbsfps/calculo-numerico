import numpy as np


def gauss_seidel(A, b, x0, precisao=1e-4, max_iter=1000):
    n = len(b)
    x = x0.copy()
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum_j = sum(A[i][j] * x_new[j] for j in range(i)) + \
                sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum_j) / A[i][i]

        # Verifica se a convergência foi atingida
        if np.linalg.norm(x_new - x, ord=np.inf) < precisao:
            return x_new, _

        x = x_new
    raise ValueError(
        "O método não convergiu após o número máximo de iterações")


# Exemplo de uso
A = np.array([[3, 2, 4], [2, 2, 3], [3, 3, 5]], dtype=float)
b = np.array([320, 240, 380], dtype=float)
x0 = np.zeros_like(b)

sol, iters = gauss_seidel(A, b, x0)
print(f'Solução encontrada: {sol} em {iters} iterações')
# Solução encontrada: [40.00081961 20.00061471 39.99913941] em 101 iterações
