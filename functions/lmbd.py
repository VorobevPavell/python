#Объявите анонимную (лямбда) функцию для вычисления модуля числа (то есть, отрицательные числа нужно делать положительными). Вызовите эту функцию для введенного числа x:

x = float(input())
a = lambda x: abs(x)
res = a(x)
print(res)