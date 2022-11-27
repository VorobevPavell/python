# Имеется массив чисел, нужно проссумировать все числа и вернуть сумму.

#Решение с помощью цикла

def summarr(arr):
    sum = 0
    for i,val in enumerate(arr):
        sum += val
    return sum

print(summarr([2,4,6]))


#Решение с помощью рекурсии


def find_sum(arr):
    if arr == []:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        sub_sum = find_sum(arr[1:])
        return arr[0] + sub_sum


print(find_sum([2,4,6]))