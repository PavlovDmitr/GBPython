from portfolio import calculate_portfolio_value  as calc_value
from portfolio import calculate_portfolio_return as calc_retur
from portfolio import get_most_profitable_stock as most_profit
from chess import check_8_queens as check8


STOKS_OLD = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
PRICES_OLD = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}

STOKS_NEW = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
PRICES_NEW = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
_SAFE_COMB_EXAMPLE = [(0, 0), (6, 1), (4, 2), (7, 3),
(1, 4), (3, 5), (5, 6), (2, 7)]
_SAFE_COMB_EXAMPLE2 = [(3, 1), (7, 1), (0, 2), (2, 3),
(5, 4), (1, 5), (6, 6), (4, 7)]

def main():
    old_price = calc_value(stocks=STOKS_OLD, prices=PRICES_OLD)
    print("Цена портфеля на момент создания: {}".format(old_price))
    new_price = calc_value(stocks=STOKS_NEW, prices=PRICES_NEW)
    print("Цена портфеля на текущий момент : {}".format(new_price))
    print("Доходность портфеля на текущий момент: {}".format(calc_retur(old_price, new_price)))
    print("Самое прибыльное вложение: {}".format(most_profit(stocks=STOKS_NEW, prices=PRICES_NEW)))
    print(check8(_SAFE_COMB_EXAMPLE2))

    pass


if __name__ == "__main__":
    main()