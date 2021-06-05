from tkinter import *
class Janela:
    def __init__(self,toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Oi!')
        self.botao.pack()
raiz=Tk()
raiz.geometry("500x500")

Janela(raiz)
raiz.mainloop()