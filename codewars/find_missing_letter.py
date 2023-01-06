'''
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'

'''
from string import ascii_lowercase,ascii_uppercase
def find_missing_letter(chars):
    chars = list(chars)
    if chars[0] in ascii_lowercase:
        arr = list(ascii_lowercase)
    else:
        arr = list(ascii_uppercase)
    start = (arr.index(chars[0]))
    end = start+len(chars)+1
    new_arr = arr[start:end]
    res = filter(lambda x : x not in chars ,new_arr)
    return next(res)
