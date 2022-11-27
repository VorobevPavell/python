import tkinter as tk 

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')


def delete_enrty():
    name.delete(0,tk.END)
    password.delete(0,tk.END)

def get_insert():
    name.delete(0,tk.END)
    name.insert(0,'hello')


def submit():
    n = name.get()
    p = password.get()
    delete_enrty()
    print(n)
    print(p)
win = tk.Tk()
win.geometry('500x350+550+205')
win.config(bg='black')
name = tk.Entry(win)
password = tk.Entry(win,show="*")
tk.Label(win,text="NAME").grid(column=0,row=0,sticky='w')
tk.Label(win,text="PASSWORD").grid(column=0,row=1,sticky='w')
btn1 = tk.Button(win,text='get!',command=get_entry).grid(column = 0,row = 2,sticky='we')
btn2 = tk.Button(win,text='delete',command=delete_enrty).grid(column = 1,row = 3,sticky='we')
btn3 = tk.Button(win,text='insert',command=get_insert).grid(column = 1,row = 2,sticky='we')
btn4 = tk.Button(win,text='submit',command=submit).grid(column = 0,row = 3,sticky='we')

name.grid(row = 0,column=1)
password.grid(row= 1,column= 1)
win.columnconfigure(0,minsize=150)
win.columnconfigure(1,minsize=200)
tk.mainloop()