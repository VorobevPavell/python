# Задача : Написать алгоритм, для нахождения простых чисел

n = int(input()) #   задам конец диапазона поиска простых чисел путем ввода числа с клавиатуры
a = [True] * n # создам массив буллевых значений, длиной n и буду считать что каждое число в нем- составное
a[0] = a[1] = False #  нулевой и первый элемент всегда составные(???)
for k in range(2,n): # пробегу циклом массив, начиная с 2
    if a[k]:  # !!! если катый элемент простой, то все кратные ему уже не будут простыми, по этому нижу нужен еще один цикл
        for m in range(2*k,n,k): # шаг = к
            a[m] = False


for k in range(n):
    print(k,'-','простое' if a[k] else 'составное')