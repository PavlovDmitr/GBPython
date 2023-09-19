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
from Course import Course

from Range import Range


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


class Student:

    __age = Range(10, 103)
    __name = Name()
    table = Course
   
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.course = 1
        self.table = Course(self.course)

    def add_test(self, discipline, number, test):
        self.table.add_test_result(discipline, number, test)

    def set_grade(self, discipline, grade):
        self.table.add_grade_value(self.table, discipline, grade)

    def __repr__(self):

        return f'Student(Name={self.__name}, age={self.__age}, Тесты = {self.table})'

    def get_name(self) -> str:
        return self.__name
    

if __name__ == '__main__':
    Archimed = Student('Архимед', 16)
    Archimed.add_test('Алгебра', 1, 94)
    Archimed.add_test('Алгебра', 2, 92)
    Archimed.add_test('Алгебра', 3, 10)
    # Archimed.ins_grade_test('Геометрия', grade = 4, test = 75)
    # Archimed.ins_grade_test('Математический анализ', grade = 4, test = 85)
    # Archimed.ins_grade_test('Информатика', grade = 3, test = 64)
    # Archimed.ins_grade_test('Иностарнный язык', grade = 4, test = 80)
    # Archimed.ins_grade_test('Литература', 4, 87)
    # Archimed.ins_test('Математический анализ', 90)
    # std_other = Student('Аристотель') 
    # std_one.age = 15
    print(f'{Archimed = }')
    # std_one.grade = 11.0 # TypeError: Значение 11.0 должно быть целым числом
    # std_one.office = 73 # ValueError: Значение 73 должно быть меньше 42
    # del std_one.age # AttributeError: Свойство "_age" нельзя  удалять
    # print(f'{std_one.__dict__ = }')
