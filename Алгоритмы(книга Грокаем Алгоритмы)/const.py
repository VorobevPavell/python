# Константы 


def print_item(list):
    for item in list:
        print(item)

from time import sleep
def print_item2(list):
    for item in list:
        sleep(1)
        print(item)

print(print_item([1,2,3,4,5]))
print(print_item2([1,2,3,4,5]))



# Обе эти функции имеют сложность O(n), но первая работает быстрее т.к при использовании О-Большого это означает: с*n, где с - фиксированный промежуток времени,но обычно константа игнорируется, т.к в алгоритмах с разном О-Большим она не играет роли.