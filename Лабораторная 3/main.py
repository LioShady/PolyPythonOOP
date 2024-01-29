class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(_name={self._name!r}, _author={self._author!r})"

    @property
    def author(self) -> str:
        return self._author

    @property
    def name(self) -> str:
        return self._name


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return super().__str__() + f". Количество страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(_name={self._name!r}, _author={self._author!r}, pages={self._pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("pages must be int")
        if value <= 0:
            raise ValueError("duration must be positive")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return super().__str__() + f". Длительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(_name={self._name!r}, _author={self._author!r}, _duration={self._duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, float):
            raise TypeError("duration must be float")
        if value <= 0:
            raise ValueError("duration must be positive")
        self._duration = value


if __name__ == "__main__":
    book = AudioBook('abc', 'ivan', 3.0)
    print(book.author, book.name, book.duration)
    # book.duration = 4.0
