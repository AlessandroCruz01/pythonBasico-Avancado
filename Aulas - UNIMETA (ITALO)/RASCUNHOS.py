# #
# # try:
# #     from tkinter import *
# # except ImportError:
# #     from Tkinter import *
# #
# # tela = Tk()
# # tela.title('Aprende porra')
# # tela.geometry('544x522')
# #
# #
# #
# # matriz = [[False for i in range(8)] for i in range (8)]
# #
# #
# # #NO TKINTER HÁ 3 FORMAS DE INDICAR POSIÇÕES: place (dá a posiçao x,y) , pack , grid (divide em grade)
# #
# #
# # # #CRIANDO TABULEIRO:
# # #
# # # b1 = Button(tela, height=4, width=6, bg='black', command='')
# # # b1.grid(row=1,  column=1)
# # #
# # # b2 = Button(tela, height=4, width=6, bg='red', command='')
# # # b2.grid(row=1 ,  column=2)#ROW = LINHA / COLUNM = COLUNA
# #
# # i = 0
# #
# # for x in range(8):
# #     for y  in range(8):
# #
# #         if (x+i)%2==0:
# #             b1 = Button(tela, height=3, width=5, bg='red', command='')
# #             b1.grid(row=x,  column=y)
# #
# #
# #         else:
# #
# #             b1 = Button(tela, height=3, width=5, bg='black', command='')
# #             b1.grid(row=x, column=y)
# #
# #         i +=1
# #
# # for x in range(3):
# #     for y  in range(8):
# #
# #
# #             b1 = Button(tela, height=1, width=3, bg='Blue', command='')
# #             b1.grid(row=x,  column=y)
# #
# # def posicao(event):
# #     print("(%s, %s)"%(event.x_root,event.y_root))
# #
# # tela.bind("<Button-1>", posicao)
# #
# #
# #
# # tela.mainloop()
#
#
#
#
# # try:
# #     from tkinter import *
# # except ImportError:
# #     from Tkinter import *
# #
# # from random import *
# #
# # principal = Tk()
# # principal.geometry("500x500")
# #
# # cores = ('yellow', 'green', 'orange', 'blue', 'black', 'grey', 'pink')
# # class Quadrado():
# #     def __init__(self, principal):
# #         self.x = randint(0, 400)
# #         self.y = randint(0, 400)
# #         cor = cores[randint(0, len(cores)-1)]
# #
# #         self.principal = principal
# #         self.quadrado = Canvas(principal, width=100, height=100)
# #         self.quadrado.place(x=self.x, y=self.y)
# #         self.quadrado.create_rectangle(0,0,100,100, fill=cor, outline = cor)
# #
# # a = Quadrado(principal)
# #
# # principal.mainloop()
# #
# # import _sqlite3
# #
# # con = _sqlite3.connect('rasc.db')
# # c = con.cursor()
# #
# # c.execute('''create table Rascunho (
# # pessoas text,
# # data text);''')
# #
# # con.commit()
# #
# #
# # import sys
# # from PyQt4 import QtGui
# # def window():
# #     app = QtGui.QApplication(sys.argv)
# #     w = QtGui.QWidget()
# #     b= QtGui.QLabel(w)
# #     b.setText("Hello World!")
# #     w.setGeometry(100,100,200,50)
# #     b.move(50,20)
# #     w.setWindowTitle(“PyQt”)
# #     w.show()
# #     sys.exit(app.exec_())
# # if __name__ == '__main__':
# #     window()
# #
#
# import calendar
# import datetime
# import sys
#
# if sys.version[0] == '2':
#     import Tkinter as tk
# else:
#     import tkinter as tk
#
#
# class Calendar:
#     def __init__(self, parent, values):
#         self.values = values
#         self.parent = parent
#         self.cal = calendar.TextCalendar(calendar.SUNDAY)
#         self.year = datetime.date.today().year
#         self.month = datetime.date.today().month
#         self.wid = []
#         self.day_selected = 1
#         self.month_selected = self.month
#         self.year_selected = self.year
#         self.day_name = ''
#
#         self.setup(self.year, self.month)
#
#     def clear(self):
#         for w in self.wid[:]:
#             w.grid_forget()
#             # w.destroy()
#             self.wid.remove(w)
#
#     def go_prev(self):
#         if self.month > 1:
#             self.month -= 1
#         else:
#             self.month = 12
#             self.year -= 1
#         # self.selected = (self.month, self.year)
#         self.clear()
#         self.setup(self.year, self.month)
#
#     def go_next(self):
#         if self.month < 12:
#             self.month += 1
#         else:
#             self.month = 1
#             self.year += 1
#
#         # self.selected = (self.month, self.year)
#         self.clear()
#         self.setup(self.year, self.month)
#
#     def selection(self, day, name):
#         self.day_selected = day
#         self.month_selected = self.month
#         self.year_selected = self.year
#         self.day_name = name
#
#         # data
#         self.values['day_selected'] = day
#         self.values['month_selected'] = self.month
#         self.values['year_selected'] = self.year
#         self.values['day_name'] = name
#         self.values['month_name'] = calendar.month_name[self.month_selected]
#
#         self.clear()
#         self.setup(self.year, self.month)
#
#     def setup(self, y, m):
#         left = tk.Button(self.parent, text='<', command=self.go_prev)
#         self.wid.append(left)
#         left.grid(row=0, column=1)
#
#         header = tk.Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
#         self.wid.append(header)
#         header.grid(row=0, column=2, columnspan=3)
#
#         right = tk.Button(self.parent, text='>', command=self.go_next)
#         self.wid.append(right)
#         right.grid(row=0, column=5)
#
#         days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#         for num, name in enumerate(days):
#             t = tk.Label(self.parent, text=name[:3])
#             self.wid.append(t)
#             t.grid(row=1, column=num)
#
#         for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
#             for d, day in enumerate(week):
#                 if day:
#                     # print(calendar.day_name[day])
#                     b = tk.Button(self.parent, width=1, text=day,
#                                   command=lambda day=day: self.selection(day, calendar.day_name[(day - 1) % 7]))
#                     self.wid.append(b)
#                     b.grid(row=w, column=d)
#
#         sel = tk.Label(self.parent, height=2, text='{} {} {} {}'.format(
#             self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
#         self.wid.append(sel)
#         sel.grid(row=8, column=0, columnspan=7)
#
#         ok = tk.Button(self.parent, width=5, text='OK', command=self.kill_and_save)
#         self.wid.append(ok)
#         ok.grid(row=9, column=2, columnspan=3, pady=10)
#
#     def kill_and_save(self):
#         self.parent.destroy()
#
#
# if __name__ == '__main__':
#     class Control:
#         def __init__(self, parent):
#             self.parent = parent
#             self.choose_btn = tk.Button(self.parent, text='Choose', command=self.popup)
#             self.show_btn = tk.Button(self.parent, text='Show Selected', command=self.print_selected_date)
#             self.choose_btn.grid()
#             self.show_btn.grid()
#             self.data = {}
#
#         def popup(self):
#             child = tk.Toplevel()
#             cal = Calendar(child, self.data)
#
#         def print_selected_date(self):
#             print(self.data)
#
#
#     root = tk.Tk()
#     app = Control(root)
#     root.mainloop()
#
#
# class Pessoa(object):
#     def __init__(self, nome, idade, salario):
#         self._nome = nome
#         self._idade = idade
#         self._salario = salario
#
#     @property
#     def nome(self):
#         print('get do nome')
#         return self._nome
#
#     @nome.setter
#     def nome(self, nome):
#         print('set do nome', nome)
#         self._nome = nome
#
#     @property
#     def idade(self):
#         print('get da idade')
#         return self._idade
#
#     @idade.setter
#     def idade(self, idade):
#         print('set da idade', idade)
#         self._idade = idade
#
#     @property
#     def salario(self):
#         print('get do salario')
#         return self._salario
#
#     @salario.setter
#     def salario(self, salario):
#         print('set do salario', salario)
#         self._salario = salario
#
#
# pessoa = Pessoa('Miguel', 30, 50)
# print(pessoa.__dict__) # valores iniciais
# pessoa.nome = 'Afonso'
# pessoa.idade = 20
# pessoa.salario = 500
# print(pessoa.nome)
# print(pessoa.idade)
# print(pessoa.salario)
#
# import pycep_correios
#
# endereco = pycep_correios.consultar_cep('69906418')
#
# print(endereco)
#
# from tkinter import *
#
# # Guarda as configurações padrão para os
# # botões que serão definidos mais tarde
# button_default_config = {
#     "font": "Arial 10 normal",
#     "bg": "gray",
#     "fg": "white"
# }
#
#
# class Window(Frame):
#     """ Janela principal """
#
#     def __init__(self):
#         """ Método construtor da janela"""
#         super().__init__(master=None)  # Aqui iniciamos a nossa superclasse (Frame)
#
#         # Definições de titulos, largura
#         # e altura da janela principal
#         self.master.geometry("800x600")
#         self.master.title("MainWindow")
#
#         # Para os botões, definimos o texto e depois passamos o
#         # dicionario de atributos usando "**" para o botão
#         button1 = Button(self, text="Button1", **button_default_config)
#
#         # Coloque cada botão em seu lugar e defina o
#         # preenchimento dele usando o NSEW que significa
#         # que o botão irá se ajustar ao tamanho dos items
#         # ao seu redor e dentro da sua própria celula.
#         button1.grid(row=0, column=0, pady=40, sticky=NSEW)
#
#         # Ao criar outro botão devemos fazer da mesma forma
#         # para que fique tudo igual, passaremos o mesmo
#         # dicionário de attributos que passamos ao primeiro
#         button2 = Button(self, text="Button2", **button_default_config)
#
#         # Definimos outra fonte ao 2° botão, pois
#         # as celulas irão se ajustar automaticamente
#         button2.configure(font="Arial 20 normal")
#
#         # Configurando novamente o grid
#         button2.grid(row=0, column=1, pady=40, sticky=NSEW)
#
#         # Essa é a parte mais importante, pois, define o
#         # esticamento de cada celula do grid. Se possivel
#         # comente as 2 linhas abaixo e teste para entender melhor
#         self.columnconfigure(0, weight=1)
#         self.columnconfigure(1, weight=1)
#
#         # Epacotamos o frame na janela
#         self.pack(fill=BOTH, expand=True)
#
#
# if __name__ == '__main__':
#     window = Window()
#     window.mainloop()


