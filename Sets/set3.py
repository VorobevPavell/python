#Даны два списка чисел.Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.


n = [int(i) for i in input().split()]
n1 = [int(i) for i in input().split()]

s = set(n)
s1 = set(n1)

res = s&s1
print(*sorted(list(res)))