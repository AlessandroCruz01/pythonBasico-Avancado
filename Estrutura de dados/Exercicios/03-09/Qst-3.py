class Fila():
    def __init__(self, tam):
        self.fila = []
        self.tam = tam

    def enfileirar(self, elem):
        if len(self.fila) == self.tam:
            print("Não foi possivel adicionar o paciente '{}' LISTA CHEIA!".format(elem))
        else:
            self.fila.append(elem)

    def prox(self):
        print("O próximo paciente na fila é {}".format(self.fila[0]))

    def vagas(self):
        print("Há {} vagas do tota de {} na fila".format(len(self.fila) - self.tam, self.tam))

    def desenfileirar(self):
        print("paciente {} sendo chamado para atendimento".format(self.fila[0]))
        del(self.fila[0])

    def todos(self):
        for i in self.fila:
            print(i, end=" ")

    def total(self):

        print("\nHá {} pacientes na fila".format(len(self.fila)))

a = Fila(2) #TOTAL DE VAGAS NA FILA
a.enfileirar("Alessandro") #CADASTRO DO USUARIO 1
a.enfileirar("Alex") #CADASTRO DO USUARIO 2
a.enfileirar("Error") #TESTE PARA VER O LIMITE IMPOSTO, NAO VAI CADASTRAR ESSE NA FILA

a.prox() #VERIFICA O PROXIMO DA FILA

a.vagas() #MOSTRA QUANTAS VAGAS AINDA RESTAM

a.todos() #MOSTRA OS NOMES DOS CADASTRADOS

a.total() #MOSTRA O NUMERO TOTAL DE PACIETES NA FILA

a.desenfileirar() #CHAMA O PRÓXIMO DA FILA PARA ATENDIMENTO
a.prox() #VERIFICAÇÃO SE REALMENTE HOUVE A EXCLUSAO DO PACIENTE CHAMADO
