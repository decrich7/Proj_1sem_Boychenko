import random

f = open('numbers.txt', 'w')
f.write(' '.join([str(random.randint(-50, 50)) for i in range(5)]))
f.close()
f = open('numbers.txt', 'r')
data = f.read().split(' ')
list_data = [int(i) for i in data]
square_element = [str(i ** 2) for i in list_data if i % 2 == 0]
f.close()
f = open('numbers.txt', 'w')
f.write(f'Исходные данные - {data}\n')
f.write(f'Количество элементов - {len(data)}\n')
f.write(f'Минимальный элемент - {min(list_data)}\n')
f.write(f'Квадраты четных элементов - {" ".join(square_element)}\n')
f.write(f'Сумма квадратов четных элементов - {sum([int(i) for i in square_element])}\n')
f.write(f'Среднее арифметическое квадратов четных элементов - {sum([int(i) for i in square_element]) / len(square_element)}\n')
f.close()