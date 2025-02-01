import numpy as np


def is_diagonal_dominant(A):
    """Verifica se a matriz A é diagonal dominante."""
    for i in range(len(A)):
        row_sum = sum(abs(A[i][j]) for j in range(len(A)) if i != j)
        if abs(A[i][i]) <= row_sum:
            return False
    return True


def make_diagonal_dominant(A, b):
    """Tenta reorganizar as linhas de A e b para torná-la diagonal dominante."""
    n = len(A)
    for i in range(n):
        row_sum = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) <= row_sum:
            # Tenta buscar uma linha j abaixo de i que seja mais dominante
            for j in range(i + 1, n):
                row_sum_j = sum(abs(A[j][k]) for k in range(n) if k != j)
                if abs(A[j][j]) > row_sum_j:
                    # Troca as linhas i e j em A e b
                    A[[i, j], :] = A[[j, i], :]
                    b[[i, j]] = b[[j, i]]
                    break
    return A, b


def gauss_seidel(A, b, x0, precisao=1e-10, max_iter=1000):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum_j = sum(A[i][j] * x_new[j] for j in range(i)) + \
                sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum_j) / A[i][i]

        # Verifica se a convergência foi atingida
        if np.linalg.norm(x_new - x, ord=np.inf) < precisao:
            return x_new, k + 1

        x = x_new
    raise ValueError(
        "O método não convergiu após o número máximo de iterações")


# Matriz e vetor do problema
A = np.array([
    [80, 0, 30, 10],
    [0, 80, 10, 10],
    [16, 20, 60, 72],
    [4, 0, 0, 8]
], dtype=float)
b = np.array([450, 325, 640, 565], dtype=float)
x0 = np.zeros_like(b)

# Reorganiza A e b para tentar torná-los diagonal dominante
A, b = make_diagonal_dominant(A, b)

# Verifica se a matriz é diagonal dominante após a reorganização
if is_diagonal_dominant(A):
    print("A matriz é diagonal dominante. Procedendo com os métodos iterativos.\n")

    sol_seidel, iters_seidel = gauss_seidel(A, b, x0)
    print("Gauss-Seidel:")
    print(f"Solução encontrada: {sol_seidel}")
    print(f"Número de iterações: {iters_seidel}")
else:
    print("A matriz não é diagonal dominante. Métodos iterativos podem não convergir.\n")
