# Стек вызовов


def greet(name):
    print("hi " + name + " !")
    greet2(name)
    print("Ready to say goodbye")
    bye(name)

def greet2(name):
    print("How are you, " + name +" ?")
def bye(name):
    print("See u soon again, " + name + ":)))))")


greet('pasha')