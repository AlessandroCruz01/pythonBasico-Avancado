
class Pessoa(object):
    nome = cpf  =  None
    def dados(self):
        for i, j in self.__dict__.items():
            print('%s: %s' %(i,j))
        print('sexo:', self.sexo)

class Homem(Pessoa):
    sexo = 'masculino'

    def jogar_bola(self):
        print('futebol')

class Mulher(Pessoa):
    sexo = 'feminino'

    def jogar_voley(self):
        print('volei')

class Filha(Mulher, Homem):#herança multipla
    pass

class Filho(Homem, Mulher):
    pass

i = Filha()
i.nome = 'marcio'
i.cpf = '11111111111111111'
i.jogar_bola()
i.jogar_voley()
i.dados()

print('-------------')

i = Filho()
i.nome ='marcio'
i.cpf = '11111111111111111'
i.jogar_bola()
i.jogar_voley()
i.dados()