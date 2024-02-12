class Mammal:
    """ Базовый класс млекопитающего. """

    def __init__(self, name: str, age: int):
        """
                Инициализация экземпляра класса.

                :param name: имя животного
                :param age: возраст животного

                Example:
                >>> mammal = Mammal("some_name", 8)
                """
        if not isinstance(name, str):
            raise TypeError("Name must be str!")
        self._name = name
        self.age = age

    def make_call(self):
        """ Издает звуки, характерные для млекопитающего"""
        ...

    def celebrate_birthday(self):
        """ Увеличить возраст на год и вывести поздравление """
        self._age += 1
        print(f"Happy Birthday {self._name}!")

    def __str__(self):
        return f"Имя {self._name}. Возраст {self._age}"

    def __repr__(self):
        return f"{self.__class__.__name__}(_name={self._name!r}, _age={self._age!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Age must be int!")
        if value < 0:
            raise ValueError("Age must be non negative!")
        self._age = value


class Echidna(Mammal):
    """ Наследник класса Mammal. Представляет собой ехидну. """

    def __init__(self, name: str, age: int):
        """
                Инициализация экземпляра класса.

                :param name: имя животного
                :param age: возраст животного

                Example:
                >>> animal = Echidna("some_name", 15)
                """
        super().__init__(name, age)

    def make_call(self) -> None:
        """ Издать звуки, характерные для ехидны"""
        ...

    def __str__(self):
        return "Ехидна. " + super().__str__()


if __name__ != "__main__":
    ech = Echidna("bob", 10)
    print(ech.__repr__())
