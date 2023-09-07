# Напишите следующие функции:
# 1. Нахождение корней квадратного уравнения

import math


def sq(func):
    def wrapper(a: float, b: float, c:float):
        discr = b ** 2 - 4 * a * c
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            return f"x1 = {x1}, x2 = {x2}"
        elif discr == 0:
            x = -b / (2 * a)
            return f"x = {x}"
        else:
            return "Корней нет"
    return wrapper

