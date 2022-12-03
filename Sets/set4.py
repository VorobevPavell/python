#Даны два списка чисел. Выведите все числа в порядке возрастания, которые входят в первый список, но при этом отсутствуют во втором.


n = [int(i) for i in input().split()]
n1 = [int(i) for i in input().split()]

s = set(n)
s1 = set(n1)

s.difference_update(s1)
print(*sorted(list(s)))