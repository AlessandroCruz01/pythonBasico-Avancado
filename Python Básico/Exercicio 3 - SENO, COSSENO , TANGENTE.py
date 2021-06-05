import math

#CALCULO DO SENO
ang = float ( input('Digite o angulo: '))
seno = math.sin(math.radians(ang))
print("O seno de {} é igual á {:.2f}".format(ang, seno))

#CALCULO DO COSSENO
cosseno = math.cos(math.radians(ang))
print("O cosseno de {} é igual á {:.2f}".format(ang, cosseno))

#CALCULO DA TANGENTE
tan = math.tan(math.radians(ang))
print("Atangente de {} é igual á {:.2}".format(ang, tan))
