# Нахождение площади и периметра равностороннего треугольника

while True:
    try:  # обработка исключений
        a = int(input('Введите сторону треугольника: '))  # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")



def TrianglePS(a):
    P = a * 3
    S = a ** 2 * 3 ** 0.5 / 4
    return f'Площадь - {S} \nПериметр - {P}'


print(TrianglePS(a))
