#Вводится список целых чисел в одну строку через пробел. Необходимо выполнить его сортировку выбором по возрастанию (неубыванию).


arr = list(map(int,input().split()))

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(find_smallest(arr)))

    return newArr

print(*selectionSort(arr))