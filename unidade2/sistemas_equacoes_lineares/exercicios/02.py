import numpy as np

"""
Motores - 3x1 + 2x2 + 4x3  = 80
Lataria - 2x1 + 2x2 + 3x3 = 60
Acabamento - 3x1 + 3x2 + 5x3 = 95
"""


# def gauss_jacobi_equations(equations, x0, precisao=1e-4, max_iter=1000):
#     n = len(equations)
#     x = x0.copy()
#     for _ in range(max_iter):
#         x_new = x.copy()
#         for i in range(n):
#             left_side, right_side = equations[i](x)
#             x_new[i] = right_side / left_side

#         # Verifica se a convergência foi atingida
#         if max(abs(x_new[i] - x[i]) for i in range(n)) < precisao:
#             return x_new, _

#         x = x_new

#     raise ValueError(
#         "O método não convergiu após o número máximo de iterações")

# # Definindo as equações diretamente


# def equation1(x): return 3, 80 - 2 * x[1] - 4 * x[2]
# def equation2(x): return 2, 60 - 2 * x[0] - 3 * x[2]
# def equation3(x): return 5, 95 - 3 * x[0] - 3 * x[1]


# equations = [equation1, equation2, equation3]
# x0 = [2, 2, 2]  # Aproximação inicial

# sol, iters = gauss_jacobi_equations(equations, x0)
# sol_mensal = [s * 4 for s in sol]

# print(f"Solução encontrada (semanal): {sol}")
# print(f"Número de iterações: {iters}")
# print(f"Solução mensal: {sol_mensal}")


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


# Exemplo de uso
A = np.array([[3, 2, 4], [2, 2, 3], [3, 3, 5]], dtype=float)
b = np.array([80, 60, 95], dtype=float)
x0 = np.zeros_like(b)

sol, iters = gauss_jacobi(A, b, x0)
sol_mensal = [s * 4 for s in sol]

print(f"Solução encontrada (semanal): {sol}")
print(f"Número de iterações: {iters}")
print(f"Solução mensal: {sol_mensal}")
