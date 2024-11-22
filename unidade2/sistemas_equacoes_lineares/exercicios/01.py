"""
Mão de obra - 3x1 + 4x2 + 7x3 + 20x4 = 504kg
Metal - 20x1 + 25x2 + 40x3 + 50x4 = 1970kg
Plástico - 10x1 + 15x2 + 20x3 + 22x4 = 970kg
Componnetes = 10x1 + 8x2 + 10x3 + 15x4 = 601kg
"""
import numpy as np


def gauss_jacobi(A, b, x0, precisao=1e-4, max_iter=1000):
    n = len(b)
    x = x0.copy()
    for _ in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            sum_j = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_j) / A[i][i]

        # Verifica se a convergência foi atingida
        if np.linalg.norm(x_new - x, ord=np.inf) < precisao:
            return x_new, _

        x = x_new
    raise ValueError(
        "O método não convergiu após o número máximo de iterações")


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
A = np.array([[3, 4, 7, 20], [20, 25, 40, 50], [
             10, 15, 20, 22], [10, 8, 10, 15]], dtype=float)
b = np.array([504, 1970, 970, 601], dtype=float)
x0 = np.zeros_like(b)

sol, iters = gauss_seidel(A, b, x0)
print(f'Matriz seidel: solução encontrada: {sol} em {iters} iterações')

sol, iters = gauss_jacobi(A, b, x0)
print(f'Matriz jacobi: solução encontrada: {sol} em {iters} iterações')
"""
ValueError: O método não convergiu após o número máximo de iterações
"""
