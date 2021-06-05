# -*- coding: UTF-8 -*-

import sqlite3


class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('EX_1.db')
        # self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table Pessoa2 (
                     nome text,
                     mae text,
                     pai text,
                     cpf text,
                     nasc text)""")
        self.conexao.commit()

class Pessoa(object):
    def __init__(self, nome, mae,pai,cpf,nasc):
        self.nome = nome
        self.mae = mae
        self.pai = pai
        self.cpf = cpf
        self.nasc = nasc

    def sqlInsert(self):
        sql = 'Insert into Pessoa (cpf,nome,mae,pai,nasc) values ("%s", "%s", "%s", "%s", "%s")'%(self.nome, self.mae, self.pai, self.cpf, self.nasc)
        return sql


    def __str__(self):
        return ('%s\n%s\n%s\n%s\n%s'% (self.nome, self.mae, self.pai, self.cpf, self.nasc))

    def salvar(self,conexao):
        c = conexao.cursor()
        c.execute(self.sqlInsert())
        conexao.commit()
        c.close()
        print('SALVO!')

banco = Banco()

cadastro = Pessoa(nome = input(" "),mae = input(" "),pai = input(" "),cpf = input(" "),nasc = input(" "))
cadastro.salvar(banco.conexao)





