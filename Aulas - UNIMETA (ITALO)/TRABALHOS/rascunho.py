# from tkinter import *
#
# def on_write(*args):
#     s = var.get()
#     if len(s) > 0:
#         if not s[-1].isdigit(): # retirar ultimo caracter caso nao seja digito
#             var.set(s[:-1])
#         else: # aproveitar apenas os primeiros 5 chars
#             var.set(s[:max_len])
#
# root = Tk()
# max_len = 5 # maximo num de caracteres
# var = StringVar()
# var.trace("w", on_write) # rastrear valor da variavel e executar funcao de validacao quando mudar
#
# entrada = Entry(root, textvariable=var)
# entrada.pack()
# root.mainloop()
#
# from tkinter import *
#
# janela2 = Tk()
# janela2.geometry('250x250+100+100')
#
# lb2 = Label(janela2, text='coloque seu nome')
#
# barrinha= Entry(janela2)
#
# barrinha.place(x=80,y=80)
#
# barrinha1= Entry(janela2)
#
# barrinha1.place(x=80,y=120)
#
# janela2.mainloop ()

from tkinter import *


class KeyboardEvent(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Eventos de teclado")
        self.master.geometry("250x50")

        # Label e Stringvar que vao exibir a tecla
        self.mensagem = StringVar()
        self.label = Label(self, textvariable=self.mensagem)
        self.mensagem.set("Aperte uma tecla")
        self.label.pack()

        # Fazendo os binding no frame
        self.master.bind("<KeyPress>", self.teclaPressionada)
        self.master.bind("<KeyRelease>", self.teclaLiberada)
        self.master.bind("<KeyPress-Alt_L>", self.altPressionado)
        self.master.bind("<KeyRelease-Alt_L>", self.altLiberado)

        mainloop()

    def teclaPressionada(self, event):
        self.mensagem.set("Tecla pressionada: " + event.char)

    def teclaLiberada(self, event):
        self.mensagem.set("Tecla solta: " + event.char)

    def altPressionado(self, event):
        self.mensagem.set("Alt pressionado")

    def altLiberado(self, event):
        self.mensagem.set("Alt liberado")


# Chamando a classe
KeyboardEvent()