#
# from tkinter import *
# c = Canvas()
# c.pack()
# def novalinha(e):
#  x,y = c.canvasx(e.x), c.canvasy(e.y)
#  c.create_line(x,y,x,y,tags="corrente")
# def estendelinha(e):
#  x,y = c.canvasx(e.x), c.canvasy(e.y)
#  coords = c.coords("corrente") + [x,y]
#  c.coords("corrente",*coords)
# def fechalinha(e): c.itemconfig("corrente",tags=())
# c.bind("<Button-1>", novalinha)
# c.bind("<B1-Motion>", estendelinha)
# c.bind("<ButtonRelease-1>", fechalinha)
# c.pack()
#
#
#
# import gi
# gi.require_version('Gtk', '3.0')
# from gi.repository import Gtk, GLib
#
# class EntryWindow(Gtk.Window):
#
#     def __init__(self):
#         Gtk.Window.__init__(self, title="Entry Demo")
#         self.set_size_request(200, 100)
#
#         self.timeout_id = None
#
#         vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
#         self.add(vbox)
#
#         self.entry = Gtk.Entry()
#         self.entry.set_text("Hello World")
#         vbox.pack_start(self.entry, True, True, 0)
#
#         hbox = Gtk.Box(spacing=6)
#         vbox.pack_start(hbox, True, True, 0)
#
#         self.check_editable = Gtk.CheckButton("Editable")
#         self.check_editable.connect("toggled", self.on_editable_toggled)
#         self.check_editable.set_active(True)
#         hbox.pack_start(self.check_editable, True, True, 0)
#
#         self.check_visible = Gtk.CheckButton("Visible")
#         self.check_visible.connect("toggled", self.on_visible_toggled)
#         self.check_visible.set_active(True)
#         hbox.pack_start(self.check_visible, True, True, 0)
#
#         self.pulse = Gtk.CheckButton("Pulse")
#         self.pulse.connect("toggled", self.on_pulse_toggled)
#         self.pulse.set_active(False)
#         hbox.pack_start(self.pulse, True, True, 0)
#
#         self.icon = Gtk.CheckButton("Icon")
#         self.icon.connect("toggled", self.on_icon_toggled)
#         self.icon.set_active(False)
#         hbox.pack_start(self.icon, True, True, 0)
#
#     def on_editable_toggled(self, button):
#         value = button.get_active()
#         self.entry.set_editable(value)
#
#     def on_visible_toggled(self, button):
#         value = button.get_active()
#         self.entry.set_visibility(value)
#
#     def on_pulse_toggled(self, button):
#         if button.get_active():
#             self.entry.set_progress_pulse_step(0.2)
#             # Call self.do_pulse every 100 ms
#             self.timeout_id = GLib.timeout_add(100, self.do_pulse, None)
#         else:
#             # Don't call self.do_pulse anymore
#             GLib.source_remove(self.timeout_id)
#             self.timeout_id = None
#             self.entry.set_progress_pulse_step(0)
#
#     def do_pulse(self, user_data):
#         self.entry.progress_pulse()
#         return True
#
#     def on_icon_toggled(self, button):
#         if button.get_active():
#             icon_name = "system-search-symbolic"
#         else:
#             icon_name = None
#         self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY,
#             icon_name)
#
# win = EntryWindow()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()
#
# import tkinter as tk
#
# def startgame():
#     pass
#
# mw = tk.Tk()              #Here I tried (1)
# mw.title('The game')
#
# back = tk.Frame(master=mw, width=500, height=500, bg='black')
# back.pack()
#
# go = tk.Button(master=back, text='Start Game', bg='black', fg='red',
#                      command=lambda:startgame()).pack()
# close = tk.Button(master=back, text='Quit', bg='black', fg='red',
#                      command=lambda:quit()).pack()
# info = tk.Label(master=back, text='Made by me!', bg='red',
#                          fg='black').pack()
#
# mw.mainloop()

