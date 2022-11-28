# Реализация алгоритма сортировки слиянием
import timeit

code_to_test = '''
def merge(a,b):
    i = j = 0
    c = []
    while i < len(a) and j<len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i +=1
        else:
            c.append(b[j])
            j+=1
    if i<len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        low = merge_sort(arr[:mid])
        high = merge_sort(arr[mid:])
    return merge(low,high)



'''
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)


# Результаты (в секундах):
# 4.51
# 3.69
# 6.36
# 3.74
# 7.55
