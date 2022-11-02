#  Узнать имеется ли в числе число 2

while True:
    try:  # обработка исключений
        inp = int(input('Введите вещественное число: '))  # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")

i = 0
while inp != 0 and i != 2:
    i = inp % 10
    inp = inp // 10

print(i == 2)


