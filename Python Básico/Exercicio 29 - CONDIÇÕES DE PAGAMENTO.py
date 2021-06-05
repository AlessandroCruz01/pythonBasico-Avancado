valor=float(input('Qual o valor do produto: '))
print('''FORMA DE PAGAMENTO
[1] - A VISTA
[2] - CARTÃO
[3] - ATÉ 2X
[4] - 3X OU MAIS''')

op=int(input('SELECIONE A FORMA DE PAGAMENTO:  '))

if op==1:
    print('Pagamento a vista = {:.2f}R$ terá 10% de desconto ficando no valor de {:.2f}R$'.format(valor, valor-(valor*10/100)))

elif op==2:
    print('Pagamento no crédito a vista = {:.2f}R$ terá 5% de desconto ficando no valor de {:.2f}R$'.format(valor, valor-(valor*5/100)))

elif op==3:
    print('Pagamento parcelado em 2X = valor das parcelas {:.2f}R$ totalizando {:.2f}'.format(valor/2, valor))

elif op==4:
    print('Pagamento dividido em 3x = ficando no total de {:.2f}'.format(valor+(valor*20/100)))

else:
    print('Opção inválido')

