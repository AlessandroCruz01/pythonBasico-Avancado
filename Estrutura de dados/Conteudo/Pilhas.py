class Pilha():
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        return self.itens.pop()

    def isEmpty(self):
        return (self.itens == [])