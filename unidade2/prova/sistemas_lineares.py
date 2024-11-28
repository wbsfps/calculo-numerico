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


def gauss_jacobi(A, b, x0, precisao=1e-4, max_iter=1000):
    n = len(b)
    x = x0.copy()
    for iter_count in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            sum_j = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_j) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < precisao:
            return x_new, iter_count + 1
        x = x_new
    return None, max_iter


# Exemplo de uso
A = np.array([[3, - 0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]], dtype=float)
b = np.array([7.85, -19.3, 71.4], dtype=float)
x0 = np.zeros_like(b)

sol, iters = gauss_jacobi(A, b, x0)
print(f'Matriz jacobi: solução encontrada: {sol} em {iters} iterações')


sol, iters = gauss_seidel(A, b, x0)
print(f'Matriz seidel: solução encontrada: {sol} em {iters} iterações')
