import tkinter as tk


root = tk.Tk()
root.title('my first GUI')
w = 400
h = 250
root.geometry(f"{w}x{h}+100+200")
root.maxsize(800,500)
root.minsize(200,125)
root.resizable(True,True)
root['bg'] = '#fafafa'
canvas = tk.Canvas(root, width= 400, height= 250)
tk.mainloop()
