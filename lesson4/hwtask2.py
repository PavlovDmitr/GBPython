'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}
'''



def dictionary(res, pers, mers):
    result = {}
    try:
        result[res] = 'res'
    except TypeError:
        key = " ".join(map(str, res))
        result[key] = 'res'
    try:
        result[pers] = 'pers'
    except TypeError:
        key = " ".join(map(str, pers))
        result[key] = 'pers'
    try:
        result[mers] = 'mers'
    except TypeError:
        key = " ".join(map(str, mers))
        result[key] = 'mers'
    

    return result

if __name__ == "__main__":
    print(dictionary([10,11,12], '20', 30))