# from tkinter import *
#
# root=Tk()
#
# # Windows
# root.state('zoomed')
#
# # Linux
# #root.attributes('-zoomed', True)
#
# root.iconify()
# root.mainloop()

# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
#
#
# t1 = np.arange(0.0, 3.0, 0.01)
#
# ax1 = plt.subplot(212)
# ax1.margins(0.05)           # Default margin is 0.05, value 0 means fit
# ax1.plot(t1, f(t1))
#
# ax2 = plt.subplot(221)
# ax2.margins(2, 2)           # Values >0.0 zoom out
# ax2.plot(t1, f(t1))
# ax2.set_title('Zoomed out')
#
# ax3 = plt.subplot(222)
# ax3.margins(x=0, y=-0.25)   # Values in (-0.5, 0.0) zooms in to center
# ax3.plot(t1, f(t1))
# ax3.set_title('Zoomed in')
#
# plt.show()
#
# from tkinter import *
# root = Tk()
# # root.attributes('-fullscreen', True)

# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w, h))

# def resize(event):
#     print("New size is: {}x{}".format(event.width, event.height))
#
# root.bind("<Configure>", resize)
#
# root.state('zoomed')
#
# root.mainloop()

# from tkinter import *
#
# def on_write(*args):
#     s = var.get()
#     if len(s) > 0:
#         if not s[-1].isdigit(): # retirar ultimo caracter caso nao seja digito
#             var.set(s[:-1])
#         else: # aproveitar apenas os primeiros 5 chars
#             var.set(s[:max_len])
#
# root = Tk()
# max_len = 5 # maximo num de caracteres
# var = StringVar()
# var.trace("w", on_write) # rastrear valor da variavel e executar funcao de validacao quando mudar
#
# entrada = Entry(root, textvariable=var)
# entrada.pack()
# root.mainloop()

