try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from tkinter import messagebox as mb

from datetime import *
from time import strftime
import sqlite3

#-----------BANCO--------------#
conexao = sqlite3.connect('Agenda1.db')
conexao.cursor()
c = conexao
c.execute("""CREATE TABLE IF NOT EXISTS Pessoa (
                idpessoa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                fone1 TEXT NOT NULL,
                fone2 TEXT NOT NULL)""")

conexao.commit()

c.execute("""CREATE TABLE IF NOT EXISTS Evento (
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL,
                data_inicio TEXT NOT NULL,
                data_fim TEXT NOT NULL)""")
conexao.commit()

c.execute("""CREATE TABLE IF NOT EXISTS Reuniao (
                descricao TEXT NOT NULL,
                pauta TEXT NOT NULL,
                data_inicio TEXT NOT NULL,
                hora_inicio TEXT NOT NULL,
                data_final TEXT NOT NULL,
                hora_final TEXT NOT NULL)""")
conexao.commit()
conexao.close()


#------------------TELA PRINCIPAL--------------------#

root = Tk()
root.geometry('700x500')
root.title('MENU PRINCIPAL')
root.resizable(width=False, height=False) #NAO DEIXA ESPANDIR A TELA

#-------------------CLASSES--------------------------#

class Pessoa():
    def __init__(self, nome_p = '', fone1 = '', fone2 =''):
        self.nome_p = nome_p
        self.fone1 = fone1
        self.fone2 = fone2

        self.frame = Frame(root, width = 600, height = 500) #COM TOPLEVEL FICOU MAIS BONITO
        self.frame.place(x=50, y=10)
        self.titulo = Label(self.frame, text='CADASTRO DE PESSOA')
        self.titulo['font'] = ('Arial', '12', 'bold')
        self.titulo.place(x=230, y=50)

        self.nome_p = Label(self.frame, text='Nome: ')
        self.nome_p.place(x=20, y=100)
        self.n_nome = Entry(self.frame, width=60)
        self.n_nome.focus_force() #MANTER O FOCO NO ENTRY
        self.n_nome.place(x=100, y=100)

        self.fone1 = Label(self.frame, text='Telefone 1: ')
        self.fone1.place(x=20, y=150)
        self.n_fone1 = Entry(self.frame, width=60)
        self.n_fone1.focus_force()
        self.n_fone1.place(x=100, y=150)

        self.fone2 = Label(self.frame, text='Telefone 2: ')
        self.fone2.place(x=20, y=200)
        self.n_fone2 = Entry(self.frame, width=60)
        self.n_fone2.focus_force()
        self.n_fone2.place(x=100, y=200)


        self.sv = Button(self.frame, width=5, text='SALVAR', fg='green', command=self.salvar)
        self.sv.place(x=100, y=10)

        self.bs = Button(self.frame, width=5, text='BUSCA', fg='green', command=self.busca)
        self.bs.place(x=200, y=10)

        self.al = Button(self.frame, width=5, text='ALTERAR', fg='green', command=self.alterar)
        self.al.place(x=300, y=10)

        self.dl = Button(self.frame, width=5, text='EXCLUIR', fg='green', command=self.delete)
        self.dl.place(x=400, y=10)

        self.sr = Button(self.frame, width=5, text='SAIR', fg='red', command=self.frame.destroy)
        self.sr.place(x=250, y=300)

    def salvar(self):
        self.nome_p = self.n_nome.get()
        self.fone1 = self.n_fone1.get()
        self.fone2 = self.n_fone2.get()

        con = sqlite3.connect('Agenda1.db')
        cursor = con.cursor()

        cursor.execute('''
                        INSERT INTO pessoa (nome, fone1, fone2)
                        VALUES ('%s' ,' %s' ,' %s')
                        ''' %(self.nome_p, self.fone1, self.fone2))
        con.commit()

        con.close()
        mb.showinfo('Salvo', 'CLIENTE Salvo!')
        self.n_nome.delete(0, END)
        self.n_fone1.delete(0, END)
        self.n_fone2.delete(0, END)


    def busca(self):
        con = sqlite3.connect('Agenda1.db')
        cursor = con.cursor()
        self.au = 'select nome,fone1,fone2 from Pessoa where nome = (?)'
        self.x = self.n_nome.get()
        cursor.execute(self.au, [self.n_nome.get()])
        busca = cursor.fetchall()
        for  i in busca:
            if self.n_nome.get() in i:

                self.n_nome.delete(0, END)
                self.n_nome.insert(END, i[0])
                self.backup = i[0]
                self.n_fone1.insert(END, i[1])
                self.n_fone2.insert(END, i[2])

        con.commit()
        con.close()

        print('busca feita')


    def alterar(self):
        print(self.backup)
        self.nome_p = self.n_nome.get()
        self.fone1 = self.n_fone1.get()
        self.fone2 = self.n_fone2.get()

        con = sqlite3.connect('Agenda1.db')
        cursor = con.cursor()
        cursor.execute(f"UPDATE Pessoa SET nome ='{self.nome_p}', fone1 = '{self.fone1}',fone2 ='{self.fone2}'where nome ='{self.backup}';")

        con.commit()
        con.close()
        self.n_nome.delete(0, END)
        self.n_fone1.delete(0, END)
        self.n_fone2.delete(0, END)

    def delete(self):
        con = sqlite3.connect('Agenda1.db')
        cursor = con.cursor()

        self.de = "delete from Pessoa where nome = (?)"
        cursor.execute(self.de, [self.n_nome.get()])
        busca = cursor.fetchall()

        for i in busca:
            if self.n_nome.get() in i:

                self.n_nome.delete(0, END)

        con.commit()

        con.close()

        self.n_nome.delete(0, END)
        self.n_fone1.delete(0, END)
        self.n_fone2.delete(0, END)

        print('deletado')

