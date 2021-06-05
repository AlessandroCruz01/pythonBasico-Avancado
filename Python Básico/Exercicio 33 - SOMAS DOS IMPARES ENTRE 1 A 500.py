# -*- coding: latin1 -*-


soma=0
for i in range(1,501):
    if i%2==1:#TODOS OS NUMEROS IMPARES
        if i%3==0:#TODOS OS NUMEROS MULTIPLOS DE 3
            print(i)
            soma = soma+i

print('a soma total é igual a {}'.format(soma))