'''
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например нельзя создавать прямоугольник со сторонами отрицательной длины.
'''

class TriangleSideTypeException(Exception):
    print("Не правильный формат данных")
    pass

class TriangleExistException(Exception):
    print("Треугольник не существует")
    pass


MIN_SIDE_LENGHT = 0


def main():
    print('''Программа принимает на вход 3 цифровых значения
    и проверяет на существование треуголька с такими сторонами'''.expandtabs(tabsize=4))
    print('Check triangle: ')
    sides = {'a': 0, 'b': 0, 'c':0}
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
        else: print('the triangle is equilateral')
    else: print('the triangle is versatile')
    

if __name__ == "__main__":
    main()