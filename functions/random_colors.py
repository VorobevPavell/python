import random
def change_color():
    for i in range(20):
        color = '#' + ''.join(random.choice('ABCDEF0123456789') for i in range(6)) # присоединяет к # 6 символов
        return color
print(change_color())