class Evento():
    def __init__(self, nome_e='', tipo = '', dtai='', dtaf=''):
        self.nome_e = nome_e
        self.tipo = tipo
        self.dtai = dtai
        self.dtaf = dtaf



        self.frame = Frame(root, width = 600, height = 500)
        self.frame.place(x=50, y=10)
        self.titulo = Label(self.frame, text='CADASTRO DE PRODUTO: ')
        self.titulo['font'] = ('Arial', '12', 'bold')
        self.titulo.place(x=100, y=50)

        self.nome_e = Label(self.frame, text='Nome: ')
        self.nome_e.place(x=20, y=100)
        self.n_nome = Entry(self.frame, width=30)
        self.n_nome.focus_force() #MANTER O FOCO NO ENTRY
        self.n_nome.place(x=100, y=100)

        self.tipo = Label(self.frame, text='COD. FABRICANTE ')
        self.tipo.place(x=20, y=150)
        self.n_tipo = Entry(self.frame, width=30)
        self.n_tipo.focus_force()
        self.n_tipo.place(x=100, y=150)

        self.dtai = Label(self.frame, text='QTD: ')
        self.dtai.place(x=20, y=200)
        self.n_dtai = Entry(self.frame, width=30)
        self.n_dtai.focus_force()
        self.n_dtai.place(x=100, y=200)

        self.dtaf = Label(self.frame, text='PREÇO ')
        self.dtaf.place(x=20, y=250)
        self.n_dtaf = Entry(self.frame, width=30)
        self.n_dtaf.focus_force()
        self.n_dtaf.place(x=100, y=250)

        self.sv = Button(self.frame, width=5, text='SALVAR', fg='green', command=self.salvar)
        self.sv.place(x=100, y=10)

        self.bs = Button(self.frame, width=5, text='BUSCA', fg='green', command=self.busca)
        self.bs.place(x=200, y=10)

        #self.al = Button(self.frame, width=5, text='ALTERAR', fg='green', command=self.alterar)
        #self.al.place(x=300, y=10)

        self.dl = Button(self.frame, width=5, text='EXCLUIR', fg='green', command=self.delete)
        self.dl.place(x=300, y=10)

        self.sr = Button(self.frame, width=5, text='SAIR', fg='red', command=self.frame.destroy)
        self.sr.place(x=250, y=300)

    def salvar(self):
        try:
            self.nome_e = self.n_nome.get()
            self.tipo = self.n_tipo.get()
            self.dtai = self.n_dtai.get()
            self.dtaf = self.n_dtaf.get()


            con = sqlite3.connect('Agenda1.db')
            cursor = con.cursor()

            cursor.execute('''
                            INSERT INTO Evento (nome, tipo, data_inicio, data_fim)
                            VALUES ('%s' ,' %s' ,' %s' , '%s')
                            ''' %(self.nome_e,self.tipo, self.dtai, self.dtaf))
            con.commit()
            print('Concluido')
            mb.showinfo('SALVO', 'SALVO COM SUCESSO')
            con.close()
            self.n_nome.delete(0, END)
            self.n_tipo.delete(0, END)
            self.n_dtai.delete(0, END)
            self.n_dtaf.delete(0, END)
        except:
            mb.showerror('ERRO', 'NAO SALVO')
            self.n_nome.delete(0, END)
            self.n_tipo.delete(0, END)
            self.n_dtai.delete(0, END)
            self.n_dtaf.delete(0, END)




    def busca(self):
        self.n_tipo.delete(0, END)
        self.n_dtai.delete(0, END)
        self.n_dtaf.delete(0, END)
        con = sqlite3.connect('Agenda1.db')
        cursor = con.cursor()
        self.au = 'select nome,tipo,data_inicio,data_fim from Evento where nome = (?)'
        self.x = self.n_nome.get()
        cursor.execute(self.au, [self.n_nome.get()])
        busca = cursor.fetchall()
        for i in busca:
            if self.n_nome.get() in i:

                self.n_nome.delete(0, END)
                self.n_nome.insert(END, i[0])
                self.backup = i[0]
                self.n_tipo.insert(END, i[1])
                self.n_dtai.insert(END, i[2])
                self.n_dtaf.insert(END, i[3])

        con.commit()
        con.close()

        mb.showinfo('busca', 'busca feita')




    def alterar(self):
        print(self.backup)
        self.nome_e = self.n_nome.get()
        self.dtai = self.n_dtai.get()
        self.dtaf = self.n_dtaf.get()

        con = sqlite3.connect('Agenda1.db')
        cursor = con.cursor()
        cursor.execute(f"UPDATE Evento SET nome ='{self.nome_e}',tipo = '{self.tipo}',  data_inicio = '{self.dtai}',data_fim ='{self.dtaf}'where nome ='{self.backup}';")

        con.commit()
        con.close()
        self.n_nome.delete(0, END)
        self.n_tipo.delete(0, END)
        self.n_dtai.delete(0, END)
        self.n_dtaf.delete(0, END)

    def delete(self):
        con = sqlite3.connect('Agenda1.db')
        cursor = con.cursor()

        self.de = "delete from Evento where nome = (?)"
        cursor.execute(self.de, [self.n_nome.get()])
        busca = cursor.fetchall()

        for i in busca:
            if self.n_nome.get() in i:

                self.n_nome.delete(0, END)

        con.commit()
        con.close()

        self.n_nome.delete(0, END)
        self.n_tipo.delete(0, END)
        self.n_dtai.delete(0, END)
        self.n_dtaf.delete(0, END)

        print('deletado')



