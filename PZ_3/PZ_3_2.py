#  Составить программу определяющую процентную ставку в зависимости от цены

while True:
    try:  # обработка исключений
        price = int(input('Введите цену товара: '))  # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")

# в зависимости от цены, начисляется определенная скидка
if 500 > price:
    discount = price * 0.02
elif 1000 > price > 500:
    discount = price * 0.03
elif 1500 > price > 1000:
    discount = price * 0.04
elif 2000 > price > 1500:
    discount = price * 0.05
else:
    discount = 'Для данной суммы нет скидок'

print(f'Цена с учетом скидки составляет - {discount}')


