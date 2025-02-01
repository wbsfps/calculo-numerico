from itertools import permutations
import numpy as np


def verifica_dominancia_diagonal(matriz):
    return all(
        abs(matriz[i, i]) > sum(abs(matriz[i, j])
                                for j in range(len(matriz)) if j != i)
        for i in range(len(matriz))
    )


# Sistema original
matriz_coeficientes = np.array([
    [12, -3, 2, -1, 3],
    [9, 14, 1, 2, -1],
    [1, 7, -4, 23, 8],
    [3, 6, 22, 5, 7],
    [-8, -5, 5, 4, 33]
], dtype=float)

vetor = np.array([23, 16, -85, 7, 19], dtype=float)

indices_linhas = range(len(matriz_coeficientes))
melhor_matriz = None
melhor_vetor = None

for permutacao in permutations(indices_linhas):
    matriz_permutada = matriz_coeficientes[list(permutacao), :]
    vetor_permutado = vetor[list(permutacao)]
    if verifica_dominancia_diagonal(matriz_permutada):
        melhor_matriz = matriz_permutada
        melhor_vetor = vetor_permutado
        break

if melhor_matriz is None:
    print("Não foi possível reorganizar para matriz diagonalmente dominante.")
    melhor_matriz, melhor_vetor = matriz_coeficientes, vetor

# Método de Gauss-Seidel
precisao = 1e-10
maximo_iteracoes = 1000

vetor_solucao = np.zeros(len(melhor_vetor))
vetor_anterior = np.zeros(len(melhor_vetor))

for iteracao in range(maximo_iteracoes):
    for i in range(len(melhor_matriz)):
        soma1 = sum(melhor_matriz[i, j] * vetor_solucao[j] for j in range(i))
        soma2 = sum(melhor_matriz[i, j] * vetor_anterior[j]
                    for j in range(i + 1, len(melhor_matriz)))
        vetor_solucao[i] = (melhor_vetor[i] - soma1 -
                            soma2) / melhor_matriz[i, i]

    # Critério de parada
    if np.linalg.norm(vetor_solucao - vetor_anterior, ord=np.inf) < precisao:
        print(f"Teve {iteracao + 1} iterações")
        break

    vetor_anterior = vetor_solucao.copy()

print(vetor_solucao)
