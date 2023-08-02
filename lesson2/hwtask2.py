from fractions import Fraction


def deviders(number: int):
    result = []
    for dev in range(1, number):
        if number % dev == 0:
            result.append(dev)
            number = number // dev
    result.append(number)
    return result


def main():
    print(''.join(('  Программа принимает на вход две дроби\n',
                   '  и возвращает их сумму и произведение\n')))

    print('Введите первую дробь в виде "a/b"')
    number1 = input().split('/')
    while (not len(number1) == 2 or not number1[0].isdigit() or not number1[1].isdigit()):
        print('Введите первую дробь корректно (пример - a/b): ')
        number1 = input().split('/')
    print('Введите вторую дробь')
    number2 = input().split('/')
    while (not len(number2) == 2 or not number2[0].isdigit() or not number2[1].isdigit()):
        print('Введите вторую дробь корректно (пример - a/b): ')
        number2 = input().split('/')
    number1 = (int(number1[0]), int(number1[1]))
    number2 = (int(number2[0]), int(number2[1]))
    numerator = 0
    denominator = 1
    if (number1[1] != number2[1]):
        if not (number1[1] % number2[1] == 0 or number2[1] % number1[1] == 0):
            denominator = number1[1] * number2[1]
            numerator = number1[0] * number2[1] + number2[0] * number1[1]
        elif number1[1] > number2[1]:
            denominator = number1[1]
            numerator = number1[0] * number2[1] + number2[0] * number1[1]
        else:
            denominator = number2[1]
            numerator = number1[0] * number2[1] + number2[0] * number1[1]
    else:
        denominator = number1[1]
        numerator = number1[0] + number2[0]
    if numerator % denominator == 0:
        print("{}/{} + {}/{} = {}".format(number1[0], number1[1], number2[0], number2[1], numerator // denominator))
    else: print("{}/{} + {}/{} = {}/{}".format(number1[0], number1[1], number2[0], number2[1], numerator, denominator))
    numerator = number1[0] * number2[0]
    denominator = number1[1] * number2[1]
    print("{}/{} x {}/{} = {}/{}".format(number1[0], number1[1], number2[0], number2[1], numerator, denominator))
    

if __name__ == "__main__":
    main()
