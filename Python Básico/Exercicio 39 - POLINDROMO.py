# -*- coding: latin1 -*-

op=1
while op!=0:
    frase=str(input('Digite uma frase: ')).strip().upper()

    #RETIRANDO OS ESPAÇOS
    frase=frase.replace(" ", "")
    print(frase)

    if frase[: : -1]==frase:
        print('É polindromo')
        op = input('''
          1  - jogar novamente
          0  - sair        ''')
    else:
        print('Não é polindromo')

        op = input('''
    1  - jogar novamente
    0  - sair        ''')