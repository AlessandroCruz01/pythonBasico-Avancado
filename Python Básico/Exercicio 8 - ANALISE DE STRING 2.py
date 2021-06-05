# -*- coding: latin1 -*-


#8) FAÇA UM PROGRAMA QUE LEIA UM NUMERO ATÉ 9999 E MOSTRE NA TELA CADA
#UM DE SEUS DIGITOS SEPAREDOS:
#EXEMPLO:4567
#UN:7    DEZ:6    CEN:5    MIL:4


num = int(input('Digite um numero até 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("UN: {}".format(u))
print("DEZ:{}".format(d))
print("CENT:{}".format(c))
print("MIL: {}".format(m))
