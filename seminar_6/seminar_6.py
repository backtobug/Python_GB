# 5 - 6 задание из Яндекса

s = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
st = s + ' '
result = ''
count = 1

for i in range(len(st)):
    if st[i] == ' ':
        break
    if st[i] == st[i+1]:
        count += 1
    elif count == 1:
        result += st[i]
    else:
        result += str(count) + st[i]
        count = 1
print(result)

# ==============================================
# lst = [1, 4, 5, 2, 3, 9, 8, 11, 0]
#
# lst.sort()
# lst2 = [[lst[0]]]
# j = lst[0]
#
# for i in lst[1:]:
#     if i - j == 1:
#         lst2[-1].append(i)
#     else:
#         lst2.append([i])
#     j = i
# result = [i[0] for i in lst2]
# result2 = [i[len(i) - 1] for i in lst2]
# print(lst2)
# print(str(result[0]) + '-' + str(result2[0]))
#
# k = 0
# while k < len(result):
#     print(str(result[k]) + '-' + str(result2[k]))
#     k += 1

