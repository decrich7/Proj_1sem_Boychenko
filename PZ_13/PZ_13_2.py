# Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое


matrix = [
    [1, 2, -3],
    [4, -5, 6],
    [7, 8, -9]
]

positive_even = []

for row in matrix:
    for elem in row:
        if elem > 0 and elem % 2 == 0:
            positive_even.append(elem)

sum_of_elements = sum(positive_even)
average = sum_of_elements / len(positive_even)

print("Массив положительных четных элементов:", positive_even)
print("Сумма элементов:", sum_of_elements)
print("Среднее арифметическое:", average)