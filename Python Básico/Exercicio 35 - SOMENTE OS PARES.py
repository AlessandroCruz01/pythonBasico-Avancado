# -*- coding: latin1 -*-


lista=[]
soma=0
for i in range(1,7):
    num=int(input('Digite o {}� numero inteiro: '.format(i)))
    lista.append(num)
for i in lista:
    if i%2==0:
        print('PAR: {}'.format(i))
        soma=soma+i
    else:
        print('N�o h� numeros pares')
        break
print('A soma dos numeros pares � de {}'.format(soma))


