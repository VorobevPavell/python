# Найдите НОД из 270 и 192


def f(a,b):
    if a< b:
        a,b = b,a

    while b!= 0:
        a,b = b,a%b
    return a

print(f(270,192))