# -*- conding: latin1 -*-
import random


aluno=[]
cont=1
while cont<=4:
    nomes=input("NOMES: ")
    aluno.append(nomes)
    cont=cont+1
random.shuffle(aluno)
print("A ordem sorteda será:")
print(aluno)