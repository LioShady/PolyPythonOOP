# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import List


class Human:
    def __init__(self, name: str, surname: str, residential_address: str, age: int):
        """
        Примеры:
        >>> dimon = Human("Дмитрий", "Иванов", "улица", 20)

        >>> dimon = Human("Дмитрий", "Иванов", "улица", -20)
        Traceback (most recent call last):
        ...
        ValueError: age must be non negative

        >>> dimon = Human("Дмитрий", "Иванов", "улица", "20")
        Traceback (most recent call last):
        ...
        TypeError: age must be int
        """
        if not isinstance(name, str):
            raise TypeError("name must be string")
        self.name = name  # Имя
        if not isinstance(surname, str):
            raise TypeError("surname must be string")
        self.surname = surname  # Фамилия
        if not isinstance(residential_address, str):
            raise TypeError("address must be string")
        self.residential_address = residential_address
        if not isinstance(age, int):
            raise TypeError("age must be int")
        if age < 0:
            raise ValueError("age must be non negative")
        self.age = age  # Возраст

    def celebrate_birthday(self) -> None:
        # Повышаем возраст, выводим поздравление
        # self.age += 1
        # print("happy birthday!")
        ...

    def move_to_new_address(self, new_address: str) -> None:
        # Смена адреса проживания на new_address
        # self.residential_address = new_address
        if not isinstance(new_address, str):
            raise TypeError("address must be string")
        if self.residential_address == new_address:
            raise ValueError("new address can't be current address")


class Phone:
    def __init__(self, owner: Human, battery_level: int, is_on: bool):
        self.owner = owner  # Владелец телефона
        if not isinstance(battery_level, int):
            raise TypeError("battery_level must be int")
        if battery_level < 0 or battery_level > 100:
            raise ValueError("battery_level must be between 0 and 100")
        self.battery_level = battery_level  # Уровень заряда
        if not isinstance(is_on, bool):
            raise TypeError("phone must be on or off")
        self.is_on = is_on  # Включен ли телефон

    def get_battery_level(self) -> int:
        # return battery_level
        ...

    def turn_on(self) -> None:
        # if not self.is_on:
        #   self.is_on = True
        ...

    def turn_off(self) -> None:
        # if self.is_on:
        #   self.is_on = False
        ...


class Dormitory:
    def __init__(self, array_of_living: List[Human], director: Human):
        self.array_of_living = array_of_living  # Список проживающих
        self.director = director  # Заведующий общежитием

    def evict(self, evicted: Human) -> None:
        if not isinstance(evicted, Human):
            raise TypeError("evicted must be Human")
        # выселение человека evicted из общежития
        # self.array_of_living.remove(evicted)
        # evicted.move_to_new_address("улица")
        ...

    def close_forever(self) -> None:
        # закрыть общежитие и выселить всех его жителей
        ...

    def change_director(self, new_director: Human) -> None:
        if not isinstance(new_director, Human):
            raise TypeError(" new director must be human (PLEASE)")
        if new_director is self.director:
            raise ValueError("New director can't be current director")
        # сменить директора общежития на нового new_director


if __name__ == "__main__":
    doctest.testmod()
