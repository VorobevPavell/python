import tkinter as tk
from turtle import bgcolor 
win = tk.Tk()
count = 0
n = 0
#functions

def do_disable(): # делает кнопку "active/disable" неактивной при каждом четном нажатии
    global count
    count +=1
    if count % 2 == 0:
        btn_2['state'] = tk.DISABLED
    if count % 2 ==1:
        btn_2['state'] = tk.NORMAL



#Функция,чтобы получить случайные цвета.
import random
def change_color():
    global color
    for i in range(100):
        color = '#' + ''.join(random.choice('ABCDEF0123456789') for i in range(6)) # присоединяет к # 6 символов
        win.config(bg=color)
    


#Функция, которая добавляет количество нажатий на кнопку

def add_count():
    global n 
    n += 1
    btn_2['text'] = f'Active/Unactive : {n}'







#buttons

btn_1 = tk.Button(win,text = 'Push it',
command= do_disable)
btn_2 = tk.Button(win,
text=f'Active/Unactive : {n}',
command=add_count)

btn_3 = tk.Button(win,text='Change background color',
command=change_color)

btn_4 = tk.Button(win,text='add_label',
command=lambda: tk.Label(win,text='label_text').pack())  #  Реализовал появление Label, при нажатии на кнопку лямбда-функцией

btn_1.pack()
btn_2.pack()
btn_3.pack()
btn_4.pack()
win.title('BUTTONS N LABELS')
win.geometry('300x250+550+200')
win.resizable(False,False)
tk.mainloop()