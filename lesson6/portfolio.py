'''
Расчет общей стоимости портфеля акций. принимает два аргумента: 
stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.),
и значениями - количество акций каждого символа. 
prices - словарь, где ключами являются символы акций, а значениями - текущая цена каждой акции. 
Функция должна вернуть общую стоимость портфеля акций на основе количества акций и их текущих цен
'''
'''
Пришло:
stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
Вышло:
16410,25
'''
__initial_portfolio = {}

def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    if __initial_portfolio == {}:
        for key, value in prices.items():
            __initial_portfolio[key] = {"count": stocks.get(key), "price": value}
    result = 0
    for st_k, st_v in stocks.items():
        for pr_k, pr_v in prices.items():
            if st_k == pr_k:
                result += st_v * pr_v
    return result

    


'''________________________________________________________________'''

'''
Расчет доходности портфеля: Функция  принимает два аргумента: 
initial_value - начальная стоимость портфеля акций. 
current_value - текущая стоимость портфеля акций. 
Функция должна вернуть процентную доходность портфеля. Пример:
'''
'''
Пришло:
10000.0
15000.0
Вышло:
50%
'''


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    
    return round((round(current_value / initial_value, 2) - 
            (current_value // initial_value)) * 100, 2)

    pass


'''
Определение наиболее прибыльной акции: Функция  принимает два аргумента: 
stocks - словарь с акциями и их количеством. 
prices - словарь с акциями и их текущими ценами. 
Функция должна вернуть символ акции (ключ), 
которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью. 
Начальная стоимость - первый вызов calculate_portfolio_value, 
данные из этого вызова следует сохранить в защищенную переменную на уровне модуля.
'''
'''
Пришло:
stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
Вышло:
MSFT
'''



def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    result_name = ""
    result_price = 0
    for key, value in __initial_portfolio.items():
        if stocks.get(key) == value.get("count"):
           temp = prices.get(key) / value.get("price")
           if temp > result_price:
            result_price = temp
            result_name = key

    return result_name
    pass