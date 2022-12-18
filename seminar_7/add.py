
def add_user(data, sep):
    with open('notebook.csv', 'a+', encoding='utf8') as file:
        file.write(sep.join(data))
        file.write(f'\n')
