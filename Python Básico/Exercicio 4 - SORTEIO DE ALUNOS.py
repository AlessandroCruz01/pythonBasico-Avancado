# -*- conding: latin1 -*-

import math
import random



aluno=[]
cont=0

while cont<4:
    nomes=input("NOMES: ")
    aluno.append(nomes)
    cont=cont+1
escol = random.choice(aluno)
print("o aluno escolhido foi {}".format(escol))
