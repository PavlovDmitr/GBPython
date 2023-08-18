# ЗАДАЧА 2: Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#    К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

# Пример:
# rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv

from os import getcwd
from pathlib import Path


def rename(wanted_name: str='', count_nums: int=3, 
           extension_old: str='', extension_new: str='', diapazon=[3, 5]):
    count = 0
    for file in Path(getcwd()).iterdir():
        if file.is_dir():
            continue
        extension = file.name[-4:]
        print(file.name, extension, end='. ')
        if len(extension_old) > 0 and extension == extension_old:
            if count < count_nums:
                basename = file.name[diapazon[0]: diapazon[1]]
                count += 1
                new_name = basename + wanted_name + str(count) + extension_new
                print('New Name ', new_name)
                file.rename(new_name)
            else: 
                basename = file.name[diapazon[0]: diapazon[1]]
                count = 0
                new_name = basename + wanted_name + str(count) + extension_new
                print('New Name ', new_name)
                file.rename(new_name)
                

 

if __name__ == "__main__":
    rename(wanted_name = "video", count_nums=5, extension_old=".txt", extension_new=".csv", diapazon=[1, 6])