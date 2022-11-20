def get_max(a,b):
    return a if a > b else b


def get_max3(a,b,c):
    return get_max(a,(get_max(b,c)))


x,y,z = 3,2,1




PERIMETR = False
if PERIMETR:
    def get_rect(a,b):
        return 2 * (a + b)

else:
    def get_rect(a,b):
        return a * b

o,p = 2,3



def even(x):
    return x%2 == 0


for i in range(1,20):
    if even(i):
        print(i)