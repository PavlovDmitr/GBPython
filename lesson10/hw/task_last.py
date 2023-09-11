class Animal:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']

    def __str__(self) -> str:
        return f'{self.name} {self.age}'

    def birthday(self):
        self.age += 1


class Dog(Animal):
    def __init__(self,
                name: str = 'dog',
                age: int = 0,
                color: str = 'черный',
                breed : str = 'домашняя',
                domestic: bool = True) -> None:
        super().__init__(name = name, age = age)

        self.color = color
        self.breed = breed
        self.is_domestic = domestic

    def __str__(self):
        if self.is_domestic:
            return f'Dog {self.name} {self.color} {self.breed} домашняя'
        return f'Dog {self.name} {self.color}  {self.breed} дворняга'


class Kotopes(Animal):
    def __init__(self,
                 age: int,
                 name: str,
                 number_heads: int = 2) -> None:
        super().__init__(name, age)
        self.__number_heads = number_heads

    def __str__(self):
        return f'Kotopes -> number_heads: {self.__number_heads},\
Возраст: {self.age}, не женат '


class Fish(Animal):

    def __init__(self, name: str, age: int, 
                 aqua: str = 'морская', 
                 size: float = 1.0):
        super().__init__(name, age)
        self.aqua = aqua
        self.size = size

    def __str__(self):
        if self.aqua:
            return f'{self.name} морская'
        else:
            return f'{self.name} пресноводная'


if __name__ == "__main__":
    dog = Dog('Бобик', 3, "рыжий", "спаниель", True)
    dog2 = Dog('Тузик', 4, "серый", "спаниель", False)
    f1 = Fish("Дори", 1, True, 0.5)
    kt1 = Kotopes(3, "котопес", 2)
    print(dog)
    print(f1)
    print(kt1)
    kt1.birthday()
    print(kt1)