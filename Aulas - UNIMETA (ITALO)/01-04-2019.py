try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from threading import Thread
from time import sleep

clicado = False


class Some(Thread):
    def __init__(self, b):
        self.b = b
        super(Some, self).__init__()

    def run(self):
        sleep(4)
        if not clicado:
            self.b.destroy()


x = 200


def mover():
    global clicado
    global x
    clicado = True
    x -= 10
    b1.place(x=x, y=10)


root = Tk()
root.geometry("300x300")

b1 = Button(root, text='clique', fg="red", command=mover)
b1.place(x=x, y=10)
t = Some(b1)
t.start()

root.mainloop()
