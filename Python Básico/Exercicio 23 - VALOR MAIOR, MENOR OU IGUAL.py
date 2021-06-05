n1=int(input('1º NUMERO: '))
n2=int(input('2º NUMERO: '))

if n1>n2:
    print('{} é MAIOR que {}'.format(n1,n2))
elif n1<n2:
    print('{} é MENOR que {}'.format(n1,n2))
else:
    print('Numeros iguais')