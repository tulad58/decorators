import re
import csv
from collections import defaultdict


def read_csv(file):
    with open(file, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        return list(rows)


def get_new_contacts_list(contacts_list):
    new_contacts_list = []
    for line in contacts_list:
        new_list = []
        for i in range(3):
            new_list.append(line[i])
        string = ' '.join(new_list)
        splited = string.split()
        lastname, firstname, = splited[0], splited[1]
        if len(splited) > 2:
            surname = splited[2]
        else:
            surname = ''
        organization, position, phone, email = line[3], line[4], line[5], line[6]
        new_contacts_list.append([lastname, firstname, surname, organization, position, phone, email])
    return new_contacts_list


def format_phones(some_list):
    for el in some_list:
        pattern = r"(\+7|8)\s?\(?(\d\d\d)\)?[\s-]?(\d\d\d)[-\s]?(\d\d)[-\s]?(\d\d)[\s]?\(?(доб\.)?\s?(\d+)?\)?"
        subst_patter = r"+7(\2)\3-\4-\5 \6\7"
        phone = el[5]
        result = re.sub(pattern, subst_patter, phone)
        el.pop(5)
        el.insert(5, result)
    return some_list


def delete_duplicate(some_list):
    data = defaultdict(list)
    for info in some_list:
        key = tuple(info[:2])
        for item in info:
            if item not in data[key]:
                data[key].append(item)
    return list(data.values())


def write_to_csv(contacts_list):
    with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
    return print(f"phonebook.csv was created")


if __name__ == "__main__":
    contacts_list = read_csv("phonebook_raw.csv")
    new_list = get_new_contacts_list(contacts_list)
    formatted_forms_list = format_phones(new_list)
    final_list = delete_duplicate(formatted_forms_list)
    write_to_csv(final_list)
