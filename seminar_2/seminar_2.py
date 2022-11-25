num = input('Введите число: ')
count = 0
for i in num:
    if i == ',' or i == '-':
        continue
    count += int(i)
print(count)
