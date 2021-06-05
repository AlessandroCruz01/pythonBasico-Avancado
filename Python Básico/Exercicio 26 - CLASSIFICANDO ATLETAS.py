ano=int(input("Ano de nascimento: "))
id=(2019-ano)
if id<=9:
    print('COM A IDADE DE {} ANOS VOCE ESTA CLASSIFICADO COMO MIRIM'.format(id))
elif id<=14:
    print('Com {} anos voce é classificado como INFANTIL'.format(id))
elif id<=19:
    print('Com {} anos voce é classificado como JUNIOR'.format(id))
elif id<=20:
    print('Com {} anos voce é classificado como Senior'.format(id))
else:
    print("master")