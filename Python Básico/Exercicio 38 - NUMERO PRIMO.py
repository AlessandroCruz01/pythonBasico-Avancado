# -*- coding: latin1 -*-

num = int(input("Digite o numero que deseja saber se � primo: "))
for i in range(1,num+1):
    if num%2==1:
        print('{} � PRIMO!'.format(num))
        break
    else:
        print('{} N�O � PRIMO'.format(num))
        break