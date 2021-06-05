# -*- coding: UTF-8 -*-
#JOGOS DE DAMAS:

class Peca(object):
    dama = False
    #ATRIBUTOS:
    def __init__(self,principal,cor, pos):
        self.principal=principal
        self.cor = cor
        self.pos = pos
        self.peca = Button(height=3, width=5, command='', bg=cor)
        self.peca.place(x=posicao[0], y=posicao[1])

    #METODOS:
    def mover(self, posicao):
        self.peca.place(x=posicao[0], y=posicao[1])


    def virar_dama(self):
        self.dama = True #AUTERAR DESENHO DA PEÇA E A MOVIMENTAÇÃO FICA POR CONTA DO TABULEIRO


class Tabuleiro(object):

    def __init__(self,root):
        jogador = 'Brancas'
        pec_brancas = 12
        pec_pretas = 12
        jogo_empatei = 0

        i=0
        for x in range(8):
            for y  in range(8):
                if (x+i)%2==0:
                    b1 = Button(root, height=3, width=5, bg='red', command='')
                    b1.grid(row=x,  column=y)

                else:

                    b1 = Button(root, height=3, width=5, bg='black', command='')
                    b1.grid(row=x, column=y)

                i +=1

    #para = (LINHA, COLUNA)
    def jogar(self,peca,para):
        if peca.cor == 'Branca':
            if para[1] - peca.pos[1]**2 != 1: #ANDOU UMA CASA LATERAL
                pass
            if para[0]>peca.pos[0] and peca.dama:
                pass


try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from PIL import Image as ImageTk


root = Tk()
root.title('Aprende porra')
Tabuleiro(root)
root.geometry('544x522')

#matriz = [[False for i in range(8)] for i in range (8)]


def posicao(event):
    print("(%s, %s)"%(event.x_root,event.y_root))
root.bind("<Button-1>", posicao)


root.mainloop()

