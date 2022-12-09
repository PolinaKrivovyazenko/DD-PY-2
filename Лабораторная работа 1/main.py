import doctest


class Notebook:
    def __init__(self, total_number_of_pages: int, empty_pages_number: int, owner: str, subject: str):
        """
        Создание и подготовка к работе объекта "Тетрадь"
        :param total_number_of_pages: Общее количество страниц в тетради
        :param empty_pages_number: Количество пустых страниц в тетради
        :param owner: Владелец тетради
        :param subject: Предмет, по которому ведется тетрадь
        Примеры:
        >>> notebook_1 = Notebook(48, 30, "Полина", "Физика")  # инициализация экземпляра класса
        """
        if not isinstance(total_number_of_pages, (int, float)):
            raise TypeError("Количество страниц в тетради должно быть типа int или float")
        if total_number_of_pages < 0:
            raise ValueError("Число страниц в тетради не может быть отрицательным числом")

        if not isinstance(empty_pages_number, (int, float)):
            raise TypeError("Количество пустых страниц должно быть типа int или float")
        if empty_pages_number < 0:
            raise ValueError("Число пустых страниц в тетради не может быть отрицательным числом")
        if empty_pages_number > total_number_of_pages:
            raise ValueError("Число пустых страниц в тетради не может быть больше общего числа страниц")

        if not isinstance(owner, str):
            raise TypeError("Владелец тетради не может быть числом")
        self.owner = owner

        if not isinstance(subject, str):
            raise TypeError("Предмет, по которому ведется тетрадь, не может быть числом")
        self.subject = subject

    def is_empty_notebook(self) -> bool:
        """
        Функция которая проверяет является ли тетрадь пустой
        :return: Является ли тетрадь пустой
        Примеры:
        >>> notebook_1 = Notebook(48, 30, "Полина", "Физика")
        >>> notebook_1.is_empty_notebook()
        """
        ...

    def writing_in_notebook(self, estimate_page: float) -> None:
        """
        Письмо в тетради.
        :param estimate_page: Объем исписанных страниц
        :raise ValueError: Если количество исписанных страниц превышает количество пустых, то возвращается ошибка.
        :return: Число оставшихся пустых страниц
        Примеры:
        >>> notebook_1 = Notebook(48, 30, "Полина", "Физика")
        >>> notebook_1.writing_in_notebook(15)
        """
        ...

class Playlist:
    def __init__(self, number_of_songs: int, total_duration: (int, float)):
        """
        Создание и подготовка к работе объекта "Плейлист"
        :param number_of_songs: Количество песен в плейлисте
        :param total_duration: Общая длительность плейлиста(в минутах)
        Примеры:
        >>> Pop_hits = Playlist(20, 60)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_songs, int):
            raise TypeError("Количество песен должно быть целым числом")
        if number_of_songs < 0:
            raise ValueError("Количество песен не может быть отрицательным")
        self.number_of_songs = number_of_songs

        if not isinstance(total_duration, (int, float)):
            raise TypeError("Общая длительность плейлиста должна быть int или float")
        if total_duration < 0:
            raise ValueError("Длительность плейлиста не может быть отрицательным числом")
        self.total_duration = total_duration

    def is_empty_playlist(self) -> bool:
        """
        Функция которая проверяет является ли плейлист пустым
        :return: Является ли плейлист пустым
        Примеры:
        >>> sad_songs = Playlist(1, 3.5)
        >>> sad_songs.is_empty_playlist()
        """
        ...

    def add_songs_to_playlist(self, addition_number: int, addition_duration) -> None:
        """
        Добавление песен в плейлист.
        :param addition_number: Количество добавляемых песен в плейлист
        :param addition_duration: Общая длительность добавляемых песен
        >>> sad_songs = Playlist(1, 3.5)
        >>> sad_songs.add_songs_to_playlist(2, 8)
        """
        ...

class Window:
    def __init__(self, material: str, height: (float, int), width:(float, int), is_opened: bool):
        """
        Создание и подготовка к работе объекта "Окно"
        :param material: материал оконной рамы
        :param height: Высота рамы
        :param width: Ширина рамы
        :param is_opened: Открыто ли окно
        Примеры:
        >>> window_in_my_room = Window('Plastic', 1.5, 2, True)  # инициализация экземпляра класса
        """

        if not isinstance(material, str):
            raise TypeError("Материал оконной рамы должен быть типа str")
        self.material = material

        if not isinstance(height, (int, float)):
            raise TypeError("Высота окна должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота окна должна быть положительным числом")
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина окна должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина окна должна быть положительным числом")
        self.width = width
        self.is_opened = True

    def is_window_open(self) -> bool:
        """
        Функция которая проверяет является ли окно открытым
        :return: Является ли окно открытым
        Примеры:
        >>> window_in_my_room = Window('Plastic', 1.5, 2, True)
        >>> window_in_my_room.is_window_open()
        """
        ...

    def open_window(self, to_open: bool) -> None:
        """
        Открытие окна(действие).
        :param to_open: Индикатор открытия окна
        >>> window_in_my_room = Window('Plastic', 1.5, 2, False)
        >>> window_in_my_room.open_window(True)
        """


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации