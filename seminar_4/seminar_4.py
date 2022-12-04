# import math
#
# pi = math.pi
# num = input('Введите число d пример: 0.001, 0,01: ')
# count = 0
#
# num = num.replace('0.', '')
#
# for i in num:
#     count += 1
#
# print(f'Число {pi:.{count}f}')
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

num = 1113384455229567467970
st = str(num)
lst = []
for i in st:
    if st.count(i) < 2:
        lst.append(int(i))
print(lst)


