# Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
# полученных последовательностях



import random

N = int(input())
sequence = [random.randint(0, 100) for i in range(N)]
divisible_by_three = filter(lambda x: x % 3 == 0, sequence)
not_divisible_by_three = filter(lambda x: x % 3 != 0, sequence)

divisible_by_three = list(divisible_by_three)
not_divisible_by_three = list(not_divisible_by_three)

print("Исходная последовательность: ", sequence)
print("Последовательность для чисел, кратных трем: ", divisible_by_three)
print("Последовательность для всех остальных чисел: ", not_divisible_by_three)
print("Количество элементов в последовательности для чисел, кратных трем: ", len(divisible_by_three))
print("Количество элементов в последовательности для всех остальных чисел: ", len(not_divisible_by_three))
