# Алгоритм Евклида. Нахождение наибольшего общего делителя для двух чисел.



def find_nod(a,b):
    while a != b:
        if a < b:
            b -=a
        else:
            a -=b
    return a

print(find_nod(24,18))