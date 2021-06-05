import sqlite3

conexao = sqlite3.connect('SINTAXE.db')
conexao.cursor()
c = conexao

c.execute("""CREATE TABLE IF NOT EXISTS teste (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(50) NOT NULL,
                idade VARCHAR(3) NOT NULL
                )""")
c.commit()

nome = input('nome: ')
idade = input('idade: ')

c.execute("""INSERT INTO teste (nome, idade) 
                VALUES ('%s','%s')
                """%(nome,idade))

c.commit()
print('salvo')

conexao = sqlite3.connect('SINTAXE.db')
conexao.cursor()
x = 'SELECT nome, idade FROM teste WHERE  nome=(?)'
conexao.execute(x , [nome])
busca = conexao.fetchall()