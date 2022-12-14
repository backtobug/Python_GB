lst = [1, 4, 5, 2, 3, 9, 8, 11, 0]

lst.sort()
lst2 = [[lst[0]]]
j = lst[0]
print (lst)

for i in lst[1:]:
    if i-j == 1:
            lst2[-1].append(i)
    else:
            lst2.append([i])
    j = i
rez1 = [i[0] for i in lst2]
rez2 = [i[len(i)-1] for i in lst2]
print (lst2)
print (str(rez1[0])+'-'+str(rez2[0]))

k=0
while k < len(rez1):
    print (str(rez1[k])+'-'+str(rez2[k]))
    k += 1