# -*- coding: latin1 -*-
import datetime
lista=[]
a=0
b=0
ano1 = datetime.date.today().year  # comando para pegar ano atual
for i in range(1,8):
    ano=int(input('Digite o {} ano de nasc.: '.format(i)))
    lista.append(ano)
print(lista)

for i in lista:
    if ano1 - i >=18:
        a=a+1
    else:
        b=b+1
print('Dos anos de nascimento digitados temos {} com mais de 18 e {} com menos de 18 ano de idade'.format(a, b))