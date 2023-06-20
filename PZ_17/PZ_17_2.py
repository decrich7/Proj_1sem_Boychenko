# Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров



class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Truck(Car):
    def __init__(self, brand, model, year, cargo):
        super().__init__(brand, model, year)
        self.cargo = cargo

class PassengerCar(Car):
    def __init__(self, brand, model, year, passenger):
        super().__init__(brand, model, year)
        self.passenger = passenger



car = Car("Toyota", "Corolla", 2010)
truck = Truck("Volvo", "FH16", 2020, 5000)
passenger_car = PassengerCar("Honda", "Civic", 2015, 5)
