from tkinter import*
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect("eletronica.db")
cursor = conn.cursor()
def create_Tabela():
    cursor.execute("""CREATE TABLE IF NOT EXISTS pessoa(
                         idcontato INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                         nome TEXT NOT NULL,
                         fone1 TEXT NOT NULL,
                         fone2 TEXT NOT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS evento(
                        idevento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        evento TEXT NOT NULL,
                        tipo TEXT NOT NULL,
                        data_inicio DATE NOT NULL,
                        data_final DATE NOT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS reuniao(
                    idreuniao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     descricao TEXT NOT NULL,
                     pauta TEXT NOT NULL,
                     dat_inicio DATE NOT NULL,
                     hora_inicio TIME NOT NULL,
                     dat_final DATE NOT NULL,
                     hora_final TIME NOT NULL)""")
    conn.commit()
    conn.close()
    return conn
create_Tabela()
root = Tk()
root.title("Agenda Eletronica")
root.geometry("500x500")
root.resizable(width=False,height=False)
class Pessoa():
    def __init__(self,nome='',fone1='',fone2=''):
       self.nome = nome
       self.fone1 = fone1
       self.fone2 = fone2
       
       self.frame =Frame(root, width=400, height=400)
       self.frame.place(x=50,y=50)
       self.titulo1 = Label(self.frame, text="Contato")
       self.titulo1["font"] = ("Calibri", "12", "bold")
       self.titulo1.place(x=100,y=50)
       
       self.nome = Label(self.frame, text='Nome :')
       self.nome.place(x=50, y=100)
       self.n_nome = Entry(self.frame,width=30)
       self.n_nome.focus_force()
       self.n_nome.place(x=100, y=100)

       self.fone1 = Label(self.frame, text='Celular:')
       self.fone1.place(x=45, y=130)
       self.n_fone1 = Entry(self.frame)
       self.n_fone1.place(x=100, y=130)

       self.fone2 = Label(self.frame, text="Telefone:")
       self.fone2.place(x=35, y=160)
       self.n_fone2 = Entry(self.frame)
       self.n_fone2.place(x=100, y= 160)

       self.botao = Button(self.frame,text='Salvar', command=self.salvar)
       self.botao.place(x=20, y=200, width=100, height=25)

       self.botao1 = Button(self.frame,text='Pesquisar', command=self.mostra)
       self.botao1.place(x=130, y=200, width=100, height=25)

       self.botao2 = Button(self.frame,text='Alterar', command=self.update)
       self.botao2.place(x=235, y=200, width=100, height=25)

       self.botao3 = Button(self.frame,text='Excluir', command=self.delete_contato)
       self.botao3.place(x=235, y=250, width=100, height=25)
     
    def salvar(self):
       
       self.nome = self.n_nome.get()
       self.fone1 = self.n_fone1.get()
       self.fone2 = self.n_fone2.get()
       conn = sqlite3.connect('eletronica.db')
       cursor = conn.cursor()
       self.lok = "select nome,fone1, fone2 from pessoa where nome = (?)"
       cursor.execute(self.lok, [self.n_nome.get()])
       self.lok = cursor.fetchall()
       self.tes_fone1 = len(self.n_fone1.get())
       self.tes_fone2 = len(self.n_fone2.get())
       fone = f'({self.fone1[0:2]}){self.fone1[2:6]} - {self.fone1[6:]}'
       fon = f'({self.fone2[0:2]}){self.fone2[2:6]} - {self.fone2[6:]}'
       if self.lok:
            messagebox.showerror("Falha no Cadastro","Contato ja Existe")
            self.n_nome.delete(0,255)
            self.n_fone1.delete(0, 255)
            self.n_fone2.delete(0,255)
       elif self.tes_fone1 != 11 or self.tes_fone2 != 11:
           try:
                val= int(self.n_fone1.get())
                if not 0 >= n_fone1.get() >=11:
                    raise ValueError("Dados do Formato Errado")
           except ValueError as e:
                print("Informe Apenas Numeros",e)
           else:
                print("else")          
           messagebox.showerror("Falha no Cadastro","Dados incorretos")

       else:
            conn = sqlite3.connect('eletronica.db')
            cursor = conn.cursor()
            cursor.execute("""
                            INSERT INTO pessoa (nome,fone1,fone2)
                            VALUES ("%s","%s","%s")
                            """ % (self.nome,fone,fon))
            

            conn.commit()
            messagebox.showerror(" Cadastro","Cadastro Realizado")
            conn.close()
            self.n_nome.delete(0, END)
            self.n_fone1.delete(0, END)
            self.n_fone2.delete(0, END)
    def update(self):
        try:
            global n_nome, n_fone1, n_fone2
            print(self.backup)
            self.nome = self.n_nome.get()
            self.fone1 = self.n_fone1.get()
            self.fone2 = self.n_fone2.get()

            conn = sqlite3.connect('eletronica.db')
            cursor = conn.cursor()
            cursor.execute(f"UPDATE pessoa SET nome ='{self.nome}', fone1 = '{self.fone1}',fone2 = '{self.fone2}' where nome = '{self.backup}';")

            conn.commit()
            messagebox.showerror("Alterar Dados","Todos Dados Foram Alterado")
            conn.close()
            self.n_nome.delete(0, END)
            self.n_fone1.delete(0, END)
            self.n_fone2.delete(0, END)
            return "Contato atulizado"
        except:
            return "Não foi possivel atualizar"
    def mostra(self):
        try:
            self.n_fone1.delete(0,END)
            self.n_fone2.delete(0,END)
            conn = sqlite3.connect('eletronica.db')
            cursor = conn.cursor()
            self.au = "select nome,fone1, fone2 from pessoa where nome = (?)"
            self.x = self.n_nome.get()
            cursor.execute(self.au, [self.n_nome.get()])
            busca = cursor.fetchall()
            for i in busca:
                if self.n_nome.get() in i:

                    self.n_nome.delete(0, END)
                    self.n_nome.insert(END, i[0])
                    self.backup = i[0]
                    self.n_fone1.insert(END,i[1])
                    self.n_fone2.insert(END, i[2])

            conn.commit()
            conn.close()
            return "Busca realizada"
        except:
            return "Ocorreu um erro durante a busca"
    
    def delete_contato(self):
       try:
           conn = sqlite3.connect('eletronica.db')
           cursor = conn.cursor()
           self.te ="delete from pessoa where nome = (?)"
           cursor.execute(self.te,[self.n_nome.get()])
           busca = cursor.fetchall()
           for i in busca:
               if self.nome.get() in i:

                    self.nome.delete(0, END)
           conn.commit()
           messagebox.showerror("Deletar Dados","Todos Dados Foram Deletados")
           conn.close()
           self.n_nome.delete(0, END)
           self.n_fone1.delete(0, END)
           self.n_fone2.delete(0, END)
           return " Excluido com sucesso"
       except:
           return "Erro na exclusao "
            
