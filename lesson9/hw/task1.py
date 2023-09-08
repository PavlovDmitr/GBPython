# Напишите следующие функции:
# 1. Нахождение корней квадратного уравнения

import json
import math
import csv
from random import randint
from typing import Callable


def rnd_csv_file(): 
    rnd_lst = []
    for i in range(randint(1,11)):
        rnd_str = [str(randint(100,1000)), str(randint(100,1000)), str(randint(100,1000))]
        rnd_lst.append(rnd_str)
    with open('random.csv', 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter=';')
        csv_writer.writerows(rnd_lst)


if __name__ == '__main__':
    rnd_csv_file()


def read_csv(func:Callable):
    cread = []
    result = []
    with open('random.csv', 'r', newline='', encoding='utf-8') as file:
        csv_read = csv.reader(file, delimiter=';')
        cread  = [x for x in csv_read]
    def wrapper():
        for line in cread:
            args = tuple(int(x) for x in line)
            result.append([line, func(*args)])
        return result
    return wrapper


def write_json(func: Callable):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res_for_file = dict()
        for result in res:
            print('для a, b, c = ', result[0], 'корни = ', result[1])
            res_for_file.update({','.join(result[0]): result[1]})
            with open('result.json', 'w', encoding='utf-8') as file:
                file.write(json.dumps(res_for_file, separators=(',', ':'), indent=2))
    return wrapper


@write_json
@read_csv
def quadratic_equation(a: float, b: float, c:float):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return (f"x1 = {x1}, x2 = {x2}")
    elif discr == 0:
        x = -b / (2 * a)
        return (f"x = {x}")
    else:
        return ("Корней нет")
    


if __name__ == '__main__':
    quadratic_equation()
