# -*- coding: latin1 -*-

op=1
while op!=0:
    frase=str(input('Digite uma frase: ')).strip().upper()

    #RETIRANDO OS ESPA�OS
    frase=frase.replace(" ", "")
    print(frase)

    if frase[: : -1]==frase:
        print('� polindromo')
        op = input('''
          1  - jogar novamente
          0  - sair        ''')
    else:
        print('N�o � polindromo')

        op = input('''
    1  - jogar novamente
    0  - sair        ''')