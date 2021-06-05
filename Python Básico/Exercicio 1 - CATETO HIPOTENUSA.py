# -*- coding: latin1 -*-

import math

a2 = float ( input ('Digite o comprimento do cateto oposto: '))
b2 = float ( input ('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(a2, b2)

print("A hipotenusa tem {:.2f}cm de comprimento ".format(hip))

print('________________________')

#SOLUÇÃO MATEMATICA

a = float ( input ('Digite o comprimento do cateto oposto: '))
b = float ( input ('Digite o comprimento do cateto adjacente: '))
h = (a**2 + b**2) ** (1/2)
print("A hipotenusa tem {:.2f}cm de comprimento ".format(h))