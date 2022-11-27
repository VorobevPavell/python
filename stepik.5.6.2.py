#Вводится натуральное число n. Необходимо найти все простые числа, которые меньше этого числа n, то есть, в диапазоне [2; n). Результат вывести на экран в строчку через пробел.

n = int(input())
a = [True] * n
lst = []
a[0] = a[1] = False
for k in range(2,n):
    if a[k]:
        for m in range(2*k,n,k):
            a[m] = False

for k in range(n):
    if a[k]:
        lst.append(k)
print(*lst)