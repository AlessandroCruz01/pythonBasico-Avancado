# -*- coding: UTF-8 -*-
import operator
from tkinter import *
from tkinter import ttk
import sys
from tkinter import messagebox as mb
import os
from VETERINARIO.Icons import image
import sqlite3
import pycep_correios

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('Vet.db')
        self.conexao.cursor()
        self.c = self.conexao
        self.c.execute("""CREATE TABLE IF NOT EXISTS Pessoa (
                        idpessoa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        nasc TEXT NOT NULL,
                        cpf TEXT NOT NULL,
                        rg TEXT NOT NULL,
                        tpcadas TEXT NOT NULL,
                        fone TEXT NOT NULL,
                        fonecel TEXT,
                        fonecon TEXT,
                        email TEXT NOT NULL,
                        endereco TEXT NOT NULL,
                        cep TEXT NOT NULL,
                        bairro  TEXT NOT NULL,
                        cidade TEXT NOT NULL,
                        uf TEXT NOT NULL)""")

        self.conexao.commit()

        self.c.execute("""CREATE TABLE IF NOT EXISTS Animal (
                        nome TEXT NOT NULL,
                        idade TEXT NOT NULL,
                        especie TEXT NOT NULL,
                        raca TEXT NOT NULL)""")
        self.conexao.commit()

        self.c.execute("""CREATE TABLE IF NOT EXISTS Raca (
                             idpraca INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                             nome TEXT NOT NULL)""")
        self.conexao.commit()

        self.c.execute("""CREATE TABLE IF NOT EXISTS Contatos (
                                     idcont INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                     nome TEXT NOT NULL,
                                     telefone TEXT NOT NULL)""")
        self.conexao.commit()

        self.c.execute("""CREATE TABLE IF NOT EXISTS Especie (
                             idespecie INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                             nome TEXT NOT NULL)""")
        self.conexao.commit()

        # self.c.execute("""CREATE TABLE IF NOT EXISTS Reuniao (
        #                 descricao TEXT NOT NULL,
        #                 pauta TEXT NOT NULL,
        #                 data_inicio TEXT NOT NULL,
        #                 hora_inicio TEXT NOT NULL,
        #                 data_final TEXT NOT NULL,
        #                 hora_final TEXT NOT NULL)""")
        # self.conexao.commit()
        self.conexao.close()


