import numpy as np


def gauss_jacobi(A, b, x0, tol=1e-10, max_iter=1000):
    n = len(b)
    x = x0.copy()
    for _ in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            sum_j = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_j) / A[i][i]

        # Verifica se a convergência foi atingida
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, _

        x = x_new
    raise ValueError(
        "O método não convergiu após o número máximo de iterações")


# Exemplo de uso
A = np.array([[4, 1, 2], [3, 5, 1], [1, 1, 3]], dtype=float)
b = np.array([4, 7, 3], dtype=float)
x0 = np.zeros_like(b)

sol, iters = gauss_jacobi(A, b, x0)
print(f'Solução encontrada: {sol} em {iters} iterações')
