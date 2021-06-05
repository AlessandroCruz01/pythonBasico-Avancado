class Fila():
    def __init__(self, tam):
        self.fila = []
        self.tam = tam

    def enfileirar(self, elem):
        if len(self.fila) == self.tam:
            print("Não foi possivel adicionar o elemento '{}' LISTA CHEIA!".format(elem))

        else:
            self.fila.append(elem)

    def desenfileirar(self):
        self.fila.pop()

    def todos(self):
        for i in self.fila:
            print(i, end=" ")

    def total(self):
        print(len(self.fila))

    def contrario(self):

        for i in self.fila[::-1]:
            print(i, end=' ')
a = Fila(2)
a.enfileirar(3)
a.enfileirar(2)
a.enfileirar(1)
a.enfileirar(23)
a.todos()
a.total()
a.contrario()