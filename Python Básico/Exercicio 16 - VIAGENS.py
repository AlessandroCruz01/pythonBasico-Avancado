via = int(input("DISTANCIA DA VIAGEM: "))
if via<=200:
    print('A viagem vai custar R$ {:.2f}'.format(via*0.50))
else:
    print('A viagem vai custar R$ {:.2f}'.format(via*0.45))