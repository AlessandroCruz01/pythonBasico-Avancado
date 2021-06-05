#sintaxe básica para Tkinter
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()
root.title('calculadora')
root.geometry("800x600")
#root.wm_iconbitmap("#nome do icone(detalhe: o icone deve estar na mesma pagina do codido)")



#coloca a entrada de texto
form = Entry(root)
form.pack()

#criando botoes
calc = Button(root,text="calcule")
calc.pack()

#Texto das formulas
resultado = Label(root,text="Resultado", fg = "Blue" )#cor da fonte
resultado.pack()





root.mainloop()