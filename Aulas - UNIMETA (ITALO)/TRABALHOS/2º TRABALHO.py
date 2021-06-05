#busca de endereço por CEP necessita de acesso a internet
try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import pycep_correios

class Tela(Frame):
    def __init__(self,titulo, width, height):
        Frame.__init__(self, titulo, width=width, height=height)
        self.titulo = titulo
        self.titulo.title("Cadastro")
        self.grid()

class Campos(Tela):
    def __init__(self,titulo,width,height, x, y,nome):
        super().__init__(titulo, width,height)
        self.x = x
        self.y = y
        self.nome = nome

        self.entry = Entry(titulo, width=30)
        self.entry.place(x=self.x, y=self.y)
        self.label = Label(titulo, text=self.nome)
        self.label["font"] = ("Calibri", "12", "bold")
        self.label.place(x=self.x, y=self.y - 25)

class Pessoa(Campos):
    def __init__(self, titulo,width,height,x,y,nome,cpf='',nome_usr='',email='',rua='',num_casa='',bairro='',cidade='',estado='',cep='',nome_mae='',nome_pai=None):
        super().__init__(titulo, width, height, x, y, nome)

        self.cpf = cpf
        self.nome_usr = nome_usr
        self.email = email
        self.rua = rua
        self.num_casa = num_casa
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.nome_mae = nome_mae
        self.nome_pai = nome_pai

        tit = Label(titulo, text="Cadastro")
        tit["font"] = ("Calibri", "12", "bold")
        tit.place(x=150, y=0)

        self.bt = Button(text='Salvar', command=self.salvar)
        self.bt.place(x=100, y=420)

        self.btn = Button(text='Limpar', command=self.limpa)
        self.btn.place(x=190, y=420)

        self.btnc = Button(titulo, text='Buscar', command=self.pesquisa_cep, bg='green')
        self.btnc.place(x=230, y=225)

        self.btnc = Button(titulo, text='Buscar dados', command=self.pesquisa, bg='red')
        self.btnc.place(x=390, y=420)

#esta incompleta,  nao consegui terminar a tempo
    def pesquisa(self):
        try:
            arq = open('teste.txt', 'a')
            self.lista = arq.readlines()
            for i in range(0,len(self.lista),11):
                x = str((self.lista[i])[5:16])
                if app.entry.get().strip()==(self.lista[i])[5:16]:
                    self.lista[i+1] = (f'Nome: {app1.entry.get().strip().upper()}\n')
                    self.lista[i+2] = (f'E-mail: {app2.entry.get()}\n')
                    self.lista[i+3] = (f'Mae: {app3.entry.get().strip().upper()}\n')

                    if app4.entry.get() is '':
                        app4.entry.insert(END, 'Nao informado')
                    self.lista[i+10] = (f'Pai: {app4.entry.get().strip.upper()}\n')
                    return 1
            arq.close()
        except:
            return 2



    def salvar(self):

        try:
            arq = open('teste.txt', 'a')
            arq.write(f'CPF: {app.entry.get().strip()}') #strip é para remover caso haja espaços antes da digitação
            arq.write(f'\nNome: {app1.entry.get().strip().upper()}')#upper é para padronizar todos os dados com letrs maiusculas
            arq.write(f'\nE-mail: {app2.entry.get()}')
            arq.write(f'\nMae: {app3.entry.get().strip().upper()}')
            arq.write(f'\nPai: {app4.entry.get().strip().upper()}')
            arq.write(f'\nCep: {app5.entry.get()}')
            arq.write(f'\nCidade: {app6.entry.get().strip().upper()}')
            arq.write(f'\nEstado: {app7.combo.get()}')
            arq.write(f'\nRua: {app8.entry.get().strip().upper()}')
            arq.write(f'\nBairro: {app9.entry.get().strip().upper()}')
            arq.write(f'\nNº Casa: {app10.entry.get()}')
            arq.write('\n---------------------------------\n')
            arq.close()
            mb.showinfo('Aviso', 'Dados Salvos com Sucesso')
            print('Salvo')

            if self.combo['values'] == ['Selecione']:
                print('selecione a UF')
                mb.showinfo('Aviso', 'FALTA DE UF')



            app.entry.delete(0, END)
            app1.entry.delete(0, END)
            app2.entry.delete(0, END)
            app3.entry.delete(0, END)
            app4.entry.delete(0, END)
            app5.entry.delete(0, END)
            app6.entry.delete(0, END)
            app7.combo.delete(0, END)
            app8.entry.delete(0, END)
            app9.entry.delete(0, END)
            app10.entry.delete(0, END)


        except:
            mb.showinfo('Aviso', 'Aconteceu um erro por favor verifique os campos.')
            print('Erro')

    def limpa(self):
        app.entry.delete(0, END)
        app1.entry.delete(0, END)
        app2.entry.delete(0, END)
        app3.entry.delete(0, END)
        app4.entry.delete(0, END)
        app5.entry.delete(0, END)
        app6.entry.delete(0, END)
        app7.combo.delete(0, END)
        app8.entry.delete(0, END)
        app9.entry.delete(0, END)
        app10.entry.delete(0, END)

    def pesquisa_cep(self):
        #OBS: HÁ A NECESSIDADE DE ACESSO A INTERNET PARA USAR ESTA FUNÇÃO
        try:
            print(app5.entry.get())
            endereco = pycep_correios.consultar_cep(app5.entry.get())
            print(endereco)
            print(endereco['cidade'])

            #limpa os Entrys para nao haja repetição em caso de varios cliks na função pesquisar
            app6.entry.delete(0, END)
            app7.combo.delete(0, END)
            app8.entry.delete(0, END)
            app9.entry.delete(0, END)


            app9.entry.insert(END, endereco['bairro'])
            app6.entry.insert(END, endereco['cidade'])
            app7.combo.delete(0, END)
            app7.combo.insert(END, endereco['uf'])
            app8.entry.insert(END, endereco['end'])
        except:
            mb.showinfo('Aviso', 'Desculpe! talvez este Cep não exista ou você está sem acesso a internte. Por favor verifcar sua conexão ou o campo CEP.')
            print('CEP INVÁLIDO')




class Box(Campos):
    def __init__(self,titulo,width,height,x,y,nome,itens=''):
        super().__init__(titulo, width, height, x, y, nome)
        self.itens = itens

        self.itens = ['Selecione', 'AC', 'AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS'
        ,'MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']
        self.combo = ttk.Combobox(titulo, width=30)
        self.combo["values"] = self.itens
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>")
        self.combo.place(x=self.x, y=self.y)



root = Tk()
app = Pessoa(root,600,70,20,50,"CPF:")
app1 = Pessoa(root,600,40,350,50,"Nome:")
app2 = Pessoa(root,600,40,20,100,"E-mail:")
app3 = Pessoa(root,600,40,350,100,"Mae:")
app4 = Pessoa(root,600,40,20,150,"Pai:")
app5 = Pessoa(root,600,40,20,230,"Cep:")
app6 = Pessoa(root,600,40,20,290,"Cidade:")
app7 = Box(root,600,40,350,290,"Estado:")
app8 = Pessoa(root,600,40,350,230,"Rua:")
app9 = Pessoa(root,600,40,20,360,"Bairro:")
app10 = Pessoa(root,600,50,350,360,"Numero casa:")
btn = Button(root,text='Fechar',command=root.destroy).place(x=280, y=420)
root.mainloop()
