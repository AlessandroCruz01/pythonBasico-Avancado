nas=int(input('Digite o ano do seu nascimento: '))
if (2019-nas)==18:
    print('Já é hora de se alistar!')
elif (2019-nas)>18:
    nas=2019-nas
    print('Você passou {} anos do ano de alistamento, e está agora com {} anos'.format(nas-18, nas))
else:
    nas=2019-nas
    print('Ainda vai se alistar, faltam {} anos pro alistamento'.format(18-nas))
