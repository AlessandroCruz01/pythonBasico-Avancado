from tkinter import *

root = Tk()
root.geometry("600x600")

canvas = Canvas(root, width=400, height=400, cursor='target', image='tabuleiro.png')
canvas.pack()



root.mainloop()