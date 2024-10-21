import numpy as np


def gauss_jacobi(A, b, x0, tol=1e-4, max_iter=1000):
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
A = np.array([[3, - 0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]], dtype=float)
b = np.array([7.85, -19.3, 71.4], dtype=float)
x0 = np.zeros_like(b)

sol, iters = gauss_jacobi(A, b, x0)
print(f'Solução encontrada: {sol} em {iters} iterações')  # 4 iterações
