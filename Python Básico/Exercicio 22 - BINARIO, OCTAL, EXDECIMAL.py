# -*- coding: latin1 -*-

def menu():
    print('''         MENU
QUAL A BASE DE CONVERÇÃO:
************************

1 - BINÁRIO
2 - OCTAL
3 - EXADECIMAL
4 - SAIR''')


num=int(input("DIGITE O NUMERO QUE DESEJA CONVERTER: "))
menu()

op=int(input("QUAL BASE DESEJA USAR?:  "))

if op==1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))

elif op==2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))

elif op==3:
    print('{} convertido para Exadecimal é igual á {}'.format(num, hex(num)[2:]))

else:
    print("OPÇÃO INCORRETA")