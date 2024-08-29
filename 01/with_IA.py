import math

# Listas para armazenar intervalos e multiplicações
list_intervals = []
list_multiplication_intervals = []

# 1. Dados iniciais
xa = 3
xb = 6
PRECISION = 0.00001

# 2. Função para calcular f(x)


def calculate_function(x) -> float:
    return math.sin(10 * x) + math.cos(3 * x)

# 3. Função para verificar se a multiplicação dos intervalos é menor que 0


def multiplication_of_intervals_less_than_zero(xa, xb):
    f_xa = calculate_function(xa)
    f_xb = calculate_function(xb)
    multiplication = f_xa * f_xb
    list_intervals.append((xa, xb))
    list_multiplication_intervals.append(multiplication)

    return multiplication < 0

# 4. Implementação do método da bisseção


def bisection_method(xa, xb):
    if not multiplication_of_intervals_less_than_zero(xa, xb):
        print("Os valores iniciais não garantem que há uma raiz no intervalo.")
        return None

    while abs(xb - xa) / 2 > PRECISION:
        xm = (xa + xb) / 2
        f_xm = calculate_function(xm)

        # Verifica se encontrou a raiz com a precisão desejada
        if abs(f_xm) < PRECISION:
            return xm

        # Adiciona os novos valores à lista
        list_intervals.append((xa, xb))

        # Verifica em qual metade está a raiz e ajusta o intervalo
        if multiplication_of_intervals_less_than_zero(xa, xm):
            xb = xm
        else:
            xa = xm

    return (xa + xb) / 2


# 5. Chamar o método da bisseção e imprimir resultados
raiz = bisection_method(xa, xb)

if raiz is not None:
    print(f"Raiz encontrada: {raiz:.5f}")
else:
    print("Não foi possível encontrar uma raiz no intervalo fornecido.")

print("Lista de intervalos:")
for interval in list_intervals:
    print(f"Xa = {interval[0]:.5f}, Xb = {interval[1]:.5f}")

print("\nMultiplicações dos Intervalos:")
for mult in list_multiplication_intervals:
    print(f"{mult:.5f}")
