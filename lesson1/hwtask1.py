
def chekins(ins: str):
    

    pass


def main():
    print('Check triangle: ')
    sides = {'a': 0, 'b': 0, 'c':0}
    keys = sides.keys()
    for side in keys:
        print('Please enter a side {}:'.format(side))
        side_str = input()
        while (not side_str.isdigit()) or int(side_str) < 0:
            print('Please enter a valid number greater than zero, {}: '.format(side))
            side_str = input()
            
        sides.update({side: int(side_str)})
    if  ((sides.get('a') > sides.get('b') + sides.get('c')) or
            (sides.get('b') > sides.get('a') + sides.get('c')) or
            (sides.get('c') > sides.get('b') + sides.get('a'))):
        print('the triangle does not exist')
        return
    if  sides.get('a') == sides.get('b') or sides.get('a') == sides.get('c') or sides.get('b') == sides.get('c'):
        if sides.get('b') != sides.get('c') or sides.get('a') != sides.get('c') or sides.get('b') != sides.get('a'):
            print('the triangle is isosceles')
        else: print('the triangle is equilateral')
    else: print('the triangle is versatile')
    

if __name__ == "__main__":
    main()