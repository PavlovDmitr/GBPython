import csv
import os

from Range import Range


class Course:

    __subjects = []

    class Test(Range):
        min_value = 0
        max_value = 100
        def __init__(self, min_value: int = None, max_value: int = None):
            super().__init__(min_value, max_value)

    class Grade(Range):
        min_value = 2
        max_value = 5
        def __init__(self, min_value: int = None, max_value: int = None):
            super().__init__(min_value, max_value)
    
    __tests = {str: {str: Test}}
    __grade = {str: Grade}
    __number = Range(1,3)

    def __init__(self, number:int) -> None:
        self.__number = number
        
        with open(f'course{self.__number}.csv', 'r', newline='', encoding='utf-8') as file:
            lines = csv.reader(file, delimiter=';')
            for item in lines:
                
                self.__subjects.extend(item)

        for item in self.__subjects:
            self.__tests[item] = dict()


    def add_grade_value(self, value, result):
        self.validate(value)
        self.__grade[value] = result

    def add_test_result(self, value, number, result):

        self.validate(value)
        # print(self.__tests)
        self.__tests[value][number] = result
    
    def get_tests_result(self, value):
        self.validate(value)
        count = 0
        x = 0
        # print(self.__tests[value])
        for key in self.__tests[value].keys():
            
            x = x + self.__tests[value].get(key)
            count += 1
        if count == 0: # вот тут мозг отказал и пошел спать)
            count = 1
        return x / count

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __repr__(self) -> str:
        return ', '.join([f'{sub}: {self.get_tests_result(sub)}' for sub in self.__subjects])
        

    def validate(self, value):
        if str(value) not in self.__subjects:
            raise TypeError(f'чет не совпадает {value} с базой ')