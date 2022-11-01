# Суммирование числового ряда

while True:
    try:  # обработка исключений
        len_row = int(input('Введите длинну числового ряда: '))  # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")

def sum(len_row): # функция суммирования
    resalt = 0
    i = 0
    while i < len_row:
        try:
            resalt += int(input('Введите число: '))
            i += 1
        except ValueError:
            print("Не корректный ввод, попробуйте еще раз!")

    return resalt


print(sum(len_row))

