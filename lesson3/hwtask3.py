# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


ITEMS = {'Палатка': 1.5, 'Спальник' : 0.75 , 'Коврик': 0.5,
          'Горелка': 0.3, 'Дождевик': 0.1,'Котелок': 0.2,'КЛМН': 0.4,
          "Фонарик+1": 0.3, 'Компас': 0.05, 'Радиостанция': 0.3,
           'Аптечка':0.3, 'Навигатор': 0.3, 'PowerBank': 0.5, 'Сапоги': 0.9, 'Еда': 2, 'Вода': 5}


def separate(weight: int):
    result = []
    isinstance
    for item in ITEMS.keys():
        if (weight - ITEMS.get(item)) > 0:
            weight -= ITEMS.get(item)
            result.append(item)
        str.sp
    return result

def main():
    print('''Программа принимает на вход грузоподъемность рюкзака
          возвращает список вещей влезающих в этот рюкзак.'''.replace('  ', ''))
    weight = int(input('Введите грузоподъемность рюкзака: '))
    print(separate(weight))

if __name__ == "__main__":
    main()