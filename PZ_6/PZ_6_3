from random import randint
# Поменять пестами первый элемент со вторым и т.д
while True:
    try:  # обработка исключений
        N = int(input('Введите длинну списка: '))  # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")

list_p = [randint(0, 100) for i in range(N)]
print(list_p)
for i in range(N - 1):
    list_p[i], list_p[i + 1] = list_p[i + 1], list_p[i]
print(list_p)
