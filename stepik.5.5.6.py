#В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64. Вводится натуральное число n. Как наименьшим количеством таких денежных купюр можно выплатить сумму n? Вывести на экран список купюр для формирования суммы n (в одну строчку через пробел, начиная с наибольшей и заканчивая наименьшей). Предполагается, что имеется достаточно большое количество купюр всех достоинств.



dengi = int(input())
stepen = 6
kupuri = 0
res = 0
lst=[]
while dengi !=0:
    kupuri = dengi // 2** stepen # количество купюр
    dengi -=kupuri*2**stepen
    res += kupuri
    for _ in range(kupuri):
        lst.append(2**stepen)
    if dengi < 2 **stepen:
        while dengi < 2**stepen:
            stepen-= 1
    kupuri += kupuri


print(*lst)