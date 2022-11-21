#Дана коробка, наполненная другими коробками, в которых может быть либо коробка,либо ключ. Задача : найти ключ. (Псевдокод)
#Решение 1 с помощью цикла while, без рекурсии


from queue import Empty


def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not Empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print('found the key')


# Решение 2 (также псевдокод) с помощью рекурсии(вызова функцией самой себя)


def look_for_key(box):      # Объявляем функцию, передаем ей параметр коробка
    for item in box:        # Перебор каждого элемента в коробке:
        if item.is_a_box(): # Если предмет - коробка, то :
            look_for_key(item) #  объявляем эту же функцию, но передаем ей в параметры предмет(т.е коробку,которая лежит в коробке)
        elif item.is_a_key(): # А если это не коробка, то ключ, задача решена
            print('found the key')