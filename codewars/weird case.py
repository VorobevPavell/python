#Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.
# ('Weird string case')  => returns 'WeIrD StRiNg CaSe'
#https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python

def to_weird_case(words):
    words = words.split()
    res = []
    for j in words:
        res.append(' ')
        for i,val in enumerate(j):
            if i % 2 == 0:
                res.append(val.upper())
            else:
                res.append(val.lower())
    a = ''.join(res[1:])
    return a