class Evento:
    def __init__(self,evento='',tipo='',data_inicio='',data_final=''):
        self.evento = evento
        self.tipo = tipo
        self.data_inicio = data_inicio
        self.data_final = data_final

        self.frame1 =Frame(root, width=400, height=400)
        self.frame1.place(x=50,y=50)
        self.titulo2 = Label(self.frame1, text="Evento")
        self.titulo2["font"] = ("Calibri", "12", "bold")
        self.titulo2.place(x=100,y=0)
        
        self.evento = Label(self.frame1, text='Nome :')
        self.evento.place(x=55, y=20)
        self.lnome = Entry(self.frame1)
        self.lnome.focus_force()
        self.lnome.place(x=55, y=50)

        self.tipo = Label(self.frame1, text='Tipo:')
        self.tipo.place(x=55, y=80)
        self.n_tipo = Entry(self.frame1)
        self.n_tipo.place(x=55, y=110)

        self.data_inicio = Label(self.frame1, text="Data Inicio:")
        self.data_inicio.place(x=35, y=140)
        self.n_data_inicio = Entry(self.frame1, width=10)
        self.n_data_inicio.place(x=35, y=160)

        self.data_final = Label(self.frame1, text="Data final:")
        self.data_final.place(x=205, y=140)
        self.n_data_final = Entry(self.frame1, width=10)
        self.n_data_final.place(x=205, y=160)

        self.botao = Button(self.frame1, text='Salvar', command=self.salvar_evento)
        self.botao.place(x=20, y=200, width=100, height=25)

        self.botao1 = Button(self.frame1, text='Pesquisar', command=self.mostra_evento)
        self.botao1.place(x=130, y=200, width=100, height=25)

        self.botao2 = Button(self.frame1, text='Alterar', command=self.update_evento)
        self.botao2.place(x=235, y=200, width=100, height=25)

        self.botao3 = Button(self.frame1, text='Excluir', command=self.delete_evento)
        self.botao3.place(x=235, y=250, width=100, height=25)
        
    def salvar_evento(self):
        try:
            self.evento = self.lnome.get()
            self.tipo = self.n_tipo.get()
            self.data_inicio = self.n_data_inicio.get()
            self.data_final = self.n_data_final.get()
            data = f'{self.data_final[0:2]}/{self.data_final[2:4]}/{self.data_final[4:]}'
            data1 = f'{self.data_inicio[0:2]}/{self.data_inicio[2:4]}/{self.data_inicio[4:]}'
            conn = sqlite3.connect('eletronica.db')
            cursor = conn.cursor()

            cursor.execute("""
                            INSERT INTO evento (evento,tipo,data_inicio,data_final)
                            VALUES ("%s","%s","%s","%s")
                            """ % (self.evento, self.tipo, data1,data))

            conn.commit()
            messagebox.showerror(" Salvar Dados","Todos Dados estão Salvo")
            conn.close()
            self.lnome.delete(0, END)
            self.n_tipo.delete(0, END)
            self.n_data_inicio.delete(0, END)
            self.n_data_final.delete(0,END)
            return "Evento salvo"
        except:
            return " Nao foi possivel salvar Evento "

    def mostra_evento(self):
        try:
            
            self.n_tipo.delete(0, END)
            self.n_data_inicio.delete(0, END)
            self.n_data_final.delete(0,END)
            conn = sqlite3.connect('eletronica.db')
            cursor = conn.cursor()
            self.su = "select evento,tipo, data_inicio,data_final from evento where evento = (?)"
            cursor.execute(self.su, [self.lnome.get()])
            busca = cursor.fetchall()
            for i in busca:
                if self.lnome.get() in i:
                    self.lnome.delete(0, END)
                    self.lnome.insert(END, i[0])
                    self.backup1 = i[0]
                    self.n_tipo.insert(END,i[1])
                    self.n_data_inicio.insert(END, i[2])
                    self.n_data_final.insert(END, i[3])

            conn.commit()
            conn.close()
            return "Busca realizada"
        except:
            return "Erro na Busca"

    def update_evento(self):
        try:
            self.evento = self.lnome.get()
            self.tipo = self.n_tipo.get()
            self.data_inicio = self.n_data_inicio.get()
            self.data_final = self.n_data_final.get()
            conn = sqlite3.connect('eletronica.db')
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE evento SET evento ='{self.evento}', tipo = '{self.tipo}', data_inicio = '{self.data_inicio}',data_final = '{self.data_final}' where evento = '{self.backup1}';")
            conn.commit()
            messagebox.showerror("Alterar Dados ","Todos Dados Foram Alterados")
            conn.close()
            self.lnome.delete(0, END)
            self.n_tipo.delete(0, END)
            self.n_data_inicio.delete(0, END)
            self.n_data_final.delete(0,END)
            return "Atualização realizada"
        except:
            return "Erro na atualização"
            
    def delete_evento(self):
       try:
           conn = sqlite3.connect('eletronica.db')
           cursor = conn.cursor()
           self.te ="delete from evento where evento = (?)"
           cursor.execute(self.te,[self.lnome.get()])
           busca = cursor.fetchall()
           for i in busca:
               if self.evento.get() in i:

                    self.evento.delete(0, END)
           conn.commit()
           messagebox.showerror("Deletar Dados","Todos Dados Foram Deletados")
           conn.close()
           self.lnome.delete(0, END)
           self.n_tipo.delete(0, END)
           self.n_data_inicio.delete(0, END)
           self.n_data_final.delete(0,END)
           return " Excluido com sucesso"
       except:
           return "Erro na exclusao "


