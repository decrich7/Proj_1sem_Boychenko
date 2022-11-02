# определить путь пройденный лодкой

while True:
    try:  # обработка исключений
        speed_boat = int(input('Введите скорость лодки: '))
        speed_water = int(input("Введите скорость течения: "))
        time_boat = int(input("Введите время в пути по озеру"))
        time_boat_in_water = int(input("Введите время в пути против течения: "))
        break
    except ValueError:  # обработка исключения ValueError
        print("Вы должны ввести число, попробуйте еще раз")


if speed_boat > speed_water and (time_boat < time_boat_in_water):  # Вычисление пройденного пути
    distance_river = (speed_boat - speed_water) * time_boat_in_water
    distance_lake = speed_boat * time_boat
    print(f'{((speed_boat - speed_water) * time_boat_in_water) + speed_boat * time_boat} км')

else:
    print('Скорость течения больше скорости лодки, исправьте')
