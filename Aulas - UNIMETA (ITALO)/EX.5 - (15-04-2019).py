# -*- coding: UTF-8 -*-

#################################################################
# BIBLIOTECAS #

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from random import randint

from time import sleep

from threading import Thread

fim = False
###################################################################
# CRIANDO TELA Tkinter

root = Tk()
root.geometry('600x600')


##################################################################
# INCREMENTAÇÕES

cores = ('yellow', 'green', 'orange', 'blue', 'black', 'grey', 'pink')
position = ('LEFT', 'RIGHT', 'UP', 'DOWN')



###################################################################
# CRIANDO CLASSES

class Quadrado(object):
    def desenhar(self, principal):
        self.x = randint(0,500)
        self.y = randint(0,500)
        self.principal = principal
        cor = cores[randint(0, len(cores) - 1)]
        self.quadrado = Canvas(principal, width=100, height=100)
        self.quadrado.place(x=self.x, y=self.y)
        self.quadrado.create_rectangle(0, 0, 100, 100, fill=cor, outline=cor)


class Circulo(object):
    def desenhar(self, principal):
        self.x = randint(0,500)
        self.y = randint(0,500)
        self.principal = principal
        cor = cores[randint(0, len(cores) - 1)]
        self.circulo = Canvas(principal, width=100, height=100)
        self.circulo.place(x=self.x, y=self.y)
        self.circulo.create_oval(50, 50, 100, 100, fill=cor, outline=cor)


class Triangulo(object):
    def desenhar(self, principal):
        self.x = randint(0,500)
        self.y = randint(0,500)
        self.principal = principal
        cor = cores[randint(0, len(cores) - 1)]
        self.triangulo = Canvas(principal, width=100, height=100)
        self.triangulo.place(x=self.x, y=self.y)
        self.triangulo.create_polygon(50, 0, 0, 100,100,100, fill=cor, outline=cor)




class Mov_quadrado(Thread, Quadrado):

    def run(self):
        self.desenhar(root)
        while True:
            pos = position[randint(0, len(position) - 1)]
            sleep(1)

            if pos == 'LEFT':
                print('LEFT')
                self.x -= 50
                self.quadrado.place(x=self.x, y=self.y)

            elif pos == 'RIGHT':
                print('RIGHT')
                self.x += 50
                self.quadrado.place(x=self.x, y=self.y)

            elif pos == 'UP':
                print('UP')
                self.y += 50
                self.quadrado.place(x=self.x, y=self.y)
            elif pos == 'DOWN':
                print('DOWN')
                self.y -= 50
                self.quadrado.place(x=self.x, y=self.y)



class Mov_circulo(Thread, Circulo):

    def run(self):
        self.desenhar(root)
        while True:
            pos = position[randint(0, len(position) - 1)]
            sleep(1)

            if pos == 'LEFT':
                print('LEFT')
                self.x -= 50
                self.circulo.place(x=self.x, y=self.y)

            elif pos == 'RIGHT':
                print('RIGHT')
                self.x += 50
                self.circulo.place(x=self.x, y=self.y)

            elif pos == 'UP':
                print('UP')
                self.y += 50
                self.circulo.place(x=self.x, y=self.y)
            elif pos == 'DOWN':
                print('DOWN')
                self.y -= 50
                self.circulo.place(x=self.x, y=self.y)


class Mov_triangulo(Thread, Triangulo):

    def run(self):
        self.desenhar(root)
        while True:
            pos = position[randint(0, len(position) - 1)]
            sleep(1)

            if pos == 'LEFT':
                print('LEFT')
                self.x -= 50
                self.triangulo.place(x=self.x, y=self.y)

            elif pos == 'RIGHT':
                print('RIGHT')
                self.x += 50
                self.triangulo.place(x=self.x, y=self.y)

            elif pos == 'UP':
                print('UP')
                self.y += 50
                self.triangulo.place(x=self.x, y=self.y)
            elif pos == 'DOWN':
                print('DOWN')
                self.y -= 50
                self.triangulo.place(x=self.x, y=self.y)



###############################################################
# INSTANCIANDO CLASSES


x = Mov_quadrado()
x.start()

y = Mov_circulo()
y.start()

z = Mov_triangulo()
z.start()

root.mainloop()


