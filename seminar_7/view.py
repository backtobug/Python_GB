
def print_user(data):
    if len(data) > 0:
        print('-' * 40)
        for item in data:
            print(f'{item[0]} {item[1]} {item[2]} {item[3]}')
        print('-' * 40)
    else:
        print('Контакты не найдены :(')