class Reuniao:
    def __init__(self, descricao='', pauta='', dat_inicio='', hora_inicio='',dat_final='',hora_final=''):
        
        self.descricao = descricao
        self.pauta = pauta
        self.dat_inicio = dat_inicio
        self.hora_inicio = hora_inicio
        self.dat_final = dat_final
        self.hora_final = hora_final

        
        self.frame2 =Frame(root, width=400, height=400)
        self.frame2.place(x=50,y=50)
        self.titulo = Label(self.frame2, text="Reunião")
        self.titulo["font"] = ("Calibri", "12", "bold")
        self.titulo.place(x=100,y=50)

        self.descricao = Label(self.frame2, text='Descricao:')
        self.descricao.place(x=25, y=100)
        self.n_descricao = Entry(self.frame2)
        self.n_descricao.focus_force()
        self.n_descricao.place(x=100, y=100)

        self.pauta = Label(self.frame2, text='Pauta: ')
        self.pauta.place(x=50, y=130)
        self.n_pauta = Entry(self.frame2)
        self.n_pauta.place(x=100, y=130)

        self.dat_inicio = Label(self.frame2, text="Data Inicio:")
        self.dat_inicio.place(x=20, y=160)
        self.n_dat_inicio = Entry(self.frame2, width=10)
        self.n_dat_inicio.place(x=100, y=160)

        self.dat_final = Label(self.frame2, text="Data final:")
        self.dat_final.place(x=25, y=190)
        self.n_dat_final = Entry(self.frame2, width=10)
        self.n_dat_final.place(x=100, y=190)

        self.hora_inicio = Label(self.frame2, text="Hora Inicio:")
        self.hora_inicio.place(x=20, y=220)
        self.n_hora_inicio = Entry(self.frame2, width=10)
        self.n_hora_inicio.place(x=100, y=220)

        self.hora_final = Label(self.frame2, text="Hora final:")
        self.hora_final.place(x=25, y=250)
        self.n_hora_final = Entry(self.frame2, width=10)
        self.n_hora_final.place(x=100, y=250)

        self.botao = Button(self.frame2, text='Salvar', command=self.salvar_reuniao)
        self.botao.place(x=20, y=300, width=100, height=25)

        self.botao1 = Button(self.frame2, text='Pesquisar', command=self.mostra_reuniao)
        self.botao1.place(x=130, y=300, width=100, height=25)

        self.botao2 = Button(self.frame2, text='Alterar', command=self.update_reuniao)
        self.botao2.place(x=235, y=300, width=100, height=25)

        self.botao3 = Button(self.frame2, text='Excluir', command=self.delete_reuniao)
        self.botao3.place(x=235, y=340, width=100, height=25)
        
    def salvar_reuniao(self):
        try:
            self.descricao = self.n_descricao.get()
            self.pauta = self.n_pauta.get()
            self.dat_inicio = self.n_dat_inicio.get()
            self.dat_final = self.n_dat_final.get()
            data4 = f'{self.dat_final[0:2]}/{self.dat_final[2:4]}/{self.dat_final[4:]}'
            data6 = f'{self.dat_inicio[0:2]}/{self.dat_inicio[2:4]}/{self.dat_inicio[4:]}'
            self.hora_inicio = self.n_hora_inicio.get()
            self.hora_final = self.n_hora_final.get()
            hora = f'{self.hora_inicio[0:2]}:{self.hora_inicio[2:]}'
            hora1 = f'{self.hora_final[0:2]}:{self.hora_final[2:]}'
            conn = sqlite3.connect('eletronica.db')
            cursor = conn.cursor()

            cursor.execute("""
                            INSERT INTO Reuniao(descricao,pauta,dat_inicio,hora_inicio,dat_final,hora_final)
                            VALUES ("%s","%s","%s","%s","%s","%s")
                            """ % (self.descricao, self.pauta,data6,hora,data4,hora1))

            conn.commit()
            messagebox.showerror("Dados  de Reunão Salvo","Todos Dados de Reunião estão Salvo")
            conn.close()
            self.n_descricao.delete(0, END)
            self.n_pauta.delete(0, END)
            self.n_dat_inicio.delete(0, END)
            self.n_dat_final.delete(0,END)
            self.n_hora_inicio.delete(0,END)
            self.n_hora_final.delete(0,END)
            return "Reunião salva"
        except:
            return "Não foi possivel salvar a reunião"
        
    def mostra_reuniao(self):
        try:
            self.n_descricao.delete(0, END)
            self.n_dat_inicio.delete(0, END)
            self.n_dat_final.delete(0,END)
            self.n_hora_inicio.delete(0,END)
            self.n_hora_final.delete(0,END)
            conn = sqlite3.connect('eletronica.db')
            cursor = conn.cursor()
            self.sud = "select descricao,pauta, dat_inicio,hora_inicio,dat_final,hora_final from reuniao where pauta = (?)"
            cursor.execute(self.sud, [self.n_pauta.get()])
            busca = cursor.fetchall()
            for i in busca:
                if self.n_pauta.get() in i:
                    
                    self.n_descricao.insert(END, i[0])
                    self.n_pauta.delete(0, END)
                    self.n_pauta.insert(END,i[1])
                    self.backup2 = i[1]
                    self.n_dat_inicio.insert(END, i[2])
                    self.n_hora_inicio.insert(END,i[3])
                    self.n_dat_final.insert(END, i[4])
                    self.n_hora_final.insert(END,i[5])

            conn.commit()
            conn.close()
            return "Busca realizada"
        except:
            return "Erro durante a busca"

    def update_reuniao(self):
        try:
            global n_descricao, n_pauta, n_dat_inicio,n_hora_inicio,n_dat_final,n_hora_final
            print(self.backup2)
            self.descricao = self.n_descricao.get()
            self.pauta = self.n_pauta.get()
            self.dat_inicio = self.n_dat_inicio.get()
            self.hora_inicio =  self.n_hora_inicio.get()
            self.dat_final = self.n_dat_final.get()
            self.hora_final = self.n_hora_final.get()
            conn = sqlite3.connect('eletronica.db')
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE reuniao SET descricao = '{self.descricao}',pauta ='{self.pauta}',dat_inicio ='{self.dat_inicio}', hora_inicio ='{self.hora_inicio}', dat_final = '{self.dat_final}',hora_final = '{self.hora_final}' where pauta = '{self.backup2}';")
            conn.commit()
            messagebox.showerror("Alterar Dados","Todos Dados Foram Alterados")
            conn.close()
            self.n_descricao.delete(0, END)
            self.n_pauta.delete(0, END)
            self.n_dat_inicio.delete(0, END)
            self.n_dat_final.delete(0,END)
            self.n_hora_inicio.delete(0,END)
            self.n_hora_final.delete(0,END)
            return "Atualização Feita"
        except:
            return "Não foi possivel atualizar"
    def delete_reuniao(self):
       try:
           conn = sqlite3.connect('eletronica.db')
           cursor = conn.cursor()
           self.te ="delete from reuniao where pauta = (?)"
           cursor.execute(self.te,[self.n_pauta.get()])
           busca = cursor.fetchall()
           for i in busca:
               if self.pauta.get() in i:

                    self.pauta.delete(0, END)
           conn.commit()
           messagebox.showerror("Deletar Dados ","Todos Dados Foram Apagados")
           conn.close()
           self.n_descricao.delete(0, END)
           self.n_pauta.delete(0, END)
           self.n_dat_inicio.delete(0, END)
           self.n_dat_final.delete(0,END)
           self.n_hora_inicio.delete(0,END)
           self.n_hora_final.delete(0,END)
           return " Excluido com sucesso"
       except:
           return "Erro na exclusao "


frame =Frame(root, width=500, height=50)
frame.place(x=50,y=0)
b1 = Button(frame, text='Contato', command=Pessoa)
b1.place(x=10, y=0, width=100, height=25)
b2 = Button(frame, text='Evento', command=Evento)
b2.place(x=120, y=0, width=100, height=25)
b3 = Button(frame, text='Reuniao', command=Reuniao)
b3.place(x=230, y=0, width=100, height=25)
b4 = Button(frame, text='Sair', command=root.destroy)
b4.place(x=340, y=0, width=100, height=25)
root.mainloop()
