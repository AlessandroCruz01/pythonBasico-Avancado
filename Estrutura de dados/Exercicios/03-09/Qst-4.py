class Call_center():
    def __init__(self, tam):
        self.fila = []
        self.tam = tam
        self.contatos = ()

    def enfileirar(self, nome, tel):
        if len(self.contatos) == self.tam:
            print("Não foi possivel adicionar o paciente '{}' LISTA CHEIA!".format(nome))
        else:
            self.contatos = {nome:tel}

    def todos(self):
        for i in self.contatos:
            print(self.contatos)
            print(type(self.contatos))


a = Call_center(2)
a.enfileirar("alessandro", "9999-9999")
a.enfileirar("lucas", "0000-0000")
a.enfileirar("fernando", "0000-0000")
a.todos()