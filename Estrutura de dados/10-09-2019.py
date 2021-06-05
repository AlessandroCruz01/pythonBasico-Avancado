class No():
    def __init__(self,valor, prox=None):
        self.valor = valor
        self.prox = prox

    def __str__(self):
        return "%s - %s"%(self.valor, self.prox)

    def insere_inicio(self):
        self.__primeiro = No(self.valor, self.__primeiro)
        if self.__ultimo == None:
            self.__ultimo = self.__primeiro

a = No(23, None)
a = No(5, a)
a = No(10, a)
a.insere_inicio()
print(a)