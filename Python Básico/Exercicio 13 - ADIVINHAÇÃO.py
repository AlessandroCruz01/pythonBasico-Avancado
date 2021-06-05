# -*- coding: latin1 -*-

from random import randint
n = (randint(0,5))
x = int(input("DIGITE SEU PAUPITE: "))
if n == x:
    print("Voçê acertou: {}".format(n))
else:
    print("Você errou. numero certo seria {} ".format(n))