# from tkinter import *
# from sqlite3 import *
#
# class criar(object):
#     def __init__(self, principal):
# #frames e empacotamento de frames
#         self.frame1 = Frame(principal)
#         self.frame1.place()
#         self.frame1.pack()
#         self.frame2 = Frame(principal)
#         self.frame2.place()
#         self.frame2.pack()
#         self.subFrameOptions = Frame(self.frame2)
#         self.subFrameOptions.place()
#         self.subFrameOptions.pack()
# #texto exibido na tela
#         L1 = Label(self.frame1, text = "Nome do Seu Banco de Dado")
#         L1.place(x = 10,y = 10)
#         L1.pack()
#         E1 = Entry(self.frame1, bd = 5, )
#         E1.place(x = 60,y = 10)
#         E1.pack()
# #checkButtons
#         self.nome = Checkbutton(self.subFrameOptions, bd = 5, text = 'Nome', variable = Vnome)
#         self.nome.pack(side = LEFT)
#         Vnome.get()
#         self.cor = Checkbutton(self.subFrameOptions, bd = 5, text = 'Cor', variable = Vcor)
#         self.cor.pack(side = LEFT)
#         Vcor.get()
#         self.cpf = Checkbutton(self.subFrameOptions, bd = 5, text = 'CPF', variable = Vcpf)
#         self.cpf.pack(side = LEFT)
#         Vcpf.get()
#         self.email = Checkbutton(self.subFrameOptions, bd = 5, text = 'Email', variable = Vemail)
#         self.email.pack(side = LEFT)
#         Vemail.get()
#
#
# principal = Tk()
# #variaveis dos metodos dos checkButtons
# Vnome = IntVar()
# Vcor = IntVar()
# Vcpf = IntVar()
# Vemail = IntVar()
# #cria a instancia
# criar(principal)
# principal.geometry('400x300')
# principal.title("Gerenciador de Cadastro")
# principal.mainloop()

