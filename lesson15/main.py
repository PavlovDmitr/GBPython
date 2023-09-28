import csv
from keywords import keywords
from mail_model import Mail
import os

def main(file_path: str):
    parts = {}
    mails = []
    index = 0
    for k in keywords.keys():
        for item in keywords.get(k):
            parts[item] = k
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as file:
            csv_file = csv.reader(file, delimiter=';')
            for mail_line in csv_file:
                for mail_item in mail_line:

                    mails.append(Mail(index, body = mail_item, subj=''))
                    index += 1
    except FileNotFoundError:
        print('Файл не найден')
        mails.append(None)
    return mails

if __name__ == '__main__':
    current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(current_file)
    os.chdir(current_directory)
    res = main('user_support_letter.csv')
    print(res[len(res)-1])