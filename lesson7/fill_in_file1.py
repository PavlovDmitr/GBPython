'''Напишите функцию, которая генерирует псевдоимена. 
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, 
среди которых обязательно должны быть гласные. 
Полученные имена сохраните в файл.'''

from random import randint, uniform

def fill_in_file(name_file: str, count_line: int) -> None:
    name_file += '.txt'

    with open(name_file, 'a', encoding='utf-8') as file:
        for _ in range(count_line):
            file.write(f"{randint(-1000, 1000)} | {uniform(-1000, 1000)} \n")


if __name__ == "__main__":
    fill_in_file(name_file="test_file",
    count_line=5)