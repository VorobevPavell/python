# Если в массиве нет или 1 элемент, то его не нужно сортировать и это базовый случай
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]     # Опорный элемент
        less = [i for i in arr[1:] if i < pivot] #  Подмассив меньших опорного
        high = [i for i in arr[1:] if i > pivot] # Подмассив больших опорного

        return quicksort(less) + [pivot] + quicksort(high)   # Возвращаем отсортированные подмассивы и опорный элемент(в центре)

print(quicksort([18,-9,16,25,42,66,8]))