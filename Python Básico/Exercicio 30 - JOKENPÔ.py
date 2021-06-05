# -*- coding: latin1 -*-

from random import randint

pc=(randint(1,3))

print('''Escolha
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA''')

es=int(input('Faça sua escolha: '))

if es==1:
    if pc==3:
        print('Voce ganhou! PC=tesoura (pedra quebra a tesoura)')
    elif pc==1:
        print('Empate! PC=também escolheu a pedra')
    else:
        print('O computador ganhou! PC=papel (o papel envolve a pedra)')

elif es==2:
    if pc==1:
        print('Voce ganhou! PC=pedra (o papel envolve a pedra)')
    elif pc==2:
        print('Empate! PC=também escolheu a papel')
    else:
        print('O computador ganhou! PC=Tesoura (tesoura corta o papel)')

elif es==3:
    if pc==1:
        print('Voce perdeu! PC=pedra (a pedra quebra a tesoura)')
    elif pc==2:
        print('Voce ganhou! PC=papel (tesoura corta o papel)')
    else:
        print('Empate! O PC tambem escolheu a tesoura')

else:
    print('Opção incorreta')





