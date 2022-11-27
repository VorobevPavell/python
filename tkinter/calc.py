from cgitb import text
import tkinter as tk
from unicodedata import digit 

def make_a_btn(digit):
    return tk.Button(win,text=digit ,bd = 5,command=lambda: add_digit(digit),font=('Arial,',15))

def make_a_op(op):
    return tk.Button(win,text=op ,bd = 5,fg = 'red',command=lambda: add_operation(op),font=('Arial,',15))

def make_a_calc_btn(op):
    return tk.Button(win,text=op ,bd = 5,fg = 'red',command=lambda: add_digit(op),font=('Arial,',15))

def add_digit(digit):
    value = calc.get() + str(digit)
    if value[0] == '0':
        value = value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value)

def add_operation(op):
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,value+op)






win = tk.Tk()
calc = tk.Entry(win,justify="right",font=('Arial,',15),width=15)
calc.insert(0,'0')
calc.grid(row=0,column=0,columnspan=4,sticky='we',padx=5)
make_a_btn('1').grid(column=0,row=1,sticky='snwe',padx=5,pady=5)
make_a_btn('2').grid(column=1,row=1,sticky='snwe',padx=5,pady=5)
make_a_btn('3').grid(column=2,row=1,sticky='snwe',padx=5,pady=5)
make_a_btn('4').grid(column=0,row=2,sticky='snwe',padx=5,pady=5)
make_a_btn('5').grid(column=1,row=2,sticky='snwe',padx=5,pady=5)
make_a_btn('6').grid(column=2,row=2,sticky='snwe',padx=5,pady=5)
make_a_btn('7').grid(column=0,row=3,sticky='snwe',padx=5,pady=5)
make_a_btn('8').grid(column=1,row=3,sticky='snwe',padx=5,pady=5)
make_a_btn('9').grid(column=2,row=3,sticky='snwe',padx=5,pady=5)
make_a_btn('0').grid(column=0,row=4,sticky='news',padx=5,pady=5)
make_a_op('+').grid(column = 3,row = 1 ,sticky='news',padx = 5,pady= 5)
make_a_op('-').grid(column = 3,row = 2 ,sticky='news',padx = 5,pady= 5)
make_a_op('/').grid(column = 3,row = 3 ,sticky='news',padx = 5,pady= 5)
make_a_op('*').grid(column = 3,row = 4 ,sticky='news',padx = 5,pady= 5)


make_a_calc_btn('=').grid(column = 2,row = 4 ,sticky='news',padx = 5,pady= 5)

win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(0,minsize=60)
win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)











win.title('CALCULATOR')
win.geometry('260x300+500+200')
win['bg'] = '#D7C29E'
tk.mainloop()