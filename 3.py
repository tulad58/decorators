import os
from regular import get_new_contacts_list, format_phones, delete_duplicate, read_csv
from logger import logger


paths = ('log_01.log', 'log_02.log', 'log_03.log')
for path in paths:
    if os.path.exists(path):
        os.remove(path)

    @logger(path)
    def read_csv_dec(file):
        return read_csv(file)

    @logger(path)
    def get_new_contacts_list_decorated(contacts_list):
        return get_new_contacts_list(contacts_list)


    @logger(path)
    def formatted_forms_list_2(some_list):
        return format_phones(some_list)

    @logger(path)
    def delete_duplicate_dec(some_list):
        return delete_duplicate(some_list)

    contacts_list = read_csv_dec("phonebook_raw.csv")
    new_list = get_new_contacts_list_decorated(contacts_list)
    formatted_forms_list = formatted_forms_list_2(new_list)
    final_list = delete_duplicate_dec(formatted_forms_list)
