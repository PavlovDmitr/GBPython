

def separate(data: list):
    result = []
    for item in data:
        data.remove(item)
        if (item in data) and not (item in result):
            result.append(item)
    return result

def main():
    print('Программа принимает на вход список объектов,\nи возвращает список продублированных элементов')
    data = str(input()).split(' ')
    print(separate(data))

if __name__ == "__main__":
    main()