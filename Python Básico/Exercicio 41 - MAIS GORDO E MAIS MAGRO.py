# -*- coding: latin1 -*-

# peso=float(input('SEU PESO: '))
# altura=float(input('SUA ALTURA:  '))
# imc=peso/altura**2

# if imc<=18.5:
#     print('ABAIXO DO PESO - IMC:{:.2f}'.format(imc))
# elif imc<=25:
#     print('PESO IDEAL - IMC:{:.2f}'.format(imc))
# elif imc <= 30:
#     print('SOBREPESO - IMC:{:.2f}'.format(imc))
# elif imc<=40:
#     print('OBESIDADE - IMC:{:.2f}'.format(imc))
# else:
#     print('MORBIDA - IMC:{:.2f}'.format(imc))

lista=[]
for i in range(1,6):
    x = float(input('Qual o {}º peso: '.format(i)))
    lista.append(x)
print(lista)
for i in lista:
    for c in lista:
        if c>i:
            g=c
        elif c<i:
            m=c

print('Mais gordo:{} Mais magro:{}'.format(c,m))