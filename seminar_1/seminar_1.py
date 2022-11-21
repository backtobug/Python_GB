days = [1, 2, 3, 4, 5]
number = int(input())
if 1 < number < 8:
    if number in days:
        print('Работать, еще будни')
    else:
        print('Выходные')
else:
    print('Хорошая попытка, но нет')

# =====================================================================
# for x in [True, False]:
#     for y in [True, False]:
#         for z in [True, False]:
#             print(x, y, z) # если я конечно правильно понял задание

# =======================================================================

# x = int(input('Введите x: '))
# y = int(input('Введите y: '))

# if x == 0 and y == 0:
#     print('0')
# elif x > 0 and y > 0:
#     print('плоскость 1')
# elif x < 0 and y > 0:
#     print('плоскость 2')
# elif x < 0 and y < 0:
#     print('плоскость 3')
# elif x > 0 and y < 0:
#     print('плоскость 4')

# =========================================================================

# num = int(input('Введите четверть: '))

# if num == 1:
#     print('От x > 0 до y > 0')
# elif num == 2:
#     print('От x < 0 до y > 0')
# elif num == 3:
#     print('От x < 0 до y < 0')
# elif num == 4:
#     print('От x > 0 до y < 0')
# else:
#     print('четверти всего 4')

# =============================================================================
# import math

# ax = float(input('точка a по оси x:'))
# ay = float(input('точка a по оси y:'))
# bx = float(input('точка b по оси x:'))
# by = float(input('точка b по оси y:'))

# dist = round(math.sqrt((ax-bx)**2+(ay-by)**2), 3)
# print(dist)

# ================================================================================
