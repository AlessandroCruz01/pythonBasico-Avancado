try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from random import *
from time import *
from threading import Thread

fim = True

principal = Tk()
principal.geometry("500x500")
principal.children


position = ('LEFT', 'RIGHT', 'UP', 'DOWN')
cores = ('yellow', 'green', 'orange', 'blue', 'black', 'grey', 'pink')


class Quadrado(Thread):
    def __init__(self, principal):
        self.x = randint(0, 400)
        self.y = randint(0, 400)
        cor = cores[randint(0, len(cores)-1)]

        self.principal = principal
        self.quadrado = Canvas(principal, width=100, height=100)
        self.quadrado.place(x=self.x, y=self.y)
        self.quadrado.create_rectangle(0,0,100,100, fill=cor, outline = cor)
        super(Quadrado, self).__init__()

    
    def run(self):
        while True:
            pos = position[randint(0,len(position)-1)]
            sleep(1)

            if pos == 'LEFT':
                print('LEFT')
                self.x -=50
                self.quadrado.place(x=self.x, y=self.y)
                cor = cores[randint(0, len(cores) - 1)]
                self.quadrado.create_rectangle(0, 0, 100, 100, fill=cor, outline=cor)

            elif pos == 'RIGHT':
                print('RIGHT')
                self.x +=50
                self.quadrado.place(x=self.x, y=self.y)
                cor = cores[randint(0, len(cores) - 1)]
                self.quadrado.create_rectangle(0, 0, 100, 100, fill=cor, outline=cor)

            elif pos == 'UP':
                print('UP')
                self.y +=50
                self.quadrado.place(x=self.x, y=self.y)
                cor = cores[randint(0, len(cores) - 1)]
                self.quadrado.create_rectangle(0, 0, 100, 100, fill=cor, outline=cor)
            elif pos =='DOWN':
                print('DOWN')
                self.y -=50
                self.quadrado.place(x=self.x, y=self.y)
                cor = cores[randint(0, len(cores) - 1)]
                self.quadrado.create_rectangle(0, 0, 100, 100, fill=cor, outline=cor)


    def VerifiacaColisao(self):
        coord = self.canvas.bbox(self.quadrado)
        colisoes = self.canvas.find_overlapping(*coord)
        print(*colisoes)
        print(coord)



a = Quadrado(principal)
a.start()

b = Quadrado(principal)
b.start()

c = Quadrado(principal)
c.start()


def posicao(event):
    print("(%s, %s)"%(event.x_root,event.y_root))
principal.bind("<Button-1>", posicao)




principal.mainloop()