# -*- coding: latin1 -*-

from random import randint
n = (randint(0,5))
x = int(input("DIGITE SEU PAUPITE: "))
if n == x:
    print("Vo�� acertou: {}".format(n))
else:
    print("Voc� errou. numero certo seria {} ".format(n))