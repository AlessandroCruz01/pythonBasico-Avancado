# -*- coding: latin1 -*-

print(''' 28) DESENVOLVA UMA L?GICA QUE LEVA O PESO E A ALTURA
 DE UMA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO
 COM A TABELA ABAIXO:
  18.5 -> ABAIXO DO PESO
  ENTRE 18.5 E 25 -> PESO IDEAL
  ENTRE 25 E 30 -> SOBREPESO
  ENTRE 30 E 40 -> OBESIDADE
  ACIMA DE 40 -> MORBIDA''')

peso=float(input('SEU PESO: '))
altura=float(input('SUA ALTURA:  '))
imc=peso/altura**2
if imc<=18.5:
    print('ABAIXO DO PESO filho da puta ve se come - IMC:{:.2f}'.format(imc))
elif imc<=25:
    print('PESO IDEAL pra dar o rabo- IMC:{:.2f}'.format(imc))
elif imc <= 30:
    print('SOBREPESO  gordo fdp- IMC:{:.2f}'.format(imc))
elif imc<=40:
    print('OBESIDADE - GORDO FDP - IMC:{:.2f}'.format(imc))
else:
    print('VAI MORRER DOIDO! - IMC:{:.2f}'.format(imc))