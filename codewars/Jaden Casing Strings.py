#Дана строка, нужно чтобы каждое слово начиналось с большой буквы.
#https://www.codewars.com/kata/5390bac347d09b7da40006f6/solutions?filter=me&sort=best_practice&invalids=false
def to_jaden_case(string):
    string = string.upper().split()
    res = []
    for i in string:
        res.append(i[0]+i[1:].lower())
        a = ' '.join(res)
    return a