class TelaPrincipal(Banco):
    def __init__(self, master):
        super(Banco).__init__()
        self.master = master
        self.master.geometry('800x900')
        self.master.state('zoomed')
        self.master.iconbitmap(default='Icons/ossinho.ico')
        self.master.title('Cleutovis - Software veterinário')
        self.master['background'] = 'light blue'

        self.menuwidget = Menu(self.master)
        self.filemenu = Menu(self.menuwidget)
        self.filemenu2 = Menu(self.menuwidget)
        self.filemenu3 = Menu(self.menuwidget)
        self.filemenu4 = Menu(self.menuwidget)
        self.imaPesqFrame = PhotoImage(file='Icons/lupinha.png')
        self.imaAjuPesqFrame = PhotoImage(file='Icons/lampada.png')
        self.imaLupa = PhotoImage(file='Icons/lupa.png')
        self.imagCalendario = PhotoImage(file='Icons/calendario.png')
        self.menuwidget.add_cascade(label='Cadastrar', menu=self.filemenu)
        self.filemenu.add_command(label='Clientes', command=self.telaCadCliente)
        self.filemenu.add_command(label='Especies', command=self.telCadEsp)
        self.filemenu.add_command(label='Raças', command=self.telCadRaca)
        # self.filemenu.add_separator()
        # self.filemenu.add_command(label='Exames', command='')
        # self.filemenu.add_command(label='Receituário', command='')
        # self.filemenu.add_separator()
        # self.filemenu.add_command(label='Produtos / Serviços', command='')
        self.filemenu.add_command(label='Sair', command=self.master.destroy)
        # self.menuwidget.add_cascade(label='Estoque', menu=self.filemenu2)
        # self.filemenu2.add_command(label='Entrada Estoque Simples', command='')
        # self.filemenu2.add_command(label='Listagem de entrada', command='')
        #self.menuwidget.add_command(label='PDV', command='')
        self.menuwidget.add_cascade(label='Atendimento', menu=self.filemenu4)
        self.filemenu4.add_command(label='Cadastrar Atendimento', command=self.telaCadAtendimento)
        self.filemenu4.add_command(label='Abrir atendimento', command=self.telaAtendimento)
        self.menuwidget.add_command(label='Contatos', command=self.cadContatos)
        self.menuwidget.add_command(label='Relatórios', command=self.telRelatorio)
        #self.menuwidget.add_command(label='Configurar', command='')
        self.menuwidget.add_command(label='Sair', command=self.master.destroy)
        self.fraBot = Frame(self.master, width=1930, height=80, bg='grey')
        self.fraBot.place(x=0, y=0)
        self.master.config(menu=self.menuwidget)

    def telaCadCliente(self):
        #GOSTO DO MODELO DE JANELA SOBRE JANELA POR ISSO O TOPLEVEL
        self.fichaCliente = Toplevel(self.master)
        self.fichaCliente.geometry('800x460')
        self.fichaCliente.title('Ficha do Cliente')
        self.fichaCliente['background'] = 'light blue'
        self.fichaCliente.grab_set()

        #ESSE FRAME FICA O NOME DO USUÁRIO E ID PRA ALTERAÇÕES
        self.cabFicCli = Frame(self.fichaCliente, width=800, height=70, bg='gray')
        self.cabFicCli.pack()

        self.bSave = Button(self.fichaCliente, text='Salvar', fg='green', command=self.salvaClient)
        self.bSave.place(x=600, y=70)
        self.botFichCli = Button(self.fichaCliente, text='Ficha Cadastral', command=self.telaCadCliente, state = DISABLED)
        self.botFichCli.place(x=0, y=70)
        self.botAnimCliente = Button(self.fichaCliente)
        self.botAnimCliente.configure(text='Animais do cliente', command=self.telCadAni, state=DISABLED)
        self.botAnimCliente.place(x=93, y=70)
        # self.botDebCliente = Button(self.fichaCliente, text='Débitos')
        # self.botDebCliente.place(x=205, y=70)
        self.botAnotCliente = Button(self.fichaCliente)
        self.botAnotCliente.configure(text='Anotações', command='', state=DISABLED)
        self.botAnotCliente.place(x=205, y=70)
        # self.botHistDebCliente = Button(self.fichaCliente, text='Hist. de Débitos')
        # self.botHistDebCliente.place(x=328, y=70)
        # self.botHistPagCliente = Button(self.fichaCliente, text='Hist. de Pagamentos')
        # self.botHistPagCliente.place(x=425, y=70)
        # self.botOrcCliente = Button(self.fichaCliente, text='Orçamento')
        # self.botOrcCliente.place(x=548, y=70)
        self.atProcCli = Label(self.fichaCliente, text='Procurar:', bg='light blue')
        self.atProcCli["font"] = ("Calibri", "13", "bold")
        self.atProcCli.place(x=0, y=100)
        self.frDePesquisa = Frame(self.fichaCliente, width=700, height=50, bg='grey')
        self.frDePesquisa.place(x=50, y=122)
        self.pesPNome = Label(self.frDePesquisa, text='Nome:', bg='grey')
        self.pesPNome.place(x=5, y=0)
        self.entPesNome = Entry(self.frDePesquisa, width=50)
        self.entPesNome.focus_force()
        self.entPesNome.place(x=5, y=20)
        self.pesPCpf = Label(self.frDePesquisa, text='CPF: ', bg='grey')
        self.pesPCpf.place(x=350, y=0)

        self.vcmd = self.master.register(func=self.limita_tamanho_cpf)
        self.vcmd2 = self.master.register(func=self.limita_tamanho_rg)

        self.entPCpf = Entry(self.frDePesquisa, width=40, validate='key', validatecommand=(self.vcmd, '%P'))
        self.entPCpf.place(x=350, y=20)
        self.bPesFraPesq = Button(self.frDePesquisa, image=self.imaPesqFrame)
        self.bPesFraPesq.place(x=610, y=10)
        self.bAjudPesqFra = Button(self.frDePesquisa, image=self.imaAjuPesqFrame, text='Ajuda')
        self.bAjudPesqFra.place(x=650, y=10)
    #AQUI COMEÇAM OS LABELS E ENTRYS DO CADASTRO PROPRIAMENTE DITO
        #1° LINHA TEM SÓ O NOME POR ISSO ESSE PRIMEIRO CONJUNTO ESTA COMPLETO COM ENTRY E LABEL DE NOME
        self.nomeCliente = Label(self.fichaCliente, text='Nome: ', bg='light blue')
        self.nomeCliente.place(x=10, y=185)
        self.eNomeCliente = Entry(self.fichaCliente, width=129)
        self.eNomeCliente.place(x=10, y=205)
        #2° LINHA TEM O NASC, O CPF, RG E SE É PESSOA FISICA OU JURIDICA
            #Labels
        self.dtaNascClie = Label(self.fichaCliente, text='Data de nascimento:', bg='light blue')
        self.dtaNascClie.place(x=10, y=235)
        self.nCpfCliente = Label(self.fichaCliente, text='CPF:', bg='light blue')
        self.nCpfCliente.place(x=170, y=235)
        self.nRgCliente = Label(self.fichaCliente, text='RG:', bg='light blue')
        self.nRgCliente.place(x=300, y=235)
        self.tp = Label(self.fichaCliente, text='Tipo de Cadastro:', bg='light blue')
        self.tp.place(x=550, y=235)
            #Entrys
        self.dtaNascClieEnt = Entry(self.fichaCliente, width=20)
        self.dtaNascClieEnt.place(x=10, y=255)
        self.bPesqData = Button(self.fichaCliente, image=self.imagCalendario, command='')
        self.bPesqData.place(x=135, y=254)
        self.cpfClient = Entry(self.fichaCliente, width=18, validate='key', validatecommand=(self.vcmd, '%P'))
        self.cpfClient.place(x=170, y=255)
        self.rgClient = Entry(self.fichaCliente, width=35, validate='key', validatecommand=(self.vcmd2, '%P'))
        self.rgClient.place(x=300, y=255)
             #USO DE CHECKBUTONS PARA FACILITAR SE É FISICA OU JURIDICA
        self.itens = ['Selecione', 'PESSOA FISICA', 'PESSOA JURIDICA']
        self.n_tpp = ttk.Combobox(self.fichaCliente, width=36)
        self.n_tpp["values"] = self.itens
        self.n_tpp.current(0)
        self.n_tpp.bind("<<ComboboxSelected>>")
        self.n_tpp.place(x=550, y=255)
        #3°LINHA TEM TEL RESIDENCIAL, TEL CELULAR, , TEL CONTATO, EMAIL
            #labels
        self.nTelResCliente = Label(self.fichaCliente, text='Telefone Residencial', bg='light blue')
        self.nTelResCliente.place(x=10, y=290)
        self.nTelCelCliente = Label(self.fichaCliente, text='Telefone Celular:', bg='light blue')
        self.nTelCelCliente.place(x=170, y=290)
        self.nTelContCliente = Label(self.fichaCliente, text='Telefone Contato:', bg='light blue')
        self.nTelContCliente.place(x=300, y=290)
        self.nEmailCliente = Label(self.fichaCliente, text='Email:', bg='light blue')
        self.nEmailCliente.place(x=500, y=290)
            #Entrys
        self.telResCliente = Entry(self.fichaCliente, width=20)
        self.telResCliente.place(x=10, y=310)
        self.telCelCliente = Entry(self.fichaCliente, width=18)
        self.telCelCliente.place(x=170, y=310)
        self.telContCliente = Entry(self.fichaCliente, width=18)
        self.telContCliente.place(x=300, y=310)
        self.emailCliente = Entry(self.fichaCliente, width=55)
        self.emailCliente.place(x=450, y=310)
        #4°LINHA TEM O ENDEREÇO
        self.endCli = Label(self.fichaCliente, text='Endereço:', bg='light blue')
        self.endCli.place(x=10, y=340)
        self.endClient = Entry(self.fichaCliente, width=129)
        self.endClient.place(x=10, y=365)
        #5°LINHA TEM BAIRRO, CIDADE, CEP E ESTADO QUE É UM LISTBOX
           #labels
        self.nCepClie = Label(self.fichaCliente, text='CEP:', bg='light blue')
        self.nCepClie.place(x=10, y=390)
        self.nBairroCli = Label(self.fichaCliente, text='Bairro', bg='light blue')
        self.nBairroCli.place(x=200, y=390)
        self.nCidadeCli = Label(self.fichaCliente, text='Cidade:', bg='light blue')
        self.nCidadeCli.place(x=370, y=390)
        self.nEstCli = Label(self.fichaCliente, text='Uf:', bg='light blue')
        self.nEstCli.place(x=580, y=390)
           #entrys
        self.cepCli = Entry(self.fichaCliente, width=27)
        self.cepCli.place(x=10, y=420)
        self.bPesqCep = Button(self.fichaCliente, image=self.imaLupa, command=self.pesquisaCep)
        self.bPesqCep.place(x=165, y=420)
        self.bairCli = Entry(self.fichaCliente, width=25)
        self.bairCli.place(x=200, y=420)
        self.cidCli = Entry(self.fichaCliente, width=30)
        self.cidCli.place(x=370, y=420)
        self.itens = ['Selecione', 'AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
        self.n_uf = ttk.Combobox(self.fichaCliente, width=31)
        self.n_uf["values"] = self.itens
        self.n_uf.current(0)
        self.n_uf.bind("<<ComboboxSelected>>")
        self.n_uf.place(x=580, y=420)


    #TELA DE CADASTRO DO ANIMAL
    def telCadAni(self):
        self.cadAni = Frame(self.fichaCliente, width=800, height=400,bg='light blue' )
        self.cadAni.pack(side='left')
        self.n = Label(self.cabFicCli, text=self.nome_client, bg="gray")
        self.n["font"] = ("Arial", "25", "bold")
        self.n.place(x=300, y=10)
        self.fichaCliente.title('Ficha do Animal')
        self.cadAni.focus_force()

        self.rel = Frame(self.cadAni, width=740, height=300)
        self.rel.place(x=30, y=30)

        self.nNomeAnimal = Label(self.cadAni, text='Nome do Animal: ')
        self.nNomeAnimal.place(x=35, y=50)
        self.tipoAnimal = Label(self.cadAni, text='Espécie: ')
        self.tipoAnimal.place(x=35, y= 100)
        self.raca = Label(self.cadAni, text='Raça: ')
        self.raca.place(x=35, y=150)
        self.idadeAnim = Label(self.cadAni, text='Idade: ')
        self.idadeAnim.place(x=35, y=200)

        self.nomeAnimal = Entry(self.cadAni, width=80)
        self.nomeAnimal.place(x=150, y=50)

        self.tpesp = ['Selecione']
        self.espAni = ttk.Combobox(self.cadAni, width=77)
        self.espAni["values"] = self.combo_esp()
        self.espAni.current(0)
        self.espAni.bind("<<ComboboxSelected>>")
        self.espAni.place(x=150, y=100)
        self.bcadEsp = Button(self.cadAni, text='Cadastrar espécie', fg='red', command=self.telCadEsp)
        self.bcadEsp.place(x=650, y=100)

        self.traca = ['Selecione']
        self.racAni = ttk.Combobox(self.cadAni, width=77)
        self.racAni["values"] = self.combo_raca()
        self.racAni.current(0)
        self.racAni.bind("<<ComboboxSelected>>")
        self.racAni.place(x=150, y=150)
        self.bcadRac = Button(self.cadAni, text='Cadastrar Raça', fg='red', command=self.telCadRaca)
        self.bcadRac.place(x=650, y=150)

        self.idadeAn = Entry(self.cadAni, width=10)
        self.idadeAn.place(x=150, y=200)

        self.bAdAn = Button(self.cadAni, text='Salvar', command=self.saveAnimal)
        self.bAdAn.place(x=300, y=250)
        self.bSadAn = Button(self.cadAni, text='Cancelar', command=self.cadAni.destroy)
        self.bSadAn.place(x=400, y=250)

    #TELA DO CADASTRO DE ESPECIE
    def telCadEsp(self):
        self.cadEsp = Toplevel(self.master)
        self.cadEsp.geometry('400x150')
        self.cadEsp.grab_set()

        self.tt = Label(self.cadEsp, text='CADASTRO DE ESPÉCIES')
        self.tt["font"] = ("Calibri", "13", "bold")
        self.tt.place(x=120, y=5)
        self.nomEspEnt = Entry(self.cadEsp, width=50)
        self.nomEspEnt.place(x=50, y=50)
        self.svEsp = Button(self.cadEsp, text='Salvar', command=self.saveEsp)
        self.svEsp.place(x=120, y=90)
        self.cancEsp = Button(self.cadEsp, text='Cancelar', command=self.cadEsp.destroy)
        self.cancEsp.place(x=220, y=90)

    def telCadRaca(self):
        self.cadRac = Toplevel(self.master)
        self.cadRac.geometry('400x150')
        self.cadRac.grab_set()

        self.tt2 = Label(self.cadRac, text='CADASTRO DE RAÇAS')
        self.tt2["font"] = ("Calibri", "13", "bold")
        self.tt2.place(x=120, y=5)
        self.nomRacEnt = Entry(self.cadRac, width=50)
        self.nomRacEnt.place(x=50, y=50)
        self.svRac = Button(self.cadRac, text='Salvar', command=self.saveRaca)
        self.svRac.place(x=120, y=90)
        self.cancRac = Button(self.cadRac, text='Cancelar', command=self.cadRac.destroy)
        self.cancRac.place(x=220, y=90)

#FUNCÃO DE SALVAMENTO DA TELA DE CLIENTE!
    def salvaClient(self):
        try:
            self.nome_client = self.eNomeCliente.get().strip()
            self.nasc_cleint = self.dtaNascClieEnt.get()
            self.cpf_cliet = self.cpfClient.get()
            self.rg_client = self.rgClient.get()
            self.tp_cadas = self.n_tpp.get()
            self.tel = self.telResCliente.get()
            self.telcel = self.telCelCliente.get()
            self.telcont = self.telContCliente.get()
            self.email = self.emailCliente.get()
            self.end = self.endClient.get().strip().title()
            self.cep = self.cepCli.get()
            self.bairro = self.bairCli.get()
            self.cidade = self.cidCli.get()
            self.uf = self.n_uf.get()


            print('ok')

        except:
            print('ERRO NA FUNÇÃO SALVAR PEGANDO OS DADOS DOS ENTRYS')
            print(sys.exc_info())

        try:
            if len(self.nome_client) == 0 or len(self.cpf_cliet) == 0:
                mb.showerror('ERRO', 'CAMPOS NOME/CPF SÃO OBRIGATÓRIOS!\n POR FAVOR VERIFIQUE! ')
            else:
                con = sqlite3.connect('Vet.db')
                cursor = con.cursor()

            con = sqlite3.connect('Vet.db')
            cursor = con.cursor()
            self.lok = 'select cpf from Pessoa where cpf = (?)'
            cursor.execute(self.lok, [self.cpfClient.get()])
            self.lok = cursor.fetchall()
            if self.lok:
                mb.showerror('FALHA NO CADASTRO','JA EXISTE NO BANCO')
            else:
                cursor.execute('''
                                INSERT INTO Pessoa(nome, nasc, cpf, rg, tpcadas, fone, fonecel,  fonecon, email, endereco, cep, bairro, cidade, uf)
                                VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                                '''%(self.nome_client,self.nasc_cleint, self.cpf_cliet,self.rg_client,self.tp_cadas,self.tel,self.telcel,self.telcont,self.email, self.end, self.cep, self.bairro, self.cidade, self.uf))
                con.commit()

                mb.showinfo('SALVO', 'SALVO COM SUCESSO')
                con.close()
                self.botAnimCliente.configure(state=NORMAL)
                self.botAnotCliente.configure(state=NORMAL)
        except:
            mb.showerror('ERROR! DESCULPE NÃO FOI POSSIVEL SALVAR!', sys.exc_info()[1:])
            print(sys.exc_info())

    def saveEsp(self):
        self.nomEsp = self.nomEspEnt.get()
        con = sqlite3.connect('Vet.db')
        cursor = con.cursor()
        cursor.execute('''
                        INSERT INTO Especie(nome)
                        VALUES ('%s')'''%(self.nomEsp))

        con.commit()
        mb.showinfo('SALVO', 'SALVO COM SUCESSO')

    def saveRaca(self):
        self.nomRac = self.nomRacEnt.get()
        con = sqlite3.connect('Vet.db')
        cursor = con.cursor()
        cursor.execute('''
                        INSERT INTO Raca(nome)
                        VALUES ('%s')'''%(self.nomRac))
        con.commit()
        mb.showinfo('SALVO', 'SALVO COM SUCESSO')

    def combo_raca(self):
        con = sqlite3.connect('Vet.db')
        cursor = con.cursor()
        cursor.execute('''SELECT nome FROM Raca''')
        data = []
        for row in cursor.fetchall():
            data.append(row[0])
        return data

    def combo_esp(self):
        con = sqlite3.connect('Vet.db')
        cursor = con.cursor()
        cursor.execute('''SELECT nome FROM Especie''')
        data2 = []
        for row in cursor.fetchall():
            data2.append(row[0])
        return data2

    def saveAnimal(self):
        self.nomAni = self.nomeAnimal.get()
        self.esp = self.espAni.get()
        self.rac = self.racAni.get()
        self.idade = self.idadeAn.get()
        con = sqlite3.connect('Vet.db')
        cursor = con.cursor()

        cursor.execute('''
                         INSERT INTO Animal(nome, idade, especie, raca)
                         VALUES ('%s', '%s', '%s', '%s')''' % (self.nomAni, self.esp, self.rac, self.idade))
        con.commit()
        mb.showinfo('SALVO', 'SALVO COM SUCESSO')

    def limita_tamanho_cpf(self, p):
        if len(p) > 11:
            return False
        return True

    def limita_tamanho_rg(self, p):
        if len(p) > 8:
            return False
        return True

    def pesquisaCep(self):
        #OBS: HÁ A NECESSIDADE DE ACESSO A INTERNET PARA USAR ESTA FUNÇÃO
        try:
            print(self.cepCli.get())
            self.endereco = pycep_correios.consultar_cep(self.cepCli.get())
            print(self.endereco)
            print(self.endereco['cidade'])

            #limpa os Entrys para nao haja repetição em caso de varios cliks na função pesquisar
            self.cidCli.delete(0, END)
            self.n_uf.delete(0, END)
            self.bairCli.delete(0, END)
            self.endClient.delete(0, END)

            self.cidCli.insert(END, self.endereco['cidade'])
            self.bairCli.insert(END, self.endereco['bairro'])
            self.n_uf.delete(0, END)
            self.n_uf.insert(END, self.endereco['uf'])
            self.endClient.insert(END, self.endereco['end'])
        except:
            mb.showinfo('Aviso', 'Desculpe! talvez este CEP não exista ou você está sem acesso a internet. Por favor verifcar sua conexão ou o campo CEP.')
            print('CEP INVÁLIDO')
            print(sys.exc_info())

    def cadContatos(self):
        self.telaCont = Toplevel(self.master)
        self.telaCont.geometry('400x300')
        self.telaCont.grab_set()

        self.tt2 = Label(self.telaCont, text='CADASTRO DE CONTATOS')
        self.tt2["font"] = ("Calibri", "13", "bold")
        self.tt2.place(x=120, y=5)
        self.nomCL = Label(self.telaCont, text='Nome')
        self.nomCL.place(x=165, y=50)
        self.nomCL["font"] = ("Arial", "12", "bold")
        self.nomCL = Label(self.telaCont, text='Telefone')
        self.nomCL.place(x=155, y=130)
        self.nomCL["font"] = ("Arial", "12", "bold")

        self.nomC = Entry(self.telaCont, width=50)
        self.nomC.place(x=50, y=80)
        self.numC = Entry(self.telaCont, width=50)
        self.numC.place(x=50, y=160)
        self.svC = Button(self.telaCont, text='Salvar', command=self.svCont)
        self.svC.place(x=120, y=250)
        self.cancC = Button(self.telaCont, text='Cancelar', command=self.telaCont.destroy)
        self.cancC.place(x=220, y=250)

        self.telaCont.mainloop()

    def svCont(self):
        self.nomeCont = self.nomC.get()
        self.numeroCont = self.numC.get()
        if len(self.nomeCont) == 0 or len(self.numeroCont) == 0:
            mb.showerror('Erro', 'Todos os campos são obrigatórios!')
        else:
            con = sqlite3.connect('Vet.db')
            cursor = con.cursor()

            cursor.execute('''
                                     INSERT INTO Contatos(nome, telefone)
                                     VALUES ('%s', '%s')''' % (self.nomeCont, self.numeroCont))
            con.commit()
            mb.showinfo('SALVO', 'CONTATO SALVO COM SUCESSO!')

    def telaCadAtendimento(self):
        cadAte = Toplevel(self.master)
        cadAte.geometry('500x400')
        cadAte.mainloop()

    def telaAtendimento(self):
        Ate = Toplevel(self.master)
        Ate.geometry('500x400')
        Ate.mainloop()

    def relatorio(self):
        con = sqlite3.connect('Vet.db')
        cursor = con.cursor()
        self.lok = 'select * from Pessoa where cpf = (?)'
        cursor.execute(self.lok, [self.cpfClient.get()])
        busca = cursor.fetchall()
        for i in busca:
            print(i)
            if self.cpfClient.get() in i:
                salvo = open('Relatorio.txt', 'w')
                salvo.write('\n ---- RELATORIO DE CLIENTES ----\n')
                salvo.write('\n----------------------------------\n')
                salvo.write(f'ID: {i[0]}\n')
                salvo.write(f'Nome: {i[1]}\n')
                salvo.write(f'Nascimento: {i[2]}\n')
                salvo.write(f'CPF: {i[3]}\n')
                salvo.write(f'RG: {i[4]}\n')
                salvo.write(f'Tipo de cadastro: {i[5]}\n')
                salvo.write(f'Telefone: {i[6]}\n')
                salvo.write(f'Telefone Celular: {i[7]}\n')
                salvo.write(f'Telefone Referência: {i[8]}')
                salvo.write(f'email: {i[9]}')
                salvo.write(f'Endereço: {i[10]}')
                salvo.write(f'CEP: {i[11]}')
                salvo.write(f'Bairro: {i[12]}')
                salvo.write(f'Cidade: {i[13]}')
                salvo.write(f'Uf: {i[14]}')

                salvo.close()
        con.commit()
        mb.showinfo('RELATORIO GERADO', 'RELATORIO GERADO COM SUCESSO')
        con.close()
    def telRelatorio(self):
        self.pesRel = Toplevel(self.master)
        self.pesRel.geometry('400x150')
        self.pesRel.grab_set()

        self.tt2 = Label(self.pesRel, text='GERAR RELATORIO DE CLIENTES')
        self.tt2["font"] = ("Calibri", "13", "bold")
        self.tt2.place(x=120, y=5)
        self.eCpf = Entry(self.pesRel, width=50)
        self.eCpf.place(x=50, y=50)
        self.gerar = Button(self.pesRel, text='Gerar', command=self.relatorio)
        self.gerar.place(x=120, y=90)
        self.canc = Button(self.pesRel, text='Cancelar', command=self.pesRel.destroy)
        self.canc.place(x=220, y=90)


b = Banco()
root = Tk()
a = TelaPrincipal(root)
root.mainloop()