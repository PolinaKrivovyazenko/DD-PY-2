if __name__ == "__main__":
    class Cars:
        def __init__(self, brand: str, model: str, color: str, year: int):
            '''Класс Автомобили
                Атрибуты
                --------
                brand: str
                    бренд, выпустивший автомобиль
                model: str
                    модель автомобиля
                color : str
                    цвет кузова автомобиля
                year : int
                    год выпуска автомобиля
                Методы
                ------
                info(additional=""):
                    Печатает имя и возраст владельца.
            '''
            self.brand = brand
            self.model = model
            self.color = color
            self.year = year

        def __str__(self) -> str:
            return f'Автомобили "{self.brand}" "{self.model}" коллекция "{self.color}" в оттенке "{self.year}"'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.model!r}, collection={self.color!r}, shade={self.year})'

        @staticmethod
        def buy(self):
            '''Метод Покупки автомобиля'''
            print("Car was bought")

        def fill_the_car(self):
            '''Метод заправки автомобиля'''
            fuel = 'petrol'
            print("Fill the car with" + fuel)


    class PassengerCars(Cars):
        def __init__(self, brand: str, model: str, color: str, year: int, seats: int, transmission: str):
            '''Класс Легковые автомобили
                Атрибуты
                --------
                seats: int
                    число пассажирских сидений

                transmission: str
                    тип передачи

                Методы
                ------
                info(additional=""):
                Печатает имя и возраст владельца.
            '''
            super().__init__(brand, model, color, year)
            self.seats = seats
            self.transmission = transmission

        # Перегрузим только метод __repr__, т.к. у легковых автомобилей появились новые атрибуты,
        # но выводить для пользователя мы их не будем

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.model!r}, color={self.color!r}, year={self.year}, ' \
                   f'seats={self.seats}, transmission={self.transmission}) '

        # метод buy унаследуем от родительского класса

        def wash_carblush(self):
            '''Метод мытья автомобиля
                перегрузим метод родительского класса, т.к. для автомобили разных типов используется разное топливо
            '''
            fuel = 'AI-92'
            print("Fill the car with" + fuel)


    pass
