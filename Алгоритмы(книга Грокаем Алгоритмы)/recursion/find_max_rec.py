# Найти наибольшее число в списке 


def find_max(arr):
    if arr == []:  # Базовый случай
        return 0
    if len(arr) == 1: # Если в массиве один элемент, то он и будет наибольшим
        return arr[0]
    else:
        sub_max = find_max(arr[1:]) # Рекурсивный случай, передаем главной функции все элементы,начиная со второго
        return arr[0] if arr[0] > sub_max else sub_max

print(find_max([63,12,24,68,172,1]))