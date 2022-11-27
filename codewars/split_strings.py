#Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').



def solution(s):
    m = []
    if len(s) % 2 != 0:
        s = s + '_'
    for i in range(len(s)):
        orig_i = i
        res = s[orig_i-1] + s[orig_i]
        if i % 2 == 1:
            m.append(res)
    return m

s = input()
print(solution(s))