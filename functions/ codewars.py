#Complete the solution so that it reverses the string passed into it.


from turtle import pen


def solution(string):
    return string[::-1]


#We need a function that can transform a number (integer) into a string.


def number_to_string(num):
    return str(num)


#Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".


def greet(name):
    text = f"Hello, {name} how are you doing today?"
    return text 
    #name = input()


#Can you find the needle in the haystack?Write a function findNeedle() that takes an array full of junk but containing one "needle"After your function finds the needle it should return a message (as a string) that says:"found the needle at position " plus the index it found the needle, so:


def find_needle(haystack):
    for i in range(0,len(haystack)):
        if haystack[i] == 'needle':
            mes = f'found the needle at position {i}'
            return mes
            


haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

#print (find_needle(haystack))


#Объявите функцию с именем is_large, которая принимает строку (в качестве аргумента) и возвращает False, если длина строки меньше трех символов. Иначе возвращается значение True.

def is_large(a):

    if len(a) < 3:
        return False
    else:
        return True



#Объявите функцию для проверки числа на четность (возвращается True, если переданное число четное и False, если число нечетное).После объявления функции в цикле необходимо считывать целое числовое значение (функцией input), пока не поступит число 1. Если прочитанное значение четное (проверяется с помощью заданной функции), то оно выводится на экран (в столбик, то есть, каждое значение с новой строки).

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

i = int(input())
while i != 1 :
    if is_even(i) == True:
        print(i)
    i = int(input())
        


