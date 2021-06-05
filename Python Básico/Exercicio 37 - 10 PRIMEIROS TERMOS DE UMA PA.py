# -*- coding: latin1 -*-

inicio=int(input("Onde inicia sua P.A: "))
razao=int(input("Qual a razão: "))
c=1
while c<=10:
    print('{}º termo: {}'.format(c, inicio))
    inicio = inicio+razao
    c=c+1