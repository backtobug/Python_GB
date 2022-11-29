# from random import randint
#
# lst = [randint(1, 10) for i in range(10)]
#
# def odd_position(a):
#     count = 0
#     for i in range(0, len(a)):
#         if i % 2 == 1:
#             count += a[i]
#     print(f'{lst} ==> {count}')
#
# odd_position(lst)
# ===========================================

# from random import randint
#
# lst = [randint(1, 10) for i in range(5)]
#
# def multiply_pairs(a):
#     rev = a[::-1]
#     count = round(len(a) / 2)
#     result = []
#     if len(a) % 2 == 0:
#         for i in range(0, count):
#             result.append(lst[i] * rev[i])
#     else:
#         for i in range(0, count + 1):
#             result.append(lst[i] * rev[i])
#     print(f'{lst} ==> {result}')
#
# multiply_pairs(lst)
# =============================================

from random import uniform

lst = [round(uniform(1, 2), 2) for i in range(5)]


def float_minmax(a):
    max_min = []
    for i in range(len(a)):
        if a[i] % 1 != 0:
            max_min.append(a[i] % 1)
    return max(max_min) - min(max_min)


print(lst)
result = float_minmax(lst)
print(f'разница максимальной и минимальной дробной части = {result:.2f}')
