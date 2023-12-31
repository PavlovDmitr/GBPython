# Задача №6
# Напишите программу банкомат.

# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег


import os

TAX_PERCENT = 0.015
TAX_MIN = 30
TAX_MAX = 600
CASHBACK_PERCENT = 0.03
CASHBACK_COUNT = 3
TAX_FREE_LIMIT = 5000000
WEALTH_TAX_PERCENT = 0.1

MAIN_MENU = "Выберите действие: \n1. Пополнить баланс. \n2. Снять. \n3. Выход"
ADD_MENU = "Выберите действие: \n1. Пополнить на 50 у.е. \n2. Пополнить на 100 у.е. \n3. Пополнить на 200 у.е.\n4. Пополнить на другую сумму. \n5. Выход"

def clear(ballance):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Текущий баланс: {}".format(round(ballance, 2)))

def cashback(bank: dict):
    cashback = bank.get('ballance') * CASHBACK_PERCENT
    bank['ballance'] = bank.get('ballance') + cashback
    bank['history'].append(f'+{cashback}')
    bank['count'] = 1
    
def insert() -> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Введите сумму кратную 50у.е.')
    while True:
        money = input()
        if money.isdigit() and int(money) % 50 == 0:
            return int(money)
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print('ОШИБКА. Введите сумму кратную 50у.е. ')
    
    

    

def deposit(bank: dict, cash: int) -> str:
    if bank['ballance'] >= TAX_FREE_LIMIT:
        ballance = bank.get('ballance')
        bank['ballance'] = ballance - ballance * WEALTH_TAX_PERCENT
    if cash % 50 != 0: return 'fail'
    bank['ballance'] = bank.get('ballance') + cash
    bank['history'].append(f'+{cash}')
    if bank.get('count') == CASHBACK_COUNT:
        cashback(bank)
    else: bank['count'] = bank.get('count') + 1
    return 'pass'

def cash(bank: dict, cash: int) -> str:
    if bank['ballance'] >= TAX_FREE_LIMIT:
        print('ПОЗДРАВЯЛЕМ ВЫ - САМЫЙ ЛЮБИЙ КЛИЕНТ НАШЕГО ПСЕВДОБАНКА')
        ballance = bank.get('ballance')
        bank['ballance'] = ballance - ballance * WEALTH_TAX_PERCENT
    if cash % 50 != 0: return 'fail'
    tax = cash * TAX_PERCENT
    if tax < TAX_MIN:
        tax = TAX_MIN
    elif tax > TAX_MAX:
        tax = TAX_MAX
    if bank.get('ballance') > (cash + tax):
        ballance = bank.get('ballance')
        bank['ballance'] = ballance - (cash + tax)
        bank['history'].append(f'-{cash}')
        bank['history'].append(f'-{tax}')
    else: return 'fail'
    if bank.get('count') == CASHBACK_COUNT:
        cashback(bank)
    else: bank['count'] = bank.get('count') + 1
    return 'pass'
    


def main():
    bank = {'ballance': 0, 'count': 0, 'history': []}
  
    while True:
        clear(bank.get('ballance'))
        print(MAIN_MENU)
        menu1 = input()
        if  menu1 == '1':
            while True:
                clear(bank.get('ballance'))
                print(ADD_MENU)
                money = int(input())
                if money == 1:
                    deposit(bank=bank, cash=50)
                elif money == 2:
                    deposit(bank=bank, cash=100)
                elif money == 3:
                    deposit(bank=bank, cash=200)

                elif money == 4:
                    deposit(bank, insert())
                elif money == 5: break
                else: input('Выберите один из пунктов')
        elif menu1 == '2':
            while True:
                clear(bank.get('ballance'))
                print(ADD_MENU)
                money = int(input())
                if money == 1:
                    cash(bank=bank, cash=50)
                elif money == 2:
                    cash(bank=bank, cash=100)
                elif money == 3:
                    cash(bank=bank, cash=200)

                elif money == 4:
                    cash(bank, insert())
                elif money == 5: break
                else: input('Выберите один из пунктов')
        elif menu1 == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Закрытие программы')
            break
        else: print('ОШИБКА!ОШИБКА!ОШИБКА!')

if __name__ == "__main__":
    
            

    main()