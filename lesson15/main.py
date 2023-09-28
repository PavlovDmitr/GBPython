import csv
from keywords import keywords
from mail_model import Mail

def main(file_path: str):
    parts = {}
    mails = {}
    mail = {}
    index = 1
    for k in keywords.keys():
        for item in keywords.get(k):
            parts[item] = k
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        csv_file = csv.reader(file, delimiter=';')
        for mail_line in csv_file:
            for mail_item in mail_line:
                mail[index] = mail_item
            for key in parts.keys():
                if mail_item.find(key):
                    mails[key] = index
                    index += 1

    for k in mail.keys():
        print(k, mail[k], )

if __name__ == '__main__':
    main('user_support_letters.csv')