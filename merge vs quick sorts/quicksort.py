import timeit




code_to_test = '''
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i<pivot]
        high = [i for i in arr[1:] if i>pivot]
    return quicksort(less) + [pivot] + quicksort(high)
'''

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)


# Результаты (в секундах):
# 2.39
# 2.53
# 2.43
# 4.39
# 2.42