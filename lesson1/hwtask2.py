MIN_NUMBER = 0
MAX_NUMBER = 100000


def main():
    print(''.join(('  The program accepts 3 numbers as input\n',
    '  and checks their possibility of the existence\n', 
    '  of a triangle with sides of the appropriate length.')))
    print('Еhe program takes a number as input and checks it for simplicity')
    print('Check a number between 0 and 100000: ')
    number = input()
    while (not number.isdigit()) or int(number) < MIN_NUMBER or int(number) > MAX_NUMBER:
        print('Please enter a valid number greater than zero: ')
        number = input()
    number = int(number)
    k = 0
    for i in range(2, number // 2+1):
        if (number % i == 0):
            k = k+1
    if (k <= 0):
        print("the number is simple")
    else:
        print("the number is not simple")



if __name__ == "__main__":
    main()