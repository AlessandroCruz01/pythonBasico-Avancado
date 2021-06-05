
import tkinter # importa o modulo para interface grafica
from time import strftime # importa strftime para mostrar a hora
rel = tkinter.Label() # criar uma label vazia
rel.pack() # deixa o conteudo visivel dentro da label
rel['text'] = strftime('%H:%M:%S') # formato de hora
rel['font'] = 'Helvita 50 bold' # define a fonte do relogio
rel['foreground'] = 'blue' # define a cor dos numeros
rel['bg'] = 'gray' # define a cor do fundo bg e a abreviatura de background
def contador(): # funcao contador
        agora = strftime('%H:%M:%S') # a variavel agora rece a hora do sistema
        if rel['text'] != agora: # se a hora passada para rel['text'] for diferente de agora, rel['text'] recebe o conteudo de agora que e a hora do sistema
                rel['text'] = agora
        rel.after(100, contador) # essa parte do codigo e muito legal. a cada 100 milisegundos a funcao contador sera chamada e a hora sera atualizada !
contador() # chama a funcao contador
rel.mainloop()