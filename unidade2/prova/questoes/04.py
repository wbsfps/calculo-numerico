from itertools import permutations
import numpy as np


def is_diagonal_dominant(A):
    """Verifica se a matriz A é diagonal dominante."""
    for i in range(len(A)):
        row_sum = sum(abs(A[i][j]) for j in range(len(A)) if i != j)
        if abs(A[i][i]) <= row_sum:
            return False
    return True


def gauss_seidel(A, b, x0, precisao=1e-5, max_iter=1000):
    """Resolve o sistema linear Ax = b usando o método de Gauss-Seidel."""
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

    # Se não convergir, retorna uma mensagem
    raise ValueError(
        "O método não convergiu após o número máximo de iterações")


# Matriz e vetor do problema
A = np.array([
    [12, 3, -6],
    [7, -15, 4],
    [3, 8, 10]
], dtype=float)
b = np.array([16, 7, 25], dtype=float)
x0 = np.zeros_like(b)

try:
    # Verifica se a matriz é diagonal dominante
    if is_diagonal_dominant(A):
        print("A matriz é diagonal dominante. Procedendo com os métodos iterativos.\n")
    else:
        """
        Original
        [12, 3, -6],
        [3, 8, 10],
        [7, - 15, 4]

        Nova
        [12, 3, -6],
        [7, -15, 4],
        [3, 8, 10]
        """
        print(
            "A matriz não é diagonal dominante. Métodos iterativos podem não convergir. Invertendo a equação... \n")

    sol_seidel, iters_seidel = gauss_seidel(A, b, x0)
    print("Gauss-Seidel:")
    print(f"Solução encontrada: {sol_seidel}")
    print(f"Quantidade de iterações: {iters_seidel}")

except ValueError as e:
    print(e)


def is_diagonally_dominant(matrix):
    """Verifica se a matriz é diagonalmente dominante."""
    return all(
        abs(matrix[i, i]) > sum(abs(matrix[i, j])
                                for j in range(len(matrix)) if j != i)
        for i in range(len(matrix))
    )


# Sistema original
A = np.array([
    [12, 3, -6],
    [7, -15, 4],
    [3, 8, 10]
], dtype=float)
b = np.array([16, 7, 25], dtype=float)

# Tentando reorganizar para matriz diagonalmente dominante
row_indices = range(len(A))
best_A = None
best_b = None

for perm in permutations(row_indices):
    permuted_A = A[list(perm), :]
    permuted_b = b[list(perm)]
    if is_diagonally_dominant(permuted_A):
        best_A = permuted_A
        best_b = permuted_b
        break

if best_A is None:
    print("Não foi possível reorganizar para matriz diagonalmente dominante.")
    # Usar a matriz original, mesmo que não seja dominante.
    best_A, best_b = A, b

# Método de Gauss-Seidel
precision = 1e-10
max_iterations = 1000

x = np.zeros(len(best_b))  # Vetor inicial
previous_x = np.zeros(len(best_b))  # Para comparar iterações

for iteration in range(max_iterations):
    for i in range(len(best_A)):
        sum1 = sum(best_A[i, j] * x[j] for j in range(i))
        sum2 = sum(best_A[i, j] * previous_x[j]
                   for j in range(i + 1, len(best_A)))
        x[i] = (best_b[i] - sum1 - sum2) / best_A[i, i]

    # Critério de parada
    if np.linalg.norm(x - previous_x, ord=np.inf) < precision:
        print(f"Convergiu após {iteration + 1} iterações.")
        break

    previous_x = x.copy()

# Resultado final
print("Solução do sistema:")
print(x)
