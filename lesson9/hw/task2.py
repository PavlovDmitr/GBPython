import csv
from random import randint


def rnd_csv_file():
    rnd_lst = []
    for i in range(randint(100,1001)):
        rnd_str = [str(randint(100,1000)), str(randint(100,1000)), str(randint(100,1000))]
        rnd_lst.append(rnd_str)

    with open('random.csv', 'w', newline='', encoding='utf-8') as file:

        csv_writer = csv.writer(file, delimiter=';')
        csv_writer.writerows(rnd_lst)