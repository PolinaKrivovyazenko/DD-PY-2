class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError('Значение name должно соответствовать типу str')
        self.name = name
        if not isinstance(author, str):
            raise TypeError('Значение author должно соответствовать типу str')
        self.author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Значение pages должно соответствовать типу int')
        if not pages > 0:
            raise ValueError('Значение pages должно быть положительным числом')
        self.pages = pages

    def __str__(self):
         return f"Книга: {self._name}. Автор: {self._author}. Количество страниц: {self.pages}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f"{super_repr}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError('Значение duration должно соответствовать типу float')
        if not duration > 0:
            raise ValueError('duration должно быть положительным числом')
        self.duration = duration

    def __str__(self):
        return f"Книга: {self._name}. Автор: {self._author}. Продолжительность: {self.duration}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f"{super_repr}"