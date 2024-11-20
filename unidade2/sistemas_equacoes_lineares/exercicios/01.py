"""
Mão de obra - 3x1 + 4x2 + 7x3 + 20x4 = 504kg
Metal - 20x1 + 25x2 + 40x3 + 50x4 = 1970kg
Plástico - 10x1 + 15x2 + 20x3 + 22x4 = 970kg
Componnetes = 10x1 + 8x2 + 10x3 + 15x4 = 601kg
"""


def gauss_seidel_equations(equations, x0, precisao=1e-1, max_iter=10000000):
    n = len(equations)
    x = x0.copy()
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            left_side, right_side = equations[i](x_new)
            x_new[i] = right_side / left_side

        # Verifica se a convergência foi atingida
        if max(abs(x_new[i] - x[i]) for i in range(n)) < precisao:
            return x_new, _

        x = x_new

    raise ValueError(
        f"O método não convergiu após {max_iter} iterações. Última aproximação: {x_new}")

# Definindo as equações diretamente


def equation1(x): return 3, 504 - 4 * x[1] - 7 * x[2] - 20 * x[3]
def equation2(x): return 25, 1970 - 20 * x[0] - 40 * x[2] - 50 * x[3]
def equation3(x): return 20, 970 - 10 * x[0] - 15 * x[1] - 22 * x[3]
def equation4(x): return 15, 601 - 10 * x[0] - 8 * x[1] - 10 * x[2]


equations = [equation1, equation2, equation3, equation4]
x0 = [0, 0, 0, 0]  # Aproximação inicial

sol, iters = gauss_seidel_equations(equations, x0)
print(f'Equações seidel: solução encontrada: {sol} em {iters} iterações')
