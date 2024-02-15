#Вариант 3
#Даны два списка чисел. Найдите все числа, которые входят как в первый,
#так и во второй список и выведите их в порядке возрастания.

A = sorted(list(set([int(s) for s in input().split()]) & set([int(s) for s in input().split()])))
for elem in A:
    print(elem, end=' ')
