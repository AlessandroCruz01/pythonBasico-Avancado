# -*- coding: latin1 -*-

vc = float(input("Qual o valor da casa: "))
sl = float(input("Qual seu sal�rio: "))
pg = int(input("Quantos anos pra pagar: "))
pa=vc//pg
pm=pa//12
porcentagem=((sl * 30) / 100)

if porcentagem>=pm:
    print("Voc� podera comprar a casa! {}".format(porcentagem))
else:
    print("Compra negada! o valor da parcela ficou {:.2f} maior que os 30% do sal�rio{:.2f}".format(pm, porcentagem))