# !/usr/bin/python
# -*-coding: utf-8-*-
#
# from tkinter import *
# from calendar import monthcalendar as mc
# import time
#
# root = Tk()
#
#
# class calendario(object):
#     def selec_data(self, event=None):
#         try:
#             if self.wid:
#                 self.wid.configure(relief=FLAT)
#         except:
#             pass
#         self.wid = event.widget
#         data = []
#         data.append(self.wid["text"])
#         data.append(self.mes)
#         data.append(self.ano)
#         self.wid.configure(relief=SUNKEN)
#         return data  # Retona a data numa lista no formato dia, mes, ano, [00, 00, 0000]
#
#
# def soma_mes(self):
#     self.mes = self.mes + 1
#     if self.mes > 12:
#         self.mes = 1
#         self.ano = self.ano + 1
#     self.widgets(self.mes, self.ano)
#
#
# def subtrai_mes(self):
#     self.mes -= 1
#     if self.mes < 1:
#         self.mes = 12
#         self.ano -= 1
#     self.widgets(self.mes, self.ano)
#
#
# def soma_ano(self):
#     self.ano += 1
#     self.widgets(self.mes, self.ano)
#
#
# def subtrai_ano(self):
#     self.ano -= 1
#     self.widgets(self.mes, self.ano)
#
#
# def ret_hoje(self, event=None):
#     self.tempo = time.localtime()
#     self.mes = int(self.tempo[1])
#     self.ano = int(self.tempo[0])
#     self.dia = int(self.tempo[2])
#     self.widgets(self.mes, self.ano, self.dia)
#
#
# def cal(self, master=None, mes=None, ano=None, dia=None):
#     self.f = Frame(master, height=40)
#     self.f.grid()
#     self.f1 = Frame(self.f)
#     self.f1.grid(row=0, column=0, sticky=N)
#     self.f2 = Frame(self.f)
#     self.f2.grid(row=2, column=0)
#     self.widgets(mes, ano, dia)
#     li = Button(self.f2, text='<<', command=self.subtrai_ano, width=1)
#     li.grid(row=0, column=0, sticky=W + S)
#     li1 = Button(self.f2, text='<', command=self.subtrai_mes, width=1)
#     li1.grid(row=0, column=1, sticky=E + S)
#     re = Button(self.f2, text='>', command=self.soma_mes, width=1)
#     re.grid(row=0, column=3, sticky=W + S)
#     re1 = Button(self.f2, text='>>', command=self.soma_ano, width=1)
#     re1.grid(row=0, column=4, sticky=E + S)
#
#
# def widgets(self, mes=None, ano=None, dia=None):
#     try:
#         if self.f3:
#             self.f3.destroy()
#     except:
#         pass
#     self.var1 = StringVar()
#     mes2 = str(mes)
#     if len(mes2) == 1:
#         mes2 = str(0) + mes2
#
#     ym = mes2 + '/' + str(ano)
#     self.var1.set(ym)
#     self.ano_mes = Label(self.f2, textvariable=self.var1, cursor="watch")
#
#     self.ano_mes.grid(row=0, column=2)
#     self.ano_mes.bind("<Button-1>", self.ret_hoje)
#     self.f3 = Frame(self.f)
#     self.f3.grid(row=1, column=0)
#     x = mc(ano, mes)
#     dias = ("S", "T", "Q", "Q", "S", "S", "D")
#     for n in range(7):
#         v = StringVar()
#         l = Label(self.f3, textvariable=v)
#         l.grid(row=0, column=n)
#         v.set(dias[n])
#     for n in range(7):
#         for o in range(len(x)):
#             var = StringVar()
#             if x[o][n] == 0:
#                 b = Label(self.f3, text=" ", width=3)
#                 b.grid(column=n, row=o + 1)
#             else:
#                 b = Label(self.f3, textvariable=var, foreground="blue", width=3, takefocus=1)
#
#                 if n == 5 or n == 6:
#                     b.configure(fg="red")
#                 b.bind("<Button-1>", self.selec_data)
#                 b.grid(column=n, row=o + 1)
#                 var.set(x[o][n])
#                 if x[o][n] == dia:
#                     b.configure(bg="brown")
#         if len(x) == 5:
#             for n in range(7):
#                 l = Label(self.f3, text="  ")
#                 l.grid(row=o + 2, column=n)
#         if len(x) == 4:
#             for n in range(7):
#                 l = Label(self.f3, text="  ")
#                 l.grid(row=o + 2, column=n)
#                 l = Label(self.f3, text="  ")
#                 l.grid(row=o + 3, column=n)
#
#
# def __init__(self, master=None):
#     self.tempo = time.localtime()
#     self.mes = int(self.tempo[1])
#     self.ano = int(self.tempo[0])
#     self.dia = int(self.tempo[2])
#     self.cal(master, self.mes, self.ano, self.dia)
#
#
# if __name__ == "__main__":
#     root.title("Calendário")
#     root.geometry("200x170")
#     calendario(root)
#     root.mainloop()
#
# import calendar
# import datetime
# import sys
#
# if sys.version[0] == '2':
#     import Tkinter as tk
# else:
#     import tkinter as tk
#
#
# class Calendar:
#     def __init__(self, parent, values):
#         self.values = values
#         self.parent = parent
#         self.cal = calendar.TextCalendar(calendar.SUNDAY)
#         self.year = datetime.date.today().year
#         self.month = datetime.date.today().month
#         self.wid = []
#         self.day_selected = 1
#         self.month_selected = self.month
#         self.year_selected = self.year
#         self.day_name = ''
#
#         self.setup(self.year, self.month)
#
#     def clear(self):
#         for w in self.wid[:]:
#             w.grid_forget()
#             # w.destroy()
#             self.wid.remove(w)
#
#     def go_prev(self):
#         if self.month > 1:
#             self.month -= 1
#         else:
#             self.month = 12
#             self.year -= 1
#         # self.selected = (self.month, self.year)
#         self.clear()
#         self.setup(self.year, self.month)
#
#     def go_next(self):
#         if self.month < 12:
#             self.month += 1
#         else:
#             self.month = 1
#             self.year += 1
#
#         # self.selected = (self.month, self.year)
#         self.clear()
#         self.setup(self.year, self.month)
#
#     def selection(self, day, name):
#         self.day_selected = day
#         self.month_selected = self.month
#         self.year_selected = self.year
#         self.day_name = name
#
#         # data
#         self.values['day_selected'] = day
#         self.values['month_selected'] = self.month
#         self.values['year_selected'] = self.year
#         self.values['day_name'] = name
#         self.values['month_name'] = calendar.month_name[self.month_selected]
#
#         self.clear()
#         self.setup(self.year, self.month)
#
#     def setup(self, y, m):
#         left = tk.Button(self.parent, text='<', command=self.go_prev)
#         self.wid.append(left)
#         left.grid(row=0, column=1)
#
#         header = tk.Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
#         self.wid.append(header)
#         header.grid(row=0, column=2, columnspan=3)
#
#         right = tk.Button(self.parent, text='>', command=self.go_next)
#         self.wid.append(right)
#         right.grid(row=0, column=5)
#
#         days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#         for num, name in enumerate(days):
#             t = tk.Label(self.parent, text=name[:3])
#             self.wid.append(t)
#             t.grid(row=1, column=num)
#
#         for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
#             for d, day in enumerate(week):
#                 if day:
#                     # print(calendar.day_name[day])
#                     b = tk.Button(self.parent, width=1, text=day,
#                                   command=lambda day=day: self.selection(day, calendar.day_name[(day - 1) % 7]))
#                     self.wid.append(b)
#                     b.grid(row=w, column=d)
#
#         sel = tk.Label(self.parent, height=2, text='{} {} {} {}'.format(
#             self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
#         self.wid.append(sel)
#         sel.grid(row=8, column=0, columnspan=7)
#
#         ok = tk.Button(self.parent, width=5, text='OK', command=self.kill_and_save)
#         self.wid.append(ok)
#         ok.grid(row=9, column=2, columnspan=3, pady=10)
#
#     def kill_and_save(self):
#         self.parent.destroy()
#
#
# if __name__ == '__main__':
#     class Control:
#         def __init__(self, parent):
#             self.parent = parent
#             self.choose_btn = tk.Button(self.parent, text='Choose', command=self.popup)
#             self.show_btn = tk.Button(self.parent, text='Show Selected', command=self.print_selected_date)
#             self.choose_btn.grid()
#             self.show_btn.grid()
#             self.data = {}
#
#         def popup(self):
#             child = tk.Toplevel()
#             cal = Calendar(child, self.data)
#
#         def print_selected_date(self):
#             print(self.data)
#
#
#     root = tk.Tk()
#     app = Control(root)
#     root.mainloop()

