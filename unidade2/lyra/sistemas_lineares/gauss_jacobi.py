def norma(v, x):
    return max(abs(v[i] - x[i]) for i in range(len(v)))


def jacobi(A, b, epsilon, iterMax=100):

    n = len(A)
    x = n * [0]
    v = n * [0]

    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                A[i][j] = A[i][j]/A[i][i]
                # print(A[i][j])
        b[i] = b[i]/A[i][i]
        x[i] = b[i]

    for k in range(0, iterMax):
        for i in range(0, n):
            soma = 0
            for j in range(0, n):
                if i != j:
                    soma = soma + A[i][j]*x[j]
            v[i] = b[i] - soma

        if norma(v, x) <= epsilon:
            return v  # Convergiu com precisão desejada

        x = v[:]

    return x


# não convergia
"""A = [[3,2,4],
      [2,2,3],
      [3,3,5]]"""


A = [[7, 2, 4],
     [2, 6, 3],
     [3, 3, 7]]

b = [320, 240, 380]
epsilon = 0.001
x = jacobi(A, b, epsilon)
print(x)
