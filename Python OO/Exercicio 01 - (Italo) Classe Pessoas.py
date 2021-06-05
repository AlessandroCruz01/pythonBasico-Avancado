# -*- coding: latin1 -*-

class Pessoa(object):
    nome = mae = pai = cpf = nasc = sexo = None


    def __init__(self, nome, mae, pai, cpf, nasc, sexo ):
        self.nome = nome
        self.mae = mae
        self.pai = pai
        self.cpf = cpf
        self.nasc = nasc
        self.sexo = sexo

    def mostrar(self):
        print("nome: ", self.nome)
        print('mae: ', self.mae)
        print('Pai: ', self.pai)
        print('cpf: ', self.cpf)
        print('Data de nascimento: ', self.nasc)
        print('Sexo: ', self.cpf)

class Homen(Pessoa):
    pass