'''Filas'''

class Fila():
    def __init__(self):
        self.lista = []

    def adicionar(self, item):
        self.lista.append(item)

    def remover(self):
        self.lista.pop(0)

    def mostrar(self):
        for i in self.lista:
            print(i, end=' ')