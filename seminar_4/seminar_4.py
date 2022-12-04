import math

pi = math.pi
num = input('Введите число: 0.001, 0.01 и тд..: ').count('0')
print(f'Число {pi:.{num}f}')
# =====================================================

# def simple_f(n):
#     i = 2
#     lst = []
#     while i * i <= n:
#         while n % i == 0:
#             lst.append(i)
#             n = n / i
#         i = i + 1
#     if n > 1:
#         lst.append(n)
#     print(lst)
#
#
# simple_f(100)
# =========================================================

# num = 1113384455229567467970
# st = str(num)
# lst = []
# for i in st:
#     if st.count(i) < 2:
#         lst.append(int(i))
# print(lst)
# ===========================================================

# from random import randint
# import random
#
# num = int(input('Введите число '))
#
# res = ''
# temp = []
# for i in range(num):
#     temp.append(randint(0, 100))
#
# sym = ['+', '-']
# i = 0
# j = 0
# while num > 1:
#     if temp[i] != 0:
#         res += f'{temp[i]}x**{num}{random.choice(sym)}'
#     num -= 1
#     i += 1
#
# if temp[-1] != 0:
#     res += f'{temp[-1]}=0'
# else:
#     res += '=0'
# with open('res.txt', 'a+', encoding='utf8' ) as file:
#     file.write(f'{temp} \n {res}')
# ===============================================================
