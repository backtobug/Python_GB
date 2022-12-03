import math

pi = math.pi
num = input('Введите число d пример: 0.001, 0,01: ')
count = 0

num = num.replace('0.', '')

for i in num:
    count += 1

print(f'Число {pi:.{count}f}')