# import sys
# try:
#  cpflimpo=sys.argv[1]
# except IndexError:
#  print ("Use %s NUMERO_DO_CPF" % sys.argv[0])
#  sys.exit()
#
# if (len(cpflimpo) != 11 or not cpflimpo.isdigit()):
#  print ("Formato errado. Tente de novo (apenas numeros)")
#  sys.exit()
#
# digito = {}
# digito[0] = 0
# digito[1] = 0
# a=10
# total=0
# for c in range(0,2):
#  for i in range(0,(8+c+1)):
#   total=total+int(cpflimpo[i])*a
#   a=a-1
#  digito[c]=int(11-(total%11))
#  a=11
#  total=0
# if (int(cpflimpo[9]) == int(digito[0]) and int(cpflimpo[10]) == int(digito[1])):
#  print ("CPF valido: ")
#  for i in (range(len(cpflimpo))):
#    if (i == 2 or i == 5):
#     sep=cpflimpo[i]+" ."
#    elif (i == 8):
#     sep=cpflimpo[i]+" -"
#    else:
#     sep=cpflimpo[i]
#    print ("%s" % sep)
# else:
#  print ("CPF invalido")
#
# class Util(object):
#     #Classe util com metodo de validacao de cpf.
#     #Autor: Shalon Serpa (serpanet@gmail.com)
#     def validaCpf(self,cpf,d1=0,d2=0,i=0):
#         while i<10:
#             d1,d2,i=(d1+(int(cpf[i])*(11-i-1)))%11 if i<9 else d1,(d2+(int(cpf[i])*(11-i)))%11,i+1
#         return (int(cpf[9])==(11-d1 if d1>1 else 0)) and (int(cpf[10])==(11-d2 if d2>1 else 0))
#
#
# #exemplo de uso
#
# print(Util().validaCpf("12345678901"))


