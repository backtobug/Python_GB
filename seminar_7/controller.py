
from add import add_user
from export import export_user
from view import print_user
from search import search_user


def input_data_user():
    last_name = input('Введите фамилию: ').strip()
    first_name = input('Введите имя: ').strip()
    middle_name = input('Введите отчество: ').strip()
    phone_number = input('Введите номер контакта: ').strip()
    print('----------------------------------------')
    print(f'Контакт записан!\n{last_name} {first_name} {middle_name} {phone_number}')


    return [last_name, first_name, middle_name, phone_number]

def choice():
    sep = ','
    print('-' * 40)
    print('Что будем делать?:\n1 - Добавлять новую запись\n2 - Экспортировать все контакты\n3 - Искать контакт')
    num = input('Введите нужную цифру: ')
    print('-' * 40)
    if num == '1':
        add_user(input_data_user(), sep)
    elif num == '2':
        data = export_user()
        print_user(data)
    else:
        word = input('Кого ищем?: ').strip()
        print('-' * 40)
        data = export_user()
        item = search_user(word, data)
        if item != None:
            print(item)
            print('-' * 40)
        else:
            print('Такой записи пока нет')

