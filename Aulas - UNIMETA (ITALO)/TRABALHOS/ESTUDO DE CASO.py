# -*- coding: UTF-8 -*-

try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from tkinter import ttk
from threading import Thread
from time import strftime
import pycep_correios
from datetime import date
import sqlite3
from tkinter import messagebox as mb
import sys

conexao = sqlite3.connect('escola2.db')
conexao.cursor()
c = conexao

class Tela(Thread):
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x800')
        #self.root.state("zoomed")

        self.menuwidget = Menu(root)
        self.filemenu = Menu(self.menuwidget)
        self.filemenu1 = Menu(self.menuwidget)
        self.filemenu2 = Menu(self.menuwidget)
        self.filemenu3 = Menu(self.menuwidget)

        self.menuwidget.add_cascade(label='CONFIGURAÇÕES', menu=self.filemenu)
        self.filemenu.add_command(label='Cargo', command='')
        self.filemenu.add_command(label='Backgroud', command='')
        self.filemenu.add_command(label='Turmas', command='')
        #self.filemenu.add_command(label='Habilitar Login', command='')
        #self.filemenu.add_command(label='Usuários', command='')
        self.filemenu.add_command(label='SAIR', command=self.root.destroy)

        self.menuwidget.add_cascade(label='CADASTROS', menu=self.filemenu1)
        self.filemenu1.add_command(label='Aluno', command=self.cadastro_aluno)
        self.filemenu1.add_command(label='Funcionário', command=self.cadastro_funcionario)

        self.menuwidget.add_cascade(label='AVALIAÇÕES', menu=self.filemenu2)
        self.filemenu2.add_command(label='none', command='')
        self.filemenu2.add_command(label='none', command='')
        self.filemenu2.add_command(label='none', command='')

        self.menuwidget.add_cascade(label='RELATÓRIOS', menu=self.filemenu3)
        self.filemenu3.add_command(label='none', command='')
        self.filemenu3.add_command(label='none', command='')
        self.filemenu3.add_command(label='none', command='')


        self.root.config(menu=self.menuwidget)

        super(Tela, self).__init__()


    #------------------------------------------------------------------------------------------

    #FUNÇÃO PARA LIMITAR ENTRYS
    def on_write(self,*args):
        self.s = self.var.get()
        if len(self.s) > 0:
            if not self.s[-1].isdigit():  # retirar ultimo caracter caso nao seja digito
                self.var.set(self.s[:-1])
            else:  # aproveitar apenas os primeiros 5 chars
                self.var.set(self.s[:self.max_len])

    #-----------------------TOP LEVEL ALUNO---------------------------------------------------
    def cadastro_aluno(self):

        #PEQUENA FUNÇÃO PARA LIMITAR OS CARACTERES NOS ENTRYS
        self.max_len = 11  # maximo num de caracteres
        self.var = StringVar()
        self.var.trace("w", self.on_write)  # rastrear valor da variavel e executar funcao de validacao quando mudar

        self.cad = Toplevel(self.root)
        self.cad.title('Cadastro de Aluno')
        self.cad.grid()
        #self.cad.focus_force()  #
        self.cad.grab_set()  #
        self.cad.geometry('600x560')
        self.cad.resizable(width=False, height=False)


        self.lin = Label(self.cad, text='-' * 150)
        self.lin.place(x=0, y=5)
        self.tt1 = Label(self.cad, text='DADOS PESSOAIS')
        self.tt1["font"] = ("Calibri", "13", "bold")
        self.tt1.place(x=0, y=5)

        self.nome = Label(self.cad, text='Nome: ')
        self.nome.place(x=10, y=50)
        self.n_nome = Entry(self.cad, width=80)
        self.n_nome.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_nome.place(x=70, y=50)

        self.cpf = Label(self.cad, text='CPF: ')
        self.cpf.place(x=10, y=100)
        self.n_cpf = Entry(self.cad, width=20, textvariable=self.var)
        self.n_cpf.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_cpf.place(x=70, y=100)

        self.max_len = 8  # maximo num de caracteres
        self.var = StringVar()
        self.var.trace("w", self.on_write)  # rastrear valor da variavel e executar funcao de validacao quando mudar

        self.rg = Label(self.cad, text='RG: ')
        self.rg.place(x=350, y=100)
        self.n_rg = Entry(self.cad, width=25,textvariable=self.var )
        self.n_rg.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_rg.place(x=400, y=100)

        self.nasc = Label(self.cad, text='Data de nascimento: ')
        self.nasc.place(x=10, y=150)
        self.dia = Entry(self.cad, width=5)
        self.mes = Entry(self.cad, width=5)
        self.ano = Entry(self.cad, width=10)
        self.dia.place(x=130, y=150)
        self.mes.place(x=160, y=150)
        self.ano.place(x=190, y=150)
        #self.data = (f'{1} / {2} / {3}'.format(self.dia.get(), self.mes.get(), self.ano.get()))

        self.sexo = Label(self.cad, text='Sexo: ')
        self.sexo.place(x=350, y=150)
        self.itens1 = ['Selecione', 'MASCULINO', 'FEMININO']
        self.n_sexo = ttk.Combobox(self.cad, width=22)
        self.n_sexo["values"] = self.itens1
        self.n_sexo.current(0)
        self.n_sexo.bind("<<ComboboxSelected>>")
        self.n_sexo.place(x=400, y=150)

        #1° fase do EJA Corresponde do 1º ao 5º ano do Ensino Regular (séries iniciais do Ensino Fundamental)
        self.esc = Label(self.cad, text='Escolaridade: ')
        self.esc.place(x=10, y=200)
        self.itens2 = ['Selecione', '1° ano', '2° ano', '3° ano', '4° ano', '5° ano']
        self.n_esc = ttk.Combobox(self.cad, width=15)
        self.n_esc["values"] = self.itens2
        self.n_esc.current(0)
        self.n_esc.bind("<<ComboboxSelected>>")
        self.n_esc.place(x=100, y=200)

        self.sit = Label(self.cad, text='Situação: ')
        self.sit.place(x=235, y=200)
        self.itens3 = ['Selecione', 'Cursando','Reprovado', 'Aprovado']
        self.n_sit = ttk.Combobox(self.cad, width=9)
        self.n_sit["values"] = self.itens3
        self.n_sit.current(0)
        self.n_sit.bind("<<ComboboxSelected>>")
        self.n_sit.place(x=300, y=200)

        self.hist = Label(self.cad, text='Histórico entregue? ')
        self.hist.place(x=400, y=200)
        self.itens3 = ['', 'SIM', 'NÃO']
        self.n_hist = ttk.Combobox(self.cad, width=4)
        self.n_hist["values"] = self.itens3
        self.n_hist.current(0)
        self.n_hist.bind("<<ComboboxSelected>>")
        self.n_hist.place(x=509, y=200)

        #************************************************************#

        self.lin1 = Label(self.cad, text='-' * 150)
        self.lin1.place(x=0, y=250)
        self.tt2 = Label(self.cad, text='RESPONSÁVEL ')
        self.tt2["font"] = ("Calibri", "13", "bold")
        self.tt2.place(x=0, y=250)

        self.nome_resp = Label(self.cad, text='Nome: ')
        self.nome_resp.place(x=10, y=300)
        self.n_nome_resp = Entry(self.cad, width=30)
        self.n_nome_resp.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_nome_resp.place(x=70, y=300)

        self.cpf_resp = Label(self.cad, text='CPF: ')
        self.cpf_resp.place(x=270, y=300)
        self.n_cpf_resp = Entry(self.cad, width=16)
        self.n_cpf_resp.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_cpf_resp.place(x=310, y=300)

        self.fone = Label(self.cad, text='Fone: ')
        self.fone.place(x=430, y=300)
        self.n_fone = Entry(self.cad, width=13)
        self.n_fone.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_fone.place(x=470, y=300)

        #************************************************************#

        self.lin2 = Label(self.cad, text='-'*250)
        self.lin2.place(x=0 , y=350)
        self.tt3 = Label(self.cad, text='ENDEREÇO')
        self.tt3["font"] = ("Calibri", "13", "bold")
        self.tt3.place(x=0, y=350)

        self.cep = Label(self.cad, text='CEP: ')
        self.cep.place(x=10, y=400)
        self.n_cep = Entry(self.cad, width=20)
        self.n_cep.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_cep.place(x=70, y=400)
        self.b_cep = Button(self.cad, text='Buscar', command=self.pesquisa_cep_aluno)
        self.b_cep.place(x=200, y=395)

        self.cid = Label(self.cad, text='Cidade: ')
        self.cid.place(x=270, y=400)
        self.n_cid = Entry(self.cad, width=15)
        self.n_cid.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_cid.place(x=320, y=400)

        self.uf = Label(self.cad, text='UF: ')
        self.uf.place(x=440, y=400)
        self.itens = ['Selecione', 'AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS'
            , 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
        self.n_uf = ttk.Combobox(self.cad, width=10)
        self.n_uf["values"] = self.itens
        self.n_uf.current(0)
        self.n_uf.bind("<<ComboboxSelected>>")
        self.n_uf .place(x=470, y=400)

        self.bai = Label(self.cad, text='Bairro: ')
        self.bai.place(x=10, y=450)
        self.n_bai = Entry(self.cad, width=20)
        self.n_bai.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_bai.place(x=70, y=450)

        self.rua = Label(self.cad, text='Rua: ')
        self.rua.place(x=200, y=450)
        self.n_rua = Entry(self.cad, width=30)
        self.n_rua.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_rua.place(x=250, y=450)

        self.casa = Label(self.cad, text='Casa N°: ')
        self.casa.place(x=440, y=450)
        self.n_casa = Entry(self.cad, width=8)
        self.n_casa.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_casa.place(x=500, y=450)

        self.b_save = Button(self.cad, text='Salvar', command=self.save_aluno)
        self.b_save["font"] = ("Arial", "10", "bold")
        self.b_save.place(x=90, y=500)

        self.b_limpa = Button(self.cad, text='Limpar', command=self.limpa_tela_aluno)
        self.b_limpa["font"] = ("Arial", "10", "bold")
        self.b_limpa.place(x=150, y=500)

        self.b_busca = Button(self.cad, text='Buscar', command=self.pesquisa_aluno)
        self.b_busca["font"] = ("Arial", "10", "bold")
        self.b_busca.place(x=250, y=500)

        self.b_busca = Button(self.cad, text='Alterar', command='')
        self.b_busca["font"] = ("Arial", "10", "bold")
        self.b_busca.place(x=300, y=500)

        self.b_excluir = Button(self.cad, text='Excluir', command='')
        self.b_excluir["font"] = ("Arial", "10", "bold")
        self.b_excluir.place(x=400, y=500)

        self.b_sair = Button(self.cad, text='Sair', command=self.cad.destroy)
        self.b_sair["font"] = ("Arial", "10", "bold")
        self.b_sair.place(x=500, y=500)

        self.cad.mainloop()

#---------------------FUNÇÕES--------------------------------------------------------------------
    def pesquisa_cep_aluno(self):
        #OBS: HÁ A NECESSIDADE DE ACESSO A INTERNET PARA USAR ESTA FUNÇÃO
        try:
            print(self.n_cep.get())
            self.endereco = pycep_correios.consultar_cep(self.n_cep.get())
            print(self.endereco)
            print(self.endereco['cidade'])

            #limpa os Entrys para nao haja repetição em caso de varios cliks na função pesquisar
            self.n_cid.delete(0, END)
            self.n_uf.delete(0, END)
            self.n_bai.delete(0, END)
            self.n_rua.delete(0, END)

            self.n_cid.insert(END, self.endereco['cidade'])
            self.n_bai.insert(END, self.endereco['bairro'])
            self.n_uf.delete(0, END)
            self.n_uf.insert(END, self.endereco['uf'])
            self.n_rua.insert(END, self.endereco['end'])
        except:
            mb.showinfo('Aviso', 'Desculpe! talvez este CEP não exista ou você está sem acesso a internet. Por favor verifcar sua conexão ou o campo CEP.')
            print('CEP INVÁLIDO')
            print(sys.exc_info())

    def save_aluno(self):
        try:
            self.nome_aluno = self.n_nome.get().strip().title()
            self.cpf_aluno = self.n_cpf.get().strip()
            self.rg_aluno = self.n_rg.get().strip()
            self.nasc_aluno = self.dia.get() + '/' + self.mes.get()+ '/' + self.ano.get()
            self.sexo_aluno = self.n_sexo.get()
            self.esc_aluno = self.n_esc.get()
            self.sit_aluno = self.n_sit.get()
            self.hist_aluno = self.n_hist.get()

            self.nome_res = self.n_nome_resp.get().strip().title()
            self.cpf_res = self.n_nome_resp.get().strip
            self.fone_res = self.n_fone.get()

            self.cep_aluno = self.n_cep.get()
            self.cid_aluno = self.n_cid.get()
            self.uf_aluno = self.n_uf.get()
            self.bai_aluno = self.n_bai.get()
            self.rua_aluno = self.n_rua.get()
            self.casa_aluno = self.n_casa.get()

            print('ok')

        except:
            print('ERRO NA FUNÇÃO SALVAR PEGANDO OS DADOS DOS ENTRYS')
            print(sys.exc_info())


        try:
            con = sqlite3.connect('escola2.db')
            cursor = con.cursor()

            cursor.execute('''
                            INSERT INTO aluno(nm_aluno, nr_cpf, nr_rg, dta_nasc, escol, tp_sexo, sit,  hist)
                            VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                            '''%(self.nome_aluno,self.cpf_aluno,self.rg_aluno,self.nasc_aluno,self.esc_aluno,self.sexo_aluno,self.sit_aluno,self.hist_aluno))
            con.commit()


            #CASO FOR NECESSÁRIO VAI SER USADO O CADASTRO DO RESPONSÁVEL

            cursor.execute('''
                        INSERT INTO responsavel(nome_resp, cpf_resp, fone_resp)
                        VALUES ('%s', '%s', '%s')
                        '''%(self.nome_resp, self.cpf_resp, self.fone_res))

            cursor.execute('''
                        INSERT INTO endereco(cep, cidade, uf, bairro, rua, n_casa)
                        VALUES ('%s', '%s', '%s', '%s', '%s', '%s')
                        '''%(self.cep_aluno, self.cid_aluno, self.uf_aluno, self.bai_aluno, self.rua_aluno, self.casa_aluno))

            con.commit()
            mb.showinfo('SALVO', 'SALVO COM SUCESSO')
            con.close()

        except:

            mb.showerror('ERROR! DESCULPE NÃO FOI POSSIVEL SALVAR!', sys.exc_info()[1:])
            print(sys.exc_info())

        self.limpa_tela_aluno()

    def limpa_tela_aluno(self):
        self.n_nome.delete(0, END)
        self.n_rg.delete(0, END)
        self.n_cpf.delete(0, END)
        self.dia.delete(0, END)
        self.mes.delete(0, END)
        self.ano.delete(0, END)
        self.n_sexo.delete(0, END)
        self.n_uf.insert(END, 'Selecione')
        self.n_esc.delete(0, END)
        self.n_esc.insert(END, 'Selecione')
        self.n_sit.delete(0, END)
        self.n_sit.insert(END, 'Selecione')
        self.n_nome_resp.delete(0, END)
        self.n_cpf_resp.delete(0, END)
        self.n_fone.delete(0, END)
        self.n_cep.delete(0, END)
        self.n_cid.delete(0, END)
        self.n_uf.delete(0, END)
        self.n_uf.insert(END, 'Selecione')
        self.n_rua.delete(0, END)
        self.n_rua.delete(0, END)
        self.n_bai.delete(0, END)
        self.n_casa.delete(0, END)
        self.n_hist.delete(0, END)

    def pesquisa_aluno(self):
        con = sqlite3.connect('escola2.db')
        cursor = con.cursor()
        self.au = ('''SELECT nr_cpf, nm_aluno, nr_rg, dta_nasc, escol, tp_sexo, sit,  hist, id_aluno from aluno where nr_cpf = (?)''')
        self.sc = ''' SELECT cep, cidade, uf, bairro, rua, n_casa 
                      FROM endereco a
                      INNER JOIN aluno b on a.id_endereco = b.id_aluno '''
        self.x = self.n_cpf.get()
        cursor.execute(self.au, [self.n_cpf.get()])
        cursor.executescript(self.sc)
        busca = cursor.fetchall()
        for i in busca:
            if self.n_cpf.get() in i:
                self.n_cpf.delete(0, END)
                self.backup = i[0]
                self.n_cpf.insert(END, i[0])
                self.n_nome.insert(END, i[1])
                self.n_rg.insert(END, i[2])
                self.dia.insert(END, i[3])
                self.mes.insert(END, i[3])
                self.ano.insert(END, i[3])
                self.n_esc.delete(0, END)
                self.n_esc.insert(END, i[4])
                self.n_sexo.delete(0, END)
                self.n_sexo.insert(END, i[5])
                self.n_sit.delete(0, END)
                self.n_sit.insert(END, i[6])
                self.n_hist.delete(0, END)
                self.n_hist.insert(END, i[7])
                print(i[8])
                print(i)


                # self.n_uf.insert(END, 'Selecione')
                # self.n_esc.delete(0, END)
                # self.n_esc.insert(END, 'Selecione')
                # self.n_sit.delete(0, END)
                # self.n_sit.insert(END, 'Selecione')
                # self.n_nome_resp.delete(0, END)
                # self.n_cpf_resp.delete(0, END)
                # self.n_fone.delete(0, END)
                # self.n_cep.delete(0, END)
                # self.n_cid.delete(0, END)
                # self.n_uf.delete(0, END)
                # self.n_uf.insert(END, 'Selecione')
                # self.n_rua.delete(0, END)
                # self.n_rua.delete(0, END)
                # self.n_bai.delete(0, END)
                # self.n_casa.delete(0, END)
                # self.n_hist.delete(0, END)






    #-------------------TOP LEVEL FUNCIONÁRIO-----------------------------------

    def cadastro_funcionario(self):
        self.cadf = Toplevel(self.root)
        self.cadf.title('Cadastro de Funcionário')
        self.cadf.grid()
        self.cadf.focus_force()  #
        self.cadf.grab_set()  #
        self.cadf.geometry('600x350')
        self.cadf.resizable(width=False, height=False)

        self.lin = Label(self.cadf, text='-' * 150)
        self.lin.place(x=0, y=5)
        self.tt1 = Label(self.cadf, text='CADASTRO')
        self.tt1["font"] = ("Calibri", "13", "bold")
        self.tt1.place(x=0, y=5)

        self.nome_f = Label(self.cadf, text='Nome: ')
        self.nome_f.place(x=10, y=50)
        self.n_nome_f = Entry(self.cadf, width=80)
        self.n_nome_f.focus_force()
        self.n_nome_f.place(x=70, y=50)
        #self.n_nome_f.config(state='disabled')

        self.cpf_f = Label(self.cadf, text='CPF: ')
        self.cpf_f.place(x=10, y=100)
        self.n_cpf_f = Entry(self.cadf, width=45)
        self.n_cpf_f.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_cpf_f.place(x=70, y=100)

        self.rg_f = Label(self.cadf, text='RG: ')
        self.rg_f.place(x=350, y=100)
        self.n_rg_f = Entry(self.cadf, width=25)
        self.n_rg_f.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_rg_f.place(x=400, y=100)

        self.nasc_f = Label(self.cadf, text='Data de nascimento: ')
        self.nasc_f.place(x=10, y=150)
        self.n_nasc_f = Entry(self.cadf, width=32)
        self.n_nasc_f.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_nasc_f.place(x=150, y=150)

        self.sexo_f = Label(self.cadf, text='Sexo: ')
        self.sexo_f.place(x=350, y=150)
        self.itens = ['Selecione', 'MASCULINO', 'FEMININO']
        self.n_sexo_f = ttk.Combobox(self.cadf, width=22)
        self.n_sexo_f["values"] = self.itens
        self.n_sexo_f.current(0)
        self.n_sexo_f.bind("<<ComboboxSelected>>")
        self.n_sexo_f.place(x=400, y=150)

        self.fone_f = Label(self.cadf, text='Fone: ')
        self.fone_f.place(x=10, y=200)
        self.n_fone_f = Entry(self.cadf, width=30)
        self.n_fone_f.focus_force()  # MANTER O FOCO NO ENTRY
        self.n_fone_f.place(x=70, y=200)

        self.cargo = Label(self.cadf, text='Cargo: ')
        self.cargo.place(x=300, y=200)
        self.itens1 = ['Selecione', 'MASCULINO', 'FEMININO']
        self.n_cargo = ttk.Combobox(self.cadf, width=30)
        self.n_cargo["values"] = self.itens1
        self.n_cargo.current(0)
        self.n_cargo.bind("<<ComboboxSelected>>")
        self.n_cargo.place(x=350, y=200)

        self.b_save_f = Button(self.cadf, text='Salvar', command='')
        self.b_save_f["font"] = ("Arial", "10", "bold")
        self.b_save_f.place(x=90, y=300)

        self.b_limpa_f = Button(self.cadf, text='Limpar', command='')
        self.b_limpa_f["font"] = ("Arial", "10", "bold")
        self.b_limpa_f.place(x=190, y=300)

        self.b_busca_f = Button(self.cadf, text='Alterar', command='')
        self.b_busca_f["font"] = ("Arial", "10", "bold")
        self.b_busca_f.place(x=290, y=300)

        self.b_excluir_f = Button(self.cadf, text='Excluir', command='')
        self.b_excluir_f["font"] = ("Arial", "10", "bold")
        self.b_excluir_f.place(x=400, y=300)

        self.b_sair_f = Button(self.cadf, text='Sair', command=self.cadf.destroy)
        self.b_sair_f["font"] = ("Arial", "10", "bold")
        self.b_sair_f.place(x=500, y=300)

        self.cadf.mainloop()

    def run(self):
        self.lbr = Label(self.root)
        self.lbr.pack(side='top') #top, bottom, left, or right

        self.lbr['text'] = strftime('%H:%M:%S')  # formato de hora
        self.lbr['font'] = 'Helvita 10 bold'  # define a fonte do relogio
        self.lbr['foreground'] = 'black'  # define a cor dos numeros
        #self.lbr['bg'] = 'gray'  # define a cor do fundo bg e a abreviatura de background
        self.contador()

    #----------------RELOGIO USANDO THREDE----------------------------------------------------

    def contador(self):
        self.agora = strftime('%H:%M:%S')
        if self.lbr['text'] != self.agora:
            self.lbr['text'] = self.agora
        self.lbr.after(100, self.contador)



a = Tk()
b = Tela(a)
b.start()
a.mainloop()