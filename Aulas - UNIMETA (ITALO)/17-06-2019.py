try:
    from tkinter import *
except:
    from Tkinter import *

from tkinter import messagebox as mb
from tkinter import ttk

from threading import Thread
from time import strftime
class Tela(Thread):

    def __init__(self, root):
        self.frame = Frame(root, width=600, height=600, bg='blue')
        self.frame.place(x=50, y=10)

        self.bloco = Entry(self.frame, width=400)
        self.bloco.focus_force()  # MANTER O FOCO NO ENTRY
        self.bloco.place(x=0, y=0, height=400)

        self.btn = Button(root, text='CLICK', command=self.mostrar)
        self.btn.place(x=300, y=550)

        super(Tela, self).__init__()

    def run(self):
        self.lbr = Label(self.frame, bg='red')
        self.lbr.place(x=10, y=550)

        self.lbr['text'] = strftime('%H:%M:%S')  # formato de hora
        self.lbr['font'] = 'Helvita 10 bold'  # define a fonte do relogio
        self.lbr['foreground'] = 'blue'  # define a cor dos numeros
        self.lbr['bg'] = 'gray'  # define a cor do fundo bg e a abreviatura de background
        self.contador()

    def contador(self):
        self.agora = strftime('%H:%M:%S')
        if self.lbr['text'] != self.agora:
            self.lbr['text'] = self.agora
        self.lbr.after(100, self.contador)

    def mostrar(self):
        mb.showinfo('Aviso', self.bloco.get())

root = Tk()
root.geometry('800x800')
a = Tela(root)
a.start()
root.mainloop()
