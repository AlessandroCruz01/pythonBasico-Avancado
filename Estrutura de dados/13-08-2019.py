
class Node:

    def __init__(self, value, next_node=None):
        self.__value = value
        self.next_node = next_node

    @property
    def value(self):
        return self.__value


class EncadeadaA():

    def __init__(self):
        self.__main_node = None

    def inserir(self, value):
        if self.__main_node is None:
            self.__main_node = Node(value)
            return

        curr_node = self.__main_node
        while curr_node.next_node is not None:
            curr_node = curr_node.next_node
        curr_node.next_node = Node(value)


    def mostrar(self):
        self.values = []
        self.ordenadaA = []
        self.curr_node = self.__main_node
        while self.curr_node is not None:
            self.values.append(self.curr_node.value)
            self.curr_node = self.curr_node.next_node
        self.ordenadaA = (self.values)
        self.ordenadaA.sort()
        print('Ordenada A: {}'.format(self.ordenadaA))



class EncadeadaB(EncadeadaA):

    def __init__(self):
        super(EncadeadaA).__init__()
        self.__main_node = None


    def inserir(self, value):
        if self.__main_node is None:
            self.__main_node = Node(value)
            return

        curr_node = self.__main_node
        while curr_node.next_node is not None:
            curr_node = curr_node.next_node
        curr_node.next_node = Node(value)

    def mostrar(self):
        self.values = []
        self.ordenadaB = []
        self.curr_node = self.__main_node
        while self.curr_node is not None:
            self.values.append(self.curr_node.value)
            self.curr_node = self.curr_node.next_node
        self.ordenadaB = (self.values)
        self.ordenadaB.sort()
        print('Ordenada B: {}'.format(self.ordenadaB))
        self.values = self.ordenadaB
        print(self.values)

    def mesclar(self):
        self.ordenadaA.extend(self.ordenadaB)




a = EncadeadaA()
for i in [10,50,30,80,8]:
    a.inserir(i)
a.mostrar()

b = EncadeadaB()
for i in [10,50,30,80,8]:
    b.inserir(i)
b.mostrar()
