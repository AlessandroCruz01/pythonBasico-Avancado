class MeuBotao(object):
    def __init__(self, x,y,text,command,widget):
        self.b = Button(widget, text=text, command=command)
        self.b.place(x=x, y=y)

    def mover(self, x, y):
        self.b.place(x=x, y=y)


try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()
root.geometry("300x300")





root.mainloop()