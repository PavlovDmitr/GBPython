




'''Доработаем предыдущую задачу. Создайте новую функцию которая генерирует файлы с разными расширениями.
 Расширения и количество файлов функция принимает в качестве параметров. 
 Количество переданных расширений может быть любым.
   Количество файлов для каждого расширения различно. Внутри используйте вызов функции из прошлой задачи.'''

from random import choice, randint


def give_name() -> str:
    name: str = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()



def create_files(ext: str, min_len: int = 6,
    max_len: int = 30, min_size: int = 256,
    max_size: int = 4096, count_files: int = 42):
    for _ in range(count_files):
        with(open(give_name() + ext, 'w', encoding='utf-8') as file_output):
            list_of_bytes = bytes([randint(0,255) for x in range(min_size, max_size)])

            file_output.write(str(list_of_bytes))

EXTEN = ('.txt', '.doc', '.pdf')
def create_random_ext_files():
    ext = choice(EXTEN)
    create_files(ext=ext)


if __name__ == "__main__":
    create_files(ext='.txt')

'''Дорабатываем функции из предыдущих задач. 
Генерируйте файлы в указанную директорию - отдельный параметр функции. 
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). 
Существующие файла не должны удаляться/изменяться в случае совпадения имён.'''
from os import chdir, listdir, mkdir, getcwd
from pathlib import Path

def give_name() -> str:
    name: str = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def create_files(ext: str, directory: str = None, min_len: int = 6,
    max_len: int = 30, min_size: int = 256,
    max_size: int = 4096, count_files: int = 42):
    if not directory:
        directory = getcwd() + '\\'
    else:
        if directory not in listdir():
            mkdir(directory)
        directory = getcwd() + '\\' + directory + '\\'

    for _ in range(count_files):
        with open(directory + give_name() + ext, 'w', encoding='utf-8') as output:
            list_of_bytes = bytes([randint(0, 255) for x in range(min_size,
            max_size)])

    output.write(str(list_of_bytes))


if __name__ == "__main__":
    EXTINSIONS = ['.pdf', '.csv', '.txt', '.doc']
    create_files(ext=choice(EXTINSIONS),
    directory='test_dir\\test_test_dir', count_files=5)

'''# Создайте функцию для сортировки файлов по директориям:
# видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы,
# которые не подошли для сортировки.'''

def sort_files(directory: str | Path = 'test_dir'):
    chdir(directory)
    print(listdir())
    for file in Path(getcwd()).iterdir():
        if file.is_dir():
            continue
    ext = file.name.split('.')[1]
    if ext.upper() not in listdir():
        mkdir(ext.upper())
        file.replace(f"{ext.upper()}\\{file.name}")




# ЗАДАЧА 3:Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

