while True:
    try:  # обработка исключений
        C = input('Введите символ С: ')  # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")

print(f'Предыдущий символ - {chr(ord(C) - 1)}\nСледующий символ - {chr(ord(C) + 1)}')
