import sqlite3


conexao = sqlite3.connect('EX_6.db')

c = conexao.cursor()

c.execute("""create table Carros (
                placa text,
                marca text,
                modelo text,
                ano text,
                cor text)""")
conexao.commit()

class Carro():
    def __init__(self, placa='', marca='', modelo='', ano='', cor=''):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def salvar(self,conexao):
        self.conexao = conexao
        sql = 'Insert into Carro (placa,marca,modelo,ano,cor) values ("%s", "%s", "%s", "%s", "%s")' % (
        self.placa, self.marca, self.modelo, self.ano, self.cor)
        return sql

    def excluir(self):
        pass