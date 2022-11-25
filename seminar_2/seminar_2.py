num = input('Введите число: ')
count = 0
for i in num:
    if i == ',' or i == '-':
        continue
    count += int(i)
print(count)
# ==============================================
#
# num = int(input('Введите число: '))
# temp = 1
# lst =[]
#
# for i in range(1, num+1):
#     temp = temp * i
#     lst.append(temp)
# print(lst)
# =================================================

# num = int(input('Введите число: '))
# list = []
# for i in range (1, num+1):
#     list.append((1+1/i)**i)
# print(list)
# print(sum(list))
# =================================================
#
# import random
# num = int(input('Введите размер списка: '))
# lst = [random.randint(0,100) for i in range(num)]
# print(f"список:\n{lst}")
# random.shuffle(lst)
# print(f"перемешанный список:\n{lst}")
# ===================================================