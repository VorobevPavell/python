# Функция которая принимает на входе длину, а выводит все четные числа до этой длины


n = int(input())
def f(n):
    if n < 0:
        for k in range(0,n-1,-1):
            if k %2 == 0:
                print(k, end = " ")
    for i in range(n):
        if i%2 == 0:
            print (i, end= " ")
f(n)



