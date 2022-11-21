def f(n):
    assert n >= 0 , 'Факториал отрицательных не определен'
    if n == 1:
        return 1
    return f(n-1) * n

#print(f(5))


def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)

#print(gcd(18,4))



def sq(a,n):
    if n == 0:
        return 1
    elif n % 2 ==1:
        return sq(a,n-1)*a
    else: # a -четное 
        return sq(a**2,n//2)
print(sq(2,3))
