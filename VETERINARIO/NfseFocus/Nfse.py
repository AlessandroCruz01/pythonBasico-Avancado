from tkinter import *

def limitar(p):
    if len(p) > 8:
        return False
    return True


root = Tk()
vcmd = root.register(func=limitar)
entry = Entry(root, validate='key', validatecommand=(vcmd, '%P'))
entry.pack()
root.mainloop()