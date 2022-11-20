# Вводятся 2 слова. Нужно определить будут ли они равны если к одному прибавить или удалить букву (или поменять местами две уже существующие.)
# Не дорешал эту задачу, т.к не успеваю из-за большого количества материала,который нужно выучить, но знаю как ее дорешать(обязательно это сделаю когда появится время)


a = input()
b = input()
s = 0
s1 = 0
# буду проверять на то, что два слова одинаковые, но надо поменять 2 буквы
if len(a) == len(b):
    for x,y in enumerate(b): # Перебор второго слова
        #x = 012345
        #y = gfif (second)
        print()
    for i,d in enumerate(a): # перебор 1 слова
        if ord(d) == ord(y):
            print('True')
            break
         #i = 0123 
        # d = gfif (firs)


# если первое слово больше на одну букву
elif len(a) == len(b) + 1:
    for i,d in enumerate(a): # перебор 1 слова
        s1 += ord(d)
    print()
    #print('True')
    
        #i = 0123 
        #d = gfif (firs)


    for x,y in enumerate(b): # Перебор второго слова
        s += ord(y) # сумма кодов второго слова
        if s + ord(d) == s1 :#сумма орд первого:
    #x = 012345
    #y = gfif (second)
            print()
            print('True')
            break
        elif s + ord(d) != s1:
            print('False')
            break
            

# если второе слово больше на 1 букву
elif len(b) == len(a) - 1:
    for i,d in enumerate(a): # перебор 1 слова
        s1 += ord(d) # first codes
         #i = 0123 
         #d = gfif (firs)
        

    for x,y in enumerate(b): # Перебор второго слова
        s += ord(y) # сумма кодов второго слова
        if s1 + ord(y) == s:
            print('True')
            break
            #x = 012345
            #y = gfif (second)
        
        
        else:
            print('False')
            break
