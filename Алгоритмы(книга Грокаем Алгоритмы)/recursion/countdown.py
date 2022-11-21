# Функция для обратного отсчета в рекурсивном виде :


def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)

print(countdown(11))