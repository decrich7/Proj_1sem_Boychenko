# В квадратной матрице элементы на главной диагонали увеличить в 2 раза


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            matrix[i][j] *= 2

print(matrix)