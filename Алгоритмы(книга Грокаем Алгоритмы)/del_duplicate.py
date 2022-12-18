# Дан список. Необходимо удалить повторяющиеся элементы, то есть сделать список из уникальных элементов. Нельзя использовать доп. память.
my_arr = [0,0,0,1,1,1,2,2,3,3,3]

#f p = 0
#s p = 2
def del_counter(arr):
    first_pointer, second_pointer = 0,0 # Два указателя
    while second_pointer < len(arr): #  Главное условие, что цикл будет выполняться пока второй указатель меньше длины массива
        while second_pointer < len(arr) -1 and arr[second_pointer] == arr[second_pointer+1]:
            second_pointer += 1
        
        arr[first_pointer] = arr[second_pointer]
        first_pointer += 1
        second_pointer += 1
    return arr[:first_pointer]

print(del_counter(my_arr))