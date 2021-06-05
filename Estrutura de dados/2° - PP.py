class No:
    def __init__(self, carga=None, proximo=None):
        self.carga = carga
        self.proximo = proximo

    def __str__(self):
        return str("(%s , %s)"%(self.carga, self.proximo))

class ListaEncadeadaA():
    def __init__(self):
        self._primeiro = None
        self._ultimo = None
        self.lista = []

    def insereInicio(self, v):
        self._primeiro = No(v, self._primeiro)
        if self._ultimo == None:
            self._ultimo = self._primeiro
            self.lista.append(self._primeiro)
            for i in self.lista:
                print(i)

    def insereFim(self, v):
        p = No(v, self)
        if self._primeiro == None:
            self._primeiro = p
            self._ultimo = p
        else:
            self._ultimo.prox = p
            self._ultimo = p

    def removeInicio(self):
        if self._primeiro == None:
            raise Exception('listavazia')
        v = self._primeiro.valor
        self._primeiro = self._primeiro.prox
        if self._primeiro == None:
            self._ultimo = None
        return v


class ListaEncadeadaB():
    def __init__(self):
        self._primeiro = None
        self._ultimo = None
        self.lista = []

    def insereInicio(self, v):
        self._primeiro = No(v, self._primeiro)
        if self._ultimo == None:
            self._ultimo = self._primeiro
            self.lista.append(self._primeiro)
            print(self.lista)

    def insereFim(self, v):
        p = No(v, self)
        if self._primeiro == None:
            self._primeiro = p
            self._ultimo = p
        else:
            self._ultimo.prox = p
            self._ultimo = p

    def removeInicio(self):
        if self._primeiro == None:
            raise Exception('listavazia')
        v = self._primeiro.valor
        self._primeiro = self._primeiro.prox
        if self._primeiro == None:
            self._ultimo = None
        return v


a = ListaEncadeadaA()
a.insereInicio(5)
a.insereInicio(7)