import sqlite3

class Pessoa():
    def __init__(self, cpf = None, nome = None, mae = None, tel = None, end = None, email = None, pai = None):
        self._cpf = cpf
        self._nome = nome
        self._mae = mae
        self._tel = tel
        self._end = end
        self._email = email
        self._pai = pai

    def validar(self):
        if self.cpf=='' and self.nome=='' and self.mae=='' and self.tel=='' and self.end=='' and self.email=='' and self.pai ==  None or self.pai =='':

            return True
        else:
            return False
            print('campo nao cadastrado')

    def salvar(self):
        self.validar()
        if self.validar()== True:
            print(""" INSERT INTO PESSOA ( cpf, nome, mae, tel, end, email, pai) VALUES ({}, {}, {}, {}, {}, {}, {} """.format(self._cpf, self._nome, self._mae, self._tel, self._end, self._email, self._pai))

    def mostrar(self):
        pass

# cpf
    @property
    def cpf(self):
        print('GET  AÍ: ')
        return self._cpf
    @cpf.setter
    def cpf(self, cpf):
        print('SET  AÍ: ')
        self._cpf = cpf
#nome
    @property
    def nome(self):
        print('GET AI')
        return self._nome
    @nome.setter
    def nome(self, nome):
        print('SET AI')
        self._nomec = nome



#mae
    @property
    def mae(self):
        print('GET  AÍ: ')
        return self._mae
    @mae.setter
    def mae(self, mae):
        print('SET  AÍ: ')
        self._mae = mae

#telefone
    @property
    def tel(self):
        print('GET  AÍ: ')
        return self._tel
    @tel.setter
    def tel(self, tel):
        print('SET  AÍ: ')
        self._tel = tel

#end
    @property
    def end(self):
        print('GET  AÍ: ')
        return self._end
    @end.setter
    def end(self, end):
        print('SET  AÍ: ')
        self._end = end

#email
    @property
    def email(self):
        print('GET  AÍ: ')
        return self._email
    @email.setter
    def email(self, email):
        print('SET AÍ: ')
        self._email = email

f = ()
a = Pessoa
a.cpf = '025'
a.nome = 'Alessandro'
a.mae = 'lene'
a.tel=('058')
a.end=('Travasse')
a.email=('Ale@ale')
a.pai = None




a.salvar(a)