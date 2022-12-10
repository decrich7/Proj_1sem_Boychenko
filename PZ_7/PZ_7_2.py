# Если буквы в строке упорядочены по алфавиту, то вывести 0. В противном случае вывести номер первого символа нарушающего алфавитный порядок


while True:
    try:  # обработка исключений
        string = input('Введите строку: ') # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")


list_str_non_int = []
for i in string:
    if i not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        list_str_non_int.append(i)


if list_str_non_int == sorted(list_str_non_int):
    print('0')
else:
    for i in range(len(list_str_non_int)):
        if list_str_non_int[i] != sorted(list_str_non_int)[i]:
            print(i)
            break
