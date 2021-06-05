try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from random import *
from sre_constants import *

class Jogo():
    def __init__(self):

        #CRIANDO A TELA PRINCIPAL;

        self.root = Tk()
        self.root.geometry('%ix%i' %(L, A))
        self.root.title('TESTE')
        self.root.resizable(False,False)#O QUE É RESIZABLE

        #CRIA FRAME PARA CONTER O CANVAS

        self.frame = Frame(bg='blue')
        self.frame.pack()

        #CRIANDO O CANVAS

        self.canvas = Canvas(self.frame, bg='blue', width=L, height=A, cursor='target')
        self.canvas.pack()

        #CRIANDO OBJETOS DENTRO DO CANVAS

        self.canvas.create_line(10,10,390,390,fill='white')
        self.comecar = Button(self.root, text='INICIAR', command=self.comecar)
        self.comecar.pack()
        self.novojogo()

    #CRIANDO AS FUNÇÕES

    def novojogo(self):
        #CRIANDO OBJETOS DENTRO DO JOGO

        self.player  = self.canvas.create_rectangle(195, 360, 280, 375, fill='white')

        #CRIAR A BOLINHA

        raio = 29
        p = (100,200)
        self.ovo = self.canvas.create_oval(p[0], p[1], p[0] + raio,p[0], p[1]+raio, fill='grey')

        #VELOCIDADE DA BOLINHA

        self.b_vx = 7
        self.b_vy = 7

        #POSIÇÃO DA BOLINHA

        self.b_x, self.b_y = p

        x_inicial, y_inicial = 4, 22

        altura, largura = 20, 77
        espacamento = 2

        self.retangulos = []

        for colunas in range(5):
            for linhas in range(5):
                cor = random.choice(['red', 'white', 'green', 'brown', 'orange', 'yellow', 'black', 'darkred', 'lightyellow','','',''])
                x1 = x_inicial+(largura+espacamento)*colunas
                x2 = x1+largura
                y1 = y_inicial+(altura+espacamento)*linhas
                y2 = y1+altura

        retangulos = self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor)
        self.retangulos.append(retangulos)


        self.jogando = True

    def comecar(self):
        self.jogar()

    def jogar(self):
        if self.jogando:
            self.update()
            self.root.after(10, self.jogar)
        else:
            self.acabou(self.msg)

    def update(self):
        self.canvas.move(self.ovo, self.b_vx, self.b_vy)

        #ATUALIZA O MOVIMENTO DA BOLA E SUA POSIÇÃO
        self.b_x += self.b_vx
        self.b_y += self.b_vy

        #VERIFICA SE A BOLA ESTÁ BATENDO DOS LADOS
        if self.b_x > L - 29 or self.b_x < 0:
            self.b_vx *= -1

        if self.b_y > A - 29 or self.b_y < 0:
            self.b_vy *= -1

        #VERIFICA SE HOUVE COLISÃO
    def verificar_colisao(self):

        #CRIA UM BOUDING BOX PARA CAPTURAR A POSIÇÃO DA BOLA

        coord = self.canvas.bbox(self.ovo)
        colisoes = self.canvas.find_overlapping(*coord)
        print(*colisoes)
        print(coord)

        if len(colisoes) != 1:

            #VERIFICA SE O ID DO OBJETO COLIDIDO É DIFERENTE DO ID DO OBJETO PLAYER

            self.b_vy *= -1
            for item in colisoes:
                if item not in self.retangulos: #COLISOES COM A PRORIA BOLA OU COM O PLAYER
                    continue
                self.retangulos.remove(item)
                self.canvas.delete(item)


