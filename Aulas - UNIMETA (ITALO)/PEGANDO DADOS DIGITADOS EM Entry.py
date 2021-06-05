from tkinter import *

# Componentes da Janela
janela = Tk()
janela.title("EmagreciPet")
janela.geometry('300x500')
janela.resizable(False, False)

# Variáveis
var = StringVar()
varChoose = StringVar()
# Funções Botão
def pegar_nome():
    content = var.get()
    print(content)
# Nome do Pet
lbl1 = Label(janela, text="Nome do seu pet: ")
lbl1.pack(anchor=NW)
# Digita o nome do Pet
Entry1 = Entry(janela, bd = 2, textvariable = var)
Entry1.pack(anchor=SW)
Entry1.get()
# Botão para confirmar nome do Pet
btn1 = Button(janela, text='Confirmar nome', command=pegar_nome)
btn1.place(x=135, y=17)
# Caixa de seleção Sexo Macho
rBtn1 = Radiobutton(janela, text='Macho', variable=varChoose, value=1)
rBtn1.pack(anchor = W)
rBtn1.select()
# Caixa de seleção Sexo Fêmea
rBtn2 = Radiobutton(janela, text='Femea', variable=varChoose, value=2)
rBtn2.pack(anchor = W)
# Nome do pet digitado na tela
lbl2 = Label(janela, text="", textvariable=var)
lbl2.pack(anchor=NW)


# Fim do programa
janela.mainloop()