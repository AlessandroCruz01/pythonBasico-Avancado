from tkinter import *
def b12():
    er = Toplevel(root)
    texto = Label(er, text='Me  beija! TE AMO!!!!!!!!!!!')
    texto['font'] = ('Arial', '12', 'bold')
    texto.pack()

    er.geometry('800x800')

    er.mainloop()
root = Tk()
root.geometry('300x300')
txt = Label(root, text='Sabe Karol, eu não sei onde vamos parar. Más a vontade que eu tenho de ser feliz ao teu lado é INEVITAVEL')
txt['font'] = ('Arial', '12', 'bold')
txt.pack()

b1 = Button(root, text = 'Me quer?', command=b12)
b1.pack()



root.mainloop()




















