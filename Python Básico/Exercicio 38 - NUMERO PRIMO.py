# -*- coding: latin1 -*-

num = int(input("Digite o numero que deseja saber se é primo: "))
for i in range(1,num+1):
    if num%2==1:
        print('{} É PRIMO!'.format(num))
        break
    else:
        print('{} NÃO É PRIMO'.format(num))
        break