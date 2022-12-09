#Write a simple parser that will parse and run Deadfish.

#Deadfish has 4 commands, each 1 character long:

#i increments the value (initially 0)
#d decrements the value
#s squares the value
#o outputs the value into the return array
#Invalid characters should be ignored.

#https://www.codewars.com/kata/51e0007c1f9378fa810002a9

def parse(data):
    result = 0
    res_arr = []
    for i in data:
        if i == 'i':
            result += 1
            print(result)
        if i == 'd':
            result -= 1
            print(result)
        if i == 's':
            result = result ** 2
            
        if i == 'o':
            res_arr.append(result)
    return res_arr
