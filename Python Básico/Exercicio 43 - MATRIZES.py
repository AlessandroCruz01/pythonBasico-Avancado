'''
ESCREVA UMA FUNÇÃO QUE RECEBA UM INTEIRO 'M' E OUTRO 'N' E COM ISSO
CONTROI UMA MARTRIZ MNX
'''

# matriz = []
#
# m = int(input('LINHAS DA MATRIZ: '))
# n = int(input('COLUNAS DA MATRIZ: '))
#
# def constroimatriz(m, n , matriz):
#     for i in range(1, m+1):
#         linha = []
#         for j in range(1, n+1):
#             x = int(input('ELEMENTO %i , %i da matriz: '%(i,j)))
#             linha.append(x)
#         matriz.append(linha)
#
# constroimatriz(m , n, matriz)
#
# print(matriz)
#
#
# matriz = []
#
# x = 5
# y = 5
#
# for i in range(x): #COLUNA
#     linha = []
#     for j in range(y+1): #LINHA
#         linha.append(0)
#     matriz.append(linha)
# print(matriz)


#DIMENSÃO DA MATRIZ

matriz = []

#MOSTRANDO EM FORMA DE MATRIZ
for i in range(5):
    matriz.append([0]*5)
for i in range(5):
    print(matriz[i])