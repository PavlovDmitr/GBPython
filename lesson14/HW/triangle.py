'''
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например нельзя создавать прямоугольник со сторонами отрицательной длины.
'''
from exption import TriangleExistException, TriangleSideTypeException

MIN_SIDE_LENGHT = 0


def triangle(a:int = None, b: int = None, c: int = None):
    print('''Программа принимает на вход 3 цифровых значения
    и проверяет на существование треуголька с такими сторонами'''.expandtabs(tabsize=4))
    print(f'Check triangle {a=}, {b=}, {c=}: ')
    sides = {'a': a, 'b': b, 'c': c}
    if None in [a, b, c]:
        keys = sides.keys()
        for side in keys:
            print('Please enter a side {}:'.format(side))
            side_str = input()

            if (not side_str.isdigit()) or int(side_str) < MIN_SIDE_LENGHT:
                raise TriangleSideTypeException
                # print('Please enter a valid number greater than zero, {}: '.format(side))
                # side_str = input()
                
            sides.update({side: int(side_str)})
    if  ((sides.get('a') > sides.get('b') + sides.get('c')) or
            (sides.get('b') > sides.get('a') + sides.get('c')) or
            (sides.get('c') > sides.get('b') + sides.get('a'))):
        raise TriangleExistException
        
    if  sides.get('a') == sides.get('b') or sides.get('a') == sides.get('c') or sides.get('b') == sides.get('c'):
        if sides.get('b') != sides.get('c') or sides.get('a') != sides.get('c') or sides.get('b') != sides.get('a'):
            print('the triangle is isosceles')
            return "isosceles"
        else: 
            print('the triangle is equilateral')
            return "equilateral"
    else: 
        print('the triangle is versatile')
        return "versatile"
    

if __name__ == "__main__":
    triangle()