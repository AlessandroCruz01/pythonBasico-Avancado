from tkinter import ttk
from tkinter import*
from tkinter import messagebox as mb

class Master(Frame):
    def __init__(self, master, width, height):
        Frame.__init__(self, master, width=width, height=height,bg='light blue')
        self.master = master
        self.run()

    def run(self):
        self.master.title("Janela Cadastro")
        self.grid()

class User(Master):
    def __init__(self,master,width,height, x, y,nome1):
        super().__init__(master,width,height)
        self.x = x
        self.y = y
        self.nome1 = nome1

        self.entry = Entry(master,width= 30)
        self.entry.place(x= self.x, y= self.y)
        self.label = Label(master,text= self.nome1,bg='light blue')
        self.label.place(x=self.x, y=self.y-25)
class Pessoa(User):
    def __init__(self,master,width,height,x,y,nome1,cpf='',nome='',email='',rua='',num_casa='',bairro='',cidade='',estado='',cep='',nome_mae='',nome_pai=None):
        super().__init__(master,width,height ,x, y,nome1)

        
        self.cpf =cpf
        self.nome = nome
        self.email = email
        self.rua = rua
        self.num_casa = num_casa
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.nome_mae = nome_mae
        self.nome_pai =nome_pai
        titulo = Label(master, text="Formulario de Cadastro",bg='light blue')
        titulo["font"] = ("Calibri", "12", "bold")
        titulo.place(x=150,y=0)
        
        self.bt = Button(text='Salvar', command=self.salva)
        self.bt.place(x=100, y=420)
        self.btn = Button(text='Limpar', command=self.clear)
        self.btn.place(x=190, y=420)
    def salva(self):
        
        arq = open('Arquivo.txt', 'a')
        arq.write(f'CPF: {app.entry.get()}')
        arq.write(f'\nNome: {app1.entry.get()}')
        arq.write(f'\nE-mail: {app2.entry.get()}')
        arq.write(f'\nRua: {app3.entry.get()}')
        arq.write(f'\nNº Casa: {app4.entry.get()}')
        arq.write(f'\nBairro: {app5.entry.get()}')
        arq.write(f'\nCidade: {app6.entry.get()}')
        arq.write(f'\nEstado: {app7.combo.get()}')
        arq.write(f'\nCEP: {app8.entry.get()}')
        arq.write(f'\nMae: {app9.entry.get()}')
        arq.write(f'\nPai: {app10.entry.get()}')
        arq.write('\n---------------------------------\n')
        arq.close()
        mb.showinfo('Aviso', 'Dados Salvos com Sucesso')
        
    def clear(self):
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
class Box(User):
    def __init__(self,master,width,height,x,y,nome1,itens=''):
        super().__init__(master, width, height, x, y, nome1)
        self.itens = itens

        self.itens = ['Selecione','Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo',
                 'Goiás', 'Maranhão', 'Mato Grosso',
                 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí',
                 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul',
                 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
        self.combo = ttk.Combobox(master,width=30)
        self.combo["values"] = self.itens
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>")
        self.combo.place(x= self.x, y= self.y)
root = Tk()
app = Pessoa(root,500,70,20,50,"CPF:")
app1 = Pessoa(root,500,40,250,50,"Nome:")
app2 = Pessoa(root,500,40,20,110,"E-mail:")
app3 = Pessoa(root,500,40,20,170,"Rua:")
app4 = Pessoa(root,500,40,250,170,"Numero casa:")
app5 = Pessoa(root,500,40,20,230,"Bairro:")
app6 = Pessoa(root,500,40,20,290,"Cidade:")
app7 = Box(root,500,40,250,290,"Estado:")
app8 = Pessoa(root,500,40,250,230,"CEP:")
app9 = Pessoa(root,500,40,20,360,"Mae:")
app10 = Pessoa(root,500,50,250,360,"Pai:")
btn = Button(root,text='Fechar',command=root.destroy).place(x=280, y=420)
root.mainloop()
