
def search_user(word, data):
    count = 0
    temp = ''
    if len(data) > 0:
        for item in data:
            if word in item:
                temp += f'{item[0]} {item[1]} {item[2]} {item[3]}' + '\n'
                count += 1
        temp += f'\nНайдено контактов с такими данными - ({count})'
        return temp
    else:
        return None
