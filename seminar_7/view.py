
def print_user(data):
    if len(data) > 0:
        print('----------------------------------------')
        for item in data:
            print(f'{item[0]} {item[1]} {item[2]} {item[3]}')
        print('----------------------------------------')
    else:
        print('Контакты не найдены :(')