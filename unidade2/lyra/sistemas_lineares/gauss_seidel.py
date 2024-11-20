def norma(v, x):
    return max(abs(v[i] - x[i]) for i in range(len(v)))


def seidel(A, b, epsilon, iterMax=50):

    n = len(A)
    x = n * [0]
    v = n * [0]

    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                A[i][j] = A[i][j]/A[i][i]
        b[i] = b[i]/A[i][i]

    for k in range(0, iterMax):
        for i in range(0, n):
            soma = 0
            for j in range(0, n):
                if i != j:
                    soma = soma + A[i][j]*x[j]
            x[i] = b[i] - soma
        d = norma(x, v)
        if d <= epsilon:
            return x
        v = x[:]
    return x


""" não converge
A = [
    [3, 4, 7, 20],    # Equação da mão de obra
    [20, 25, 40, 50], # Equação do metal
    [10, 15, 20, 22], # Equação do plástico
    [10, 8, 10, 15]   # Equação dos componentes eletrônicos
]"""


A = [
    [31, 4, 7, 20],    # Equação da mão de obra
    [20, 111, 40, 50],  # Equação do metal
    [10, 15, 48, 22],  # Equação do plástico
    [10, 8, 10, 29]    # Equação dos componentes eletrônicos
]
b = [504, 1970, 970, 601]  # Restrição de recursos diários

epsilon = 0.001
x = seidel(A, b, epsilon)
print(x)
