while True:
    try:  # обработка исключений
        price = float(input('Введите вещественное число: ')) # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")

i = 1
while i <= 10:
    print(f'Стоимость конфет за {i} кг - {price * i}')
    i += 1