# /usr/bin/env python
# -*- coding:UTF-8 -*-
# fonte: http://www.python.org.br/wiki/VerificadorDeCPF
#
# import re
#
# # traduz 123.456.789-10 para 12345678910
# _translate = lambda cpf: ''.join(re.findall("\d", cpf))
#
#
# def _exceptions(cpf):
#     """Se o número de CPF estiver dentro das exceções é inválido
#
#     """
#     if len(cpf) != 11:
#         return True
#     else:
#         s = ''.join(str(x) for x in cpf)
#         if s == '00000000000' or s == '11111111111' or s == '22222222222' or s == '33333333333' or s == '44444444444' or s == '55555555555' or s == '66666666666' or s == '77777777777' or s == '88888888888' or s == '99999999999':
#             return True
#     return False
#
#
# def _gen(cpf):
#     """Gera o próximo dígito do número de CPF
#
#     """
#     res = []
#     for i, a in enumerate(cpf):
#         b = len(cpf) + 1 - i
#         res.append(b * a)
#
#     res = sum(res) % 11
#
#     if res > 1:
#         return 11 - res
#     else:
#         return 0
#
#
# class CPF(object):
#     _gen = staticmethod(_gen)
#     _translate = staticmethod(_translate)
#
#     def __init__(self, cpf):
#         """O argumento cpf pode ser uma string nas formas:
#
#         12345678910
#         123.456.789-10
#
#         ou uma lista ou tuple
#         [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0]
#         (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0)
#
#         """
#
#         if isinstance(cpf, basestring):
#             if not cpf.isdigit():
#                 cpf = self._translate(cpf)
#
#         self.cpf = [int(x) for x in cpf]
#
#     def __getitem__(self, index):
#         """Retorna o dígito em index como string
#
#         """
#
#         return self.cpf[index]
#
#     def __repr__(self):
#         """Retorna uma representação 'real', ou seja:
#
#         eval(repr(cpf)) == cpf
#
#         """
#
#         return "CPF('%s')" % ''.join(str(x) for x in self.cpf)
#
#     def __eq__(self, other):
#         """Provê teste de igualdade para números de CPF
#
#         """
#
#         return isinstance(other, CPF) and self.cpf == other.cpf
#
#     def __str__(self):
#         """Retorna uma representação do CPF na forma:
#
#         123.456.789-10
#
#         """
#
#         d = iter("..-")
#         s = map(str, self.cpf)
#         for i in xrange(3, 12, 4):
#             s.insert(i, d.next())
#         r = ''.join(s)
#         return r
#
#     def isValid(self):
#         """Valida o número de cpf
#
#         """
#
#         if _exceptions(self.cpf):
#             return False
#
#         s = self.cpf[:9]
#         s.append(self._gen(s))
#         s.append(self._gen(s))
# #         return s == self.cpf[:]
#
#
# import re
# de digitar importação Union
#
#
# classe  ValidaCpfCnpj :
#     "" "
#     Valida CPF ou CNPJ realizando cálculos dos dígitos
#     "" "
#
#     def  __init__ ( self , cpf_cnpj : str  =  ' ' ) -> Nenhum :
#         "" " Receber o CPF / CNPJ
#         : param cpf_cnpj: o CPF / CNPJ
#         : digite cpf_cnpj: str
#         "" "
#         self ._validado =  Falso
#         # O CPF pode ser lançado diretamente para instanciar uma classe
#         # ou como property
#         se cpf_cnpj:
#             auto .cpf_cnpj: str  = cpf_cnpj
#
#     def  valida ( self ) -> bool :
#         "" " Realiza toda a validação
#         : retorno: True se for válido, False caso contrário
#         : rtype: bool
#         "" "
#         se  não  for auto .cpf_cnpj:
#             return  False
#
#         qtd_caractere =  len ( self .cpf_cnpj)
#
#         # CPF
#         se qtd_caractere ==  11 :
#             # Primeiros 9 digitos
#             novo_cpf_cnpj: str  =  self ._calcula_digitos ( self .cpf_cnpj [: 9 ],
#                                                        multiplicador_inicial = 10 )
#             # 9 digitos + primeiro digito verificador
#             novo_cpf_cnpj: str  =  self ._calcula_digitos (novo_cpf_cnpj,
#                                                        multiplicador_inicial = 11 )
#
#             se novo_cpf_cnpj ==  self .cpf_cnpj:
#                 self ._validado =  True
#                 return  True
#
#         # CNPJ
#         elif qtd_caractere ==  14 :
#             # Primeiros 12 digitos
#             novo_cpf_cnpj: str  =  self ._calcula_digitos ( self .cpf_cnpj [: 12 ],
#                                                        multiplicador_inicial = 5 )
#             # 12 digitos + primeiro digito verificador
#             novo_cpf_cnpj: str  =  self ._calcula_digitos (novo_cpf_cnpj,
#                                                        multiplicador_inicial = 6 )
#
#             se novo_cpf_cnpj ==  self .cpf_cnpj:
#                 self ._validado =  True
#                 return  True
#         return  False
#
#     @ property
#     def  formatado ( self ):
#         "" " Formata o CPF / CNPJ
#         : levanta o valor: Se o CPF / CNPJ não é para o enviado ou não para válido
#         : retorno: o cpf ou cnpj formatado
#         : rtype: str
#         "" "
#         se  não  for auto ._validado:
#             se  não  for auto .cpf_cnpj ou  não  auto .valida ():
#                 raise  ValueError ( " Enviar o CPF e validar para "
#                                  " obter CPF formatado. " )
#
#         qtd_caracteres =  len ( self .cpf_cnpj)
#
#         se qtd_caracteres ==  11 :
#             cpf =  self .cpf_cnpj
#
#             return  ' % s . % s . % s - % s '  % (cpf [ 0 : 3 ], cpf [ 3 : 6 ], cpf [ 6 : 9 ], cpf [ 9 :],)
#
#         elif qtd_caracteres ==  14 :
#             cnpj =  self .cpf_cnpj
#             # 63.080.648 / 0001-35
#
#             return  ' % s . % s . % s / % s - % s '  % \
#                    (cnpj [ 0 : 2 ], cnpj [ 2 : 5 ], cnpj [ 5 : 8 ], cnpj [ 8 : 12 ], cnpj [ 12 :])
#
#     @ staticmethod
#     def  _calcula_digitos (
#             fatia_cpf_cnpj : str ,
#             multiplicador_inicial : int
#     ) -> União [ str , bool ]:
#         "" " Realiza os cálculos das positions
#         : param fatia_cpf_cnpj: fatias de 9 ou 10 digitos do CPF
#         : digite fatia_cpf_cnpj: str
#         : param multiplicador_inicial: o número que inicia os cálculos
#         : tipo multiplicador_inicial: int
#         : retorno: uma fatia do CPF mais um dos digitos gerados
#         : rtype: União [str, bool]
#         "" "
#         se  não fatia_cpf_cnpj:
#             return  False
#
#         # Evita sequências
#         seqüência: str  = fatia_cpf_cnpj [ 0 ] *  len (fatia_cpf_cnpj)
#         se sequencia == fatia_cpf_cnpj:
#             return  False
#
#         soma: int  =  0
#         para chave, _ em  enumerar ( intervalo ( len (fatia_cpf_cnpj) +  1 , 1 , - 1 )):
#             soma + =  int (fatia_cpf_cnpj [chave]) * multiplicador_inicial
#
#             if (multiplicador_inicial ==  2 ):
#                 multiplicador_inicial =  9
#             else :
#                 multiplicador_inicial - =  1
#
#         resto: int  =  11  - (soma %  11 )
#         resto: int  = resto if resto <=  9  else  0
#
#         return fatia_cpf_cnpj +  str (resto)
#
#     @ property
#     def  cpf_cnpj ( self ) -> str :
#         "" " Getter do CPF
#         : retorno: o CPF
#         : rtype: str
#         "" "
#         self ._validado =  Falso
#         devolver  self ._cpf_cnpj
#
#     @ cpf_cnpj.setter
#     def  cpf_cnpj ( self , cpf_cnpj : str ):
#         "" " Setter faz CPF
#         : param cpf: o CPF
#         : digite cpf: str
#         "" "
#         self ._cpf_cnpj =  self ._so_numeros (cpf_cnpj)
#
#     @ staticmethod
#     def  _so_numeros ( cpf_cnpj : str ) -> str :
#         "" " Remover todos os dígitos não numéricos
#         : param cpf_cnpj: o cpf ou cnpj
#         : digite cpf_cnpj: str
#         : retorno: o cpf / cnpj formatado (só com números)
#         : rtype: str
#         "" "
#         return re.sub ( ' [^ 0-9] ' , ' ' , cpf_cnpj)