# class Reuniao():
#     def __init__(self, desc='', pauta='', dta_i='', hra_i='', dta_f='', hra_f=''):
#         self.desc = desc
#         self.pauta = pauta
#         self.dta_i = dta_i
#         self.hra_i = hra_i
#         self.dta_f = dta_f
#         self.hra_f = hra_f
#
#         self.frame = Frame(root, width=600, height=500)
#         self.frame.place(x=50, y=10)
#         self.titulo = Label(self.frame, text='EVENTO: ')
#         self.titulo['font'] = ('Arial', '12', 'bold')
#         self.titulo.place(x=100, y=50)
#
#         self.desc = Label(self.frame, text='Descição: ')
#         self.desc.place(x=20, y=100)
#         self.n_desc = Entry(self.frame, width=30)
#         self.n_desc.focus_force()  # MANTER O FOCO NO ENTRY
#         self.n_desc.place(x=100, y=100)
#
#         self.pauta = Label(self.frame, text='Pauta:  ')
#         self.pauta.place(x=20, y=150)
#         self.n_pauta = Entry(self.frame, width=30)
#         self.n_pauta.focus_force()
#         self.n_pauta.place(x=100, y=150)
#
#         self.dta_i = Label(self.frame, text='Data inicio: ')
#         self.dta_i.place(x=20, y=200)
#         self.n_dta_i = Entry(self.frame, width=30)
#         self.n_dta_i.focus_force()
#         self.n_dta_i.place(x=100, y=200)
#
#         self.hra_i = Label(self.frame, text='Hora inicio: ')
#         self.hra_i.place(x=20, y=250)
#         self.n_hra_i = Entry(self.frame, width=30)
#         self.n_hra_i.focus_force()
#         self.n_hra_i.place(x=100, y=250)
#
#         self.dta_f = Label(self.frame, text='Data inicio: ')
#         self.dta_f.place(x=20, y=300)
#         self.n_dta_f = Entry(self.frame, width=30)
#         self.n_dta_f.focus_force()
#         self.n_dta_f.place(x=100, y=300)
#
#         self.hra_f = Label(self.frame, text='Hora Fim: ')
#         self.hra_f.place(x=20, y=350)
#         self.n_hra_f = Entry(self.frame, width=30)
#         self.n_hra_f.focus_force()
#         self.n_hra_f.place(x=100, y=350)
#
#         self.sv = Button(self.frame, width=5, text='SALVAR', fg='green', command=self.salvar)
#         self.sv.place(x=100, y=10)
#
#         self.bs = Button(self.frame, width=5, text='BUSCA', fg='green', command=self.busca)
#         self.bs.place(x=200, y=10)
#
#         self.al = Button(self.frame, width=5, text='ALTERAR', fg='green', command=self.alterar)
#         self.al.place(x=300, y=10)
#
#         self.dl = Button(self.frame, width=5, text='EXCLUIR', fg='green', command=self.delete)
#         self.dl.place(x=400, y=10)
#
#         self.sr = Button(self.frame, width=5, text='SAIR', fg='red', command=self.frame.destroy)
#         self.sr.place(x=250, y=400)
#
#     def salvar(self):
#         self.pauta = self.n_pauta.get()
#         self.desc = self.n_desc.get()
#         self.dta_i = self.n_dta_i.get()
#         self.hra_i = self.n_hra_i.get()
#         self.dta_f = self.n_dta_f.get()
#         self.hra_f = self.n_hra_f.get()
#
#         con = sqlite3.connect('Agenda1.db')
#         cursor = con.cursor()
#
#         cursor.execute('''
#                         INSERT INTO Reuniao (pauta, descricao,data_inicio, hora_inicio, data_final, hora_final)
#                         VALUES ('%s' ,' %s' ,' %s', '%s', '%s', '%s')
#                         ''' %(self.pauta, self.desc, self.dta_i, self.hra_i, self.dta_f, self.hra_f))
#         con.commit()
#         con.close()
#
#
#
#         self.n_pauta.delete(0, END)
#         self.n_desc.delete(0, END)
#         self.n_dta_i.delete(0, END)
#         self.n_dta_f.delete(0, END)
#         self.n_hra_i.delete(0, END)
#         self.n_hra_f.delete(0, END)
#
#
#     def busca(self):
#         con = sqlite3.connect('Agenda1.db')
#         cursor = con.cursor()
#         self.au = 'select pauta, descricao, data_inicio, hora_inicio, data_final, data_final from Reuniao where pauta = (?)'
#         self.x = self.n_desc.get()
#         cursor.execute(self.au, [self.n_desc.get()])
#         busca = cursor.fetchall()
#         for i in busca:
#             if self.n_desc.get() in i:
#
#                 self.n_desc.delete(0, END)
#                 self.n_desc.insert(END, i[0])
#                 self.backup = i[0]
#                 self.n_pauta.insert(END, i[1])
#                 self.n_dta_i.insert(END, i[2])
#                 self.n_hra_i.insert(END, i[3])
#                 self.n_dta_f.insert(END, i[4])
#                 self.n_hra_f.insert(END, i[5])
#
#         con.commit()
#         con.close()
#
#
#
#
#     def alterar(self):
#         print(self.backup)
#         self.pauta = self.n_pauta.get()
#         self.desc = self.n_desc.get()
#         self.dta_i = self.n_dta_i.get()
#         self.hra_i = self.n_hra_i.get()
#         self.dta_f = self.n_dta_f.get()
#         self.hra_f = self.n_hra_f.get()
#
#         con = sqlite3.connect('Agenda1.db')
#         cursor = con.cursor()
#         cursor.execute(f"UPDATE Reuniao SET pauta ='{self.pauta}', descricao = '{self.desc}',data_inicio ='{self.dta_i}', hora_inicio = '{self.hra_i}',data_final = '{self.dta_f}', hora_final = {self.hra_f}', where nome ='{self.backup}';")
#
#         con.commit()
#         con.close()
#         self.n_pauta.delete(0, END)
#         self.n_desc.delete(0, END)
#         self.n_dta_i.delete(0, END)
#         self.n_dta_f.delete(0, END)
#         self.n_hra_i.delete(0, END)
#         self.n_hra_f.delete(0, END)
#
#     def delete(self):
#         try:
#             con = sqlite3.connect('Agenda1.db')
#             cursor = con.cursor()
#
#             self.de = "delete from Evento where nome = (?)"
#             cursor.execute(self.de, [self.n_pauta.get()])
#             busca = cursor.fetchall()
#
#             for i in busca:
#                 if self.n_pauta.get() in i:
#
#                     self.n_pauta.delete(0, END)
#
#             con.commit()
#             con.close()
#
#             self.n_pauta.delete(0, END)
#             self.n_desc.delete(0, END)
#             self.n_dta_i.delete(0, END)
#             self.n_dta_f.delete(0, END)
#             self.n_hra_i.delete(0, END)
#             self.n_hra_f.delete(0, END)
#
#
#         except:
#             print('NAO FOI POSSIVEL DELETAR')

#------------------EXECUTAR------------------#

menuwidget = Menu(root)
filemenu = Menu(menuwidget)


menuwidget.add_cascade(label = 'CADASTROS', menu = filemenu)
filemenu.add_command(label = 'PESSOA', command=Pessoa)
filemenu.add_command(label = 'CADASTRO DE PRODUTO' , command=Evento)
#filemenu.add_command(label ='REUNIÃO', command=Reuniao)
filemenu.add_command(label = 'SAIR', command=root.destroy)


root.config(menu=menuwidget)

# b1 = Button(root, text='teste', command =Pessoa)
# b1.pack()
#
# b2 = Button(root, text='teste', command =Evento)
# b2.pack()
#
# b3 = Button(root, text='teste', command =Reuniao)
# b3.pack()

root.mainloop()