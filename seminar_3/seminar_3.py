from random import randint

lst = [randint(1, 10) for i in range(10)]

def odd_position(a):
    count = 0
    for i in range(0, len(a)):
        if i % 2 == 1:
            count += a[i]
    print(f'{lst} ==> {count}')

odd_position(lst)