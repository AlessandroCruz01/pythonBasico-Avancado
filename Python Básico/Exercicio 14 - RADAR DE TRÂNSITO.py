# -*- coding: latin1 -*-


vel = float(input("Qual velocidade: "))
if vel>80:
    multa = float(vel - 80) * 7
    print("Voce foi multado no valor de R$ {:.2f}".format(multa))
else:
    print("bom")