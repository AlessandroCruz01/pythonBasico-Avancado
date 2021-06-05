from tkinter import *
from random import *

root = Tk()
root.geometry('500x500')

frame = Frame(bg='blue')
frame.pack()

canvas = Canvas(frame, bg='blue', width=400,height=400, cursor = 'target')
canvas.pack()

canvas.create_line(10,10,390,390, fill='white')

comecar = Button(root,text='INICIAR',command='')
comecar.pack()

player = canvas.create_rectangle(195,360,280,375, fill='white')

raio = 29
p = (100,200)
ovo = canvas.create_oval(p[0], p[1], p[0]+raio, p[1]+raio, fill='red')


b_vx = 7
b_vy = 7

b_x, b_y = p

x_inicial, y_inicial = 4, 22

altura, largura = 20, 77
espacamento = 2

retangulos = []

cores = ('yellow', 'green', 'orange', 'blue', 'black', 'grey', 'pink')

for colunas in range(5):
    for linhas in range(5):
        cor = cores[randint(0, len(cores)-1)]
        x1 = x_inicial + (largura + espacamento) * colunas
        x2 = x1 + largura
        y1 = y_inicial + (altura + espacamento) * linhas
        y2 = y1 + altura
        retangulos = canvas.create_rectangle(x1,y1,x2,y2, fill = cor)
        jogando = True

canvas.move(ovo, b_vx, b_vy)

b_x += b_vx
b_y += b_vy

if b_x > 400 - 29 or b_x < 0:
    b_vx *= -1
if b_y > 400 - 29 or b_y < 0:
    b_vy *= -1


root.mainloop()



