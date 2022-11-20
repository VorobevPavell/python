#Вводится число новых подписчиков канала по дням в одну строку через пробел. На основе введенной строки необходимо сформировать список lst из целых чисел. Требуется отсортировать элементы этого списка по убыванию и результат вывести на экран командой:print(*lst)

lst = list(map(int,input().split()))

#функция для нахождения индекса наибольшего элемента в списке
def findSmallest(lst):
    biggiest = lst[0]
    biggiest_index = 0
    for i in range(1,len(lst)):
        if lst[i] > biggiest:
            biggiest = lst[i]
            biggiest_index = i
    return biggiest_index

#функция сортировки выбором на основе предыдущей функции


def selectionSort(lst):
    newLst = []
    for i in range(len(lst)):
        biggiest = findSmallest(lst)
        newLst.append(lst.pop(biggiest))
    return(newLst)


print(*selectionSort(lst))