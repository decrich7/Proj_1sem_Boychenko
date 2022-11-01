while True:
    try:  # обработка исключений
        a = int(input('Введите целое число: ')) # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")

if a % 2 == 0:
    print('Четное')
else:
    print('Не четное')
