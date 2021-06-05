'''lista'''

class Lista():
    def __init__(self):
        self.lista = []

    def adicionar(self, item):
        self.lista.append(item)

    def remover(self):
        self.lista.pop()

    def mostrar(self):
        for i in self.lista:
            print(i, end=' ')