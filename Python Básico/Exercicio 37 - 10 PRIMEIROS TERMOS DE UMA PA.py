# -*- coding: latin1 -*-

inicio=int(input("Onde inicia sua P.A: "))
razao=int(input("Qual a raz�o: "))
c=1
while c<=10:
    print('{}� termo: {}'.format(c, inicio))
    inicio = inicio+razao
    c=c+1