import numpy as np


def is_diagonal_dominant(A):
    """Verifica se a matriz A é diagonal dominante."""
    for i in range(len(A)):
        row_sum = sum(abs(A[i][j]) for j in range(len(A)) if i != j)
        if abs(A[i][i]) <= row_sum:
            return False
    return True


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


def gauss_seidel(A, b, x0, precisao=1e-4, max_iter=1000):
    n = len(b)
    x = x0.copy()
    for iter_count in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum_j = sum(A[i][j] * x_new[j] for j in range(i)) + \
                sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum_j) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < precisao:
            return x_new, iter_count + 1
        x = x_new
    return None, max_iter


# Matriz e vetor do problema
A = np.array([
    [3, 4, 7, 20],
    [20, 25, 40, 50],
    [10, 15, 20, 22],
    [10, 8, 10, 15]
], dtype=float)

b = np.array([504, 1970, 970, 601], dtype=float)
x0 = np.zeros_like(b)

# Verifica se a matriz é diagonal dominante
if is_diagonal_dominant(A):
    print("A matriz é diagonal dominante. Procedendo com os métodos iterativos.\n")

    sol_seidel, iters_seidel = gauss_seidel(A, b, x0)
    print("Gauss-Seidel:")
    print(f"Solução encontrada: {sol_seidel}")
    print(f"Número de iterações: {iters_seidel}")

    sol_jacobi, iters_jacobi = gauss_jacobi(A, b, x0)
    print("\nGauss-Jacobi:")
    print(f"Solução encontrada: {sol_jacobi}")
    print(f"Número de iterações: {iters_jacobi}")
else:
    print("A matriz não é diagonal dominante. Métodos iterativos podem não convergir.\n")
