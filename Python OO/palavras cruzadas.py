import random
def matriz(l, c):
    matriz = [] # Matriz
    linha = [] # Linha
    abc = ['x','0']

    while len(matriz) != c:
        linha.append(random.choice(abc))
        if len(linha) == c:
            matriz.append(linha)
            linha = []
    return matriz

l = int(input('Linha: '))
c = int(input('Coluna: '))

x = ''
linha = []
save = matriz(l,c)
counter = 1
for i in save:
    print(f'Linha {counter}: ', i)
    counter += 1
for i in range(len(save)):
    for y in save[i]:
        x = x + y
    linha.append(x)
    x = ''
counter = 0
keys = ['xxx','000']
for x in keys:
    for i in linha:
        counter += 1
        if x in i[::-1] or x in i:
            print(f'\nFoi encontrada a palavra "{x}" na linha {counter}')

    counter = 0
colunas = []
x = ''
counter = 1
for z in range(c):
    for i in linha:
        x += i[z]
    colunas.append(x)
    x = ''
for x in keys:
    for i in colunas:
        if x in i[::-1] or x in i:
            print(f'\nFoi encontrada a palavra "{x}" na coluna {counter}')
        counter += 1
    counter = 1

print(linha)
print(colunas)