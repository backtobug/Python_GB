
def export_user():
    with open('notebook.csv', 'r', encoding='utf8') as file:
        data = []
        for line in file:
            temp = line.strip().split(',')
            data.append(temp)
    return data