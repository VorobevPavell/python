#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
#You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.


def sort_array(source_array):
    # Return a sorted array.
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0:
            continue
        for j in range(i,len(source_array)):
            if source_array[j] % 2 != 0:
                if source_array[i] > source_array[j]:
                    source_array[i],source_array[j] = source_array[j],source_array[i]
                    
    return source_array

print(sort_array([5, 3, 2, 8, 1, 4]))