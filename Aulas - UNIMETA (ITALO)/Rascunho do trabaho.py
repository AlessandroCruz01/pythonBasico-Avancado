try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()
root.geometry('700x500')

#------------------Funções---------------------

def cadastro_Pessoa():
    janela_pessoa = Toplevel(root)
    janela_pessoa.geometry('400x400')


    sa1 = Button(janela_pessoa, text="salvar", command='')
    sa1.place(x=100, y=350)


    esc = Entry(janela_pessoa, text='Nome')
    esc.place(x=10, y=300)

    es = Text(janela_pessoa, text='NOME', bg='black')
    es.place(x=40, y=200)

    cad = Label(janela_pessoa)
    cad.place(x=100,  y=100)

    sa2 = Button(janela_pessoa, text='Sair', command=janela_pessoa.destroy)
    sa2.place(x=200, y=350)

    janela_pessoa.mainloop()

#-----------------MENU-------------------

nomeWidget = Menu(root)
fileMenu = Menu(nomeWidget)
fileMenu1 = Menu(nomeWidget)
fileMenu2 = Menu(nomeWidget)

nomeWidget.add_cascade(label='Pessoa', menu=fileMenu)
fileMenu.add_command(label="Cadastrar", command=cadastro_Pessoa)
fileMenu.add_command(label="Alterar", command='')
fileMenu.add_command(label="Excluir", command='')

nomeWidget.add_cascade(label='Evento', menu=fileMenu1)
fileMenu1.add_cascade(label='Cadastrar', command='')
fileMenu1.add_command(label='Alterar', command='')
fileMenu1.add_command(label='Excluir', command='')

nomeWidget.add_cascade(label='Reunião', menu=fileMenu2)
fileMenu2.add_cascade(label='Cadastrar', command='')
fileMenu2.add_command(label='Alterar', command='')
fileMenu2.add_command(label='Excluir', command='')


root.config(menu=nomeWidget)
root.mainloop()