""" Входные данные
В каждой строке будет вводиться одно из имен наших героев, а затем через двоеточие и пробел имя комментатора. Комментаторы могут повторяться и комментировать разных персонажей

Строка "конец" означает окончание ввода и встречается последней

Разбор решения Youtube Patreon Boosty

Входные данные
Ваша задача вывести в порядке уменьшения популярности 3 строки вида:
"Количество уникальных комментаторов у <имя героя> - <количество комментаторов>"
На склонение давайте не будем обращать обращать внимания в этой задаче.

Гарантируется, что количество уникальных комментаторов у всех наших героев разное. Могут быть ситуации, когда у героя нету ни единого комментатора, в таком случае все равно нужно выводить информацию о нем. """
#https://stepik.org/lesson/296966/step/13?thread=solutions&unit=278694


s = ''
billy_com = set()
willie_com = set()
dilly_com = set() 
while s != 'конец':
    s = input()
    s1 = s.split(': ')
    if s1[0] == "Били":
        billy_com.add(s1[1])
    elif s1[0] == "Вили":
        willie_com.add(s1[1])
    elif s1[0] == "Дили":
        dilly_com.add(s1[1])
res = [len(billy_com),len(dilly_com),len(willie_com)]
res = sorted(res)
if res[2] == len(willie_com):
    maxname = 'Вили'
elif res[2] == len(dilly_com):
    maxname = 'Дили'
elif res[2] == len(billy_com):
    maxname = 'Били'

if res[1] == len(willie_com):
    midname = 'Вили'
elif res[1] == len(dilly_com):
    midname = 'Дили'
elif res[1] == len(billy_com):
    midname = 'Били'

if res[0] == len(willie_com):
    minname = 'Вили'
elif res[0] == len(dilly_com):
    minname = 'Дили'
elif res[0] == len(billy_com):
    minname = 'Били'

print(f"Количество уникальных комментаторов у {maxname} - {res[2]}")
print(f"Количество уникальных комментаторов у {midname} - {res[1]}")
print(f"Количество уникальных комментаторов у {minname} - {res[0]}") 