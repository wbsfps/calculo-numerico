# f (x) = sen(10x) + cos(3x) - intervalo 3, 6 - Precisão 10^-5
import math

# listas
list_intervals = []
list_multiplication_intervals = []
# 1. Dados iniciais
xa = 3
xb = 6
PRECISION = 0.00001

# 2. Cálculos iniciais


def calculate_function(x) -> float:
    return math.sin(10*x) + math.cos(3*x)


interval_3 = calculate_function(3)
interval_6 = calculate_function(6)

list_intervals.append(interval_3)
list_intervals.append(interval_6)

root = False


def multiplication_of_intervals_less_than_zero(first_interval_value, second_interval_value) -> 0:
    calculate_intervals = first_interval_value * second_interval_value

    if calculate_intervals < 0:
        root = True
        return calculate_intervals, root
    else:
        new_interval_1 = float(input("Digite novo intervalo 1: "))
        new_interval_2 = float(input("Digite novo intervalo 2: "))
        multiplication_of_intervals_less_than_zero(
            new_interval_1, new_interval_2)  # não sei como mas funcionou!
        return multiplication_of_intervals_less_than_zero(new_interval_1, new_interval_2)


multiplication_intervals = multiplication_of_intervals_less_than_zero(
    interval_3, interval_6)
list_multiplication_intervals.append(multiplication_intervals)

# 3. Nova aproximação
xm = (xa + xb) / 2
value_xm_to_interval = calculate_function(abs(xm))

verification_if_contains_source = 'Contêm raiz. Fim!' if value_xm_to_interval < PRECISION else 'Não contêm raiz, rodar novamente'

print(list_multiplication_intervals, list_intervals)
print(verification_if_contains_source)
print(value_xm_to_interval)
