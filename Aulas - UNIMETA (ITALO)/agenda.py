# -*- coding: UTF-8 -*-

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

import calendar
import sys
from random import randint
from threading import Thread
from tkinter import messagebox as ms
import sqlite3
from datetime import time


class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('Agenda01.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute('''create table if not exists Pessoa (
                     idpessoa integer primary key autoincrement,
                     nome text,
                     fone1 text,
                     fone2 text)''')
        self.conexao.commit()

        c.execute('''create table if not exists Evento (
                     nome text,
                     data_inicio text,
                     data_fim text)''')
        self.conexao.commit()

        c.execute('''create table if not exists Reuniao (
                     descricao text,
                     pauta text,
                     data_inicio text,
                     hora_inicio text,
                     data_final text,
                     hora_final)''')
        self.conexao.commit()
        c.close()


class Pessoa():
    def __init__(self, nome_p, fone1, fone2):
        self.nome_p = nome_p
        self.fone1 = fone1
        self.fone2 = fone2

class Evento():
    def __init__(self, nome_e, dtai, dtaf):
        self.nome_e = nome_e
        self.dtai = dtai
        self.dtaf = dtaf

class Reuniao():
    def __init__(self, desc, pauta, dta_i, hra_i, dta_f, hra_f):
        self.desc = desc
        self.pauta = pauta
        self.dta_i = dta_i
        self.hra_i = hra_i
        self.dta_f = dta_f
        self.hra_f = hra_f

def cadastrar_pessoa():
    cad_p = Toplevel(root)
    cad_p.geometry('700x700')
    cad_p.title('Pessoa')

    #CONTAINER DO TITULO
    container1 = Frame(cad_p)
    container1['pady'] = 10
    container1.pack()

    #CONTAINER PARA O NOME
    container2 = Frame(cad_p)
    container2['padx'] = 10
    container2['pady'] = 5
    container2.pack()

    #CONTAINER DOS TELEFONES
    container3 = Frame(cad_p)
    container3['padx'] = 10
    container3['pady'] = 5
    container3.pack()

    container4 = Frame(cad_p)
    container4['padx'] = 10
    container4['pady'] = 5
    container4.pack()


    #USANDO O CONTAINER 1
    titulo = Label(container1, text="Cadastro: ")
    titulo['font'] = ('calibri', '9', 'bold')
    titulo.pack()

    #USANDO O CONTAINER 2
    nome = Label(container2, text = 'NOME: ', font='Arial 10', width = 20)
    nome.pack(side=LEFT)


    textnome = Entry(container2)
    textnome['width'] = 70
    textnome['font'] = 'Arial 10'
    textnome.pack(side = LEFT)

    #CONTAINER 3 E 4
    tel1 = Label(container3, text= 'TELEFONE (1): ', font='Arial 10', width = 20)
    tel1.pack(side=LEFT)

    tel1text = Entry(container3)
    tel1text['width'] = 70
    tel1text['font'] = 'Arial 10'
    tel1text.pack(side = LEFT)

    tel2 = Label(container4, text='TELEFONE (2): ', font='Arial 10', width=20)
    tel2.pack(side=LEFT)

    tel2text = Entry(container4)
    tel2text['width'] = 70
    tel2text['font'] = 'Arial 10'
    tel2text.pack(side=LEFT)

    sv = Button(cad_p, width=60, text='SALVAR', fg='black', bg='green', command='')
    sv.place(x=100, y=500)

    sa = Button(cad_p, width=60,text='SAIR', fg='red', command=cad_p.destroy )
    sa.place(x=100, y=600)




    cad_p.mainloop()


def alterar_pessoa():
    pass

root = Tk()
root.geometry('800x800')
root.title('Agenda')


menuwidget = Menu(root)
filemenu = Menu(menuwidget)
filemenu1 = Menu(menuwidget)
filemenu2 = Menu(menuwidget)

menuwidget.add_cascade(label = 'CADASTROS', menu = filemenu)
filemenu.add_command(label = 'PESSOA', command=cadastrar_pessoa)
filemenu.add_command(label = 'EVENTO' , command='')
filemenu.add_command(label ='REUNIÃO', command='')

menuwidget.add_cascade(label = 'PESQUISA', menu = filemenu1 )
filemenu1.add_command(label = 'POR NOME', command='')
filemenu1.add_command(label = 'POR EVENTO' , command='')
filemenu1.add_command(label ='POR REUNIÃO', command='')

menuwidget.add_cascade(label = 'SAIR', menu = filemenu2)
filemenu2.add_command(label = 'Cadastrar', command='')
filemenu2.add_command(label = 'Alterar' , command='')
filemenu2.add_command(label ='Excluir', command='')



root.config(menu=menuwidget)
root.mainloop()