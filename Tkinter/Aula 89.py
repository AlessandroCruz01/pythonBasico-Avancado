class Calculadora(object):
    def __init__(self, root):
        #coloca a entrada de texto
        self.form = Entry(root)
        self.form.pack()

        #criando botoes
        self.calc = Button(root,text="calcule", command=self.calcular)
        self.calc.pack()

        #Texto das formulas
        self.resultado = Label(root, text="calcule", fg='Blue' )#cor da fonte
        self.resultado.pack()


        #criando varios botoes
        botoes = ('1','2','3','4','5','6','7','8','9','0')
        for i in botoes:
            a = Button(root,text=i,  fg="red")
            a.pack(side = LEFT)#side - indica o tipo de organização dos botoes por exemplo LEFT(esquerda)


    def calcular(self):
        self.resultado['text'] = self.form.get()#get pega a informação passada pelos usuarios no entrys
        self.resultado['fg'] = ('green')

#sintaxe básica para Tkinter
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()
Calculadora(root)
root.geometry('300x300')

root.mainloop()