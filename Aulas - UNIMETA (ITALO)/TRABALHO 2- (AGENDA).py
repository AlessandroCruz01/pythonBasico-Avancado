try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from datetime import *

import sqlite3

#-----------BANCO--------------#

class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('Agenda.db')
        #self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table Pessoa (
                     nome text,
                     fone1 text,
                     fone2 text)""")
        self.conexao.commit()

        c.execute("""create table Evento (
                             nome text,
                             tipo text,
                             data_inicio text,
                             data_fim text)""")
        self.conexao.commit()

        c.execute("""create table Reuniao (
                             descricao text,
                             pauta text,
                             data_inicio text,
                             hora_inicio text,
                             data_final text,
                             hora_final)""")
        self.conexao.commit()

#------------------TELA PRINCIPAL--------------------#

class Pessoa():
    pass

class Evento():
    def __init__(self, nome, tipo, dta_ini, dta_fim):
        pass

class Reuniao(object):
    def __init__(self, desc, pauta, data_inicio, hra_inicio, data_fim, hra_fim):
        pass

class Calendario(object):
    pass

class Principal(Pessoa):
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x500')

        self.c = Canvas()
        self.c.pack()

        self.nomeWidget = Menu(self.root)
        self.fileMenu = Menu(self.nomeWidget)
        self.fileMenu1 = Menu(self.nomeWidget)
        self.fileMenu2 = Menu(self.nomeWidget)

        self.lb = Listbox()
        self.lb.pack(side=LEFT, expand=TRUE, fill='both')

        self.sb = Scrollbar()
        self.sb.pack(side=RIGHT, fill='y')
        self.sb.configure(command=self.lb.yview)
        self.lb.configure(yscrollcommand=self.sb.set)
        # for i in range(100):
        #     self.lb.insert(END,i)

        self.ima = PhotoImage(file='cal.png')
        self.i = self.c.create_image(300,300, image=self.ima)

        self.t = self.c.create_text(200, 35, text='Texto', font='Arial 22')

        self.nomeWidget.add_cascade(label='Pessoa', menu=self.fileMenu)
        self.fileMenu.add_command(label="Cadastrar", command='')
        self.fileMenu.add_command(label="Alterar", command='')
        self.fileMenu.add_command(label="Exluir", command='')

        self.nomeWidget.add_cascade(label='Evento', menu=self.fileMenu1)
        self.fileMenu1.add_cascade(label='Cadastrar', command='')
        self.fileMenu1.add_command(label='Alterar', command='')
        self.fileMenu1.add_command(label='Excluir', command='')

        self.nomeWidget.add_cascade(label='Reunião', menu=self.fileMenu2)
        self.fileMenu2.add_cascade(label='Cadastrar', command='')
        self.fileMenu2.add_command(label='Alterar', command='')
        self.fileMenu2.add_command(label='Excluir', command='')

        self.root.config(menu=self.nomeWidget)

banco = Banco()

root=Tk()
Principal(root)
root.mainloop()