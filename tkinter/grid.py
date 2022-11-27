import tkinter as tk 
win = tk.Tk()
win.geometry('500x350+550+205')
win.config(bg='#f2f2f2')
for i in range(5): #  rows
    for j in range(2): # columns
        tk.Button(win,text=f'Button {i},{j}').grid(column= j,row=i,sticky='we')

tk.Button(win,text="EX BUTTON").grid(row=0,column=2,rowspan=5,sticky='sn')

win.columnconfigure(0,minsize=100)
win.columnconfigure(1,minsize=200)
tk.mainloop()