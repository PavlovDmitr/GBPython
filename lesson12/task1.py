'''
Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную
 букву и наличие только букв.
- Названия предметов должны загружаться из файла CSV при 
создании экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и 
результаты тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для 
каждого предмета и по оценкам всех предметов вместе взятых.
'''
import csv
import os


class Name:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
        
    
    def validate(self, value: str):
        if not value.isalpha():
            raise TypeError(f'Имя {value} должно содержать только буквы')
        if value[0] != value[0].upper():
            raise TypeError(f'Имя {value} должно быть с большой буквы')

class Range:
    def __init__(self, min_value: int = None, max_value: int =
        None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')

class Student:
    
    age = Range(10, 103)
    name = Name()
    def load_():
        current_file = os.path.realpath(__file__)
        with open(current_file.split('.')[0]+'csv', 'r', newline='', encoding='utf-8') as file:
            lines = csv.reader(file, delimiter=';')
        pass
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age})'
    
if __name__ == '__main__':
    std_one = Student('Архимед', 16)
    # std_other = Student('Аристотель') 
    # std_one.age = 15
    print(f'{std_one = }')
    # std_one.grade = 11.0 # TypeError: Значение 11.0 должно быть целым числом
    # std_one.office = 73 # ValueError: Значение 73 должно быть меньше 42
    # del std_one.age # AttributeError: Свойство "_age" нельзя  удалять
    # print(f'{std_one.__dict__ = }')
