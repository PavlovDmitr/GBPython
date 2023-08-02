# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

NUMBER_HEX = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def main():
    print(''.join(('  Программа принимает на вход число\n',
    '  и возвращает шестнадцатеричное представление этого числа\n')))
    print('Введите число')
    number = input()
    while (not number.isdigit()):
        print('Please enter a valid number: ')
        number = input()
    number = int(number)
    result = []
    print('Результат встроеной функии hex() - "{}"'.format(hex(number)))
    while number> 0:
        temp = divmod(number, 16)
        result.append(temp[1])
        number = temp[0]
        pass
    result.reverse()
    str_result = ''
    for item in result:
        if item > 9:
            str_result= str_result + NUMBER_HEX[item]
        else: str_result= str_result + str(item)
    print('Результат работы программы - "{}"'.format(str_result))
    


if __name__ == "__main__":
    main()