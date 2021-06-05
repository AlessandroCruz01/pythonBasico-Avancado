#-*- conding: latin1 -*-


#7) Crie um programa que leia um nome de uma pessoa e retorne:
#*O nome com todas as letras maiusculas
#*O nome com todas as letrs minusculas
#*Quantas letras tem sem os espaços
#*Quantas letras tem somente o 1º nome

#=======================================================================#
nome = str(input("digite seu nome: ")).strip()

#*O nome com todas as letras maiusculas
print("seu nome {} em maiusculo fica {}".format(nome, nome.upper()))

#*O nome com todas as letrs minusculas
print("seu nome {} em minusculo fica {}".format(nome, nome.lower()))

#*Quantas letras tem sem os espaços
print(" O nome {} tem {} letras".format(nome, len(nome)-nome.count(' ')))

#QUANTAS LETRAS TEM O 1 NOME
print("o primeiro nome tem {} letras".format(nome.find(' ')))



    

