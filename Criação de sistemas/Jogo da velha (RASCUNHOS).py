# # -*- coding: latin1 -*-
#
# tabuleiro=[['' , '' , ''],
#            ['' , '' , ''],
#            ['' , '' , '']]
# def fim():
#     g = ganhador()
#     if g != '':
#         return(True, g)
#     else:
#         total = ''
#         for i in tabuleiro:
#             for j in i:
#                 total+=i
#         return(len(total)>=9, g)
#
# def ganhador():
#     for i in tabuleiro:
#         if i[0] == i[1] == i[2] and i[0] != '':
#             return i[0]
#     for i in range(3):
#         if tabuleiro[0][i] == tabuleiro [1][i] == tabuleiro[2][i] and tabuleiro[0][i] != '':
#             return tabuleiro[0][i]
#         if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[2][0] != '':
#             return tabuleiro[0][0]
#         if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[2][0] != '':
#             return tabuleiro[0][0]
#         return  ''
#
#
# jogadores = ('0','x')
# def jogador(jogada):
#     return jogadores[jogador%2]
#
#
#
# jogador = 0
# f = True
#
# while not f:
#     linha,coluna = (int(input('Digita a linha: '))-1,
#                     int(input('Digita a coluna: '))-1)
#     if tabuleiro[linha][coluna] != '':
#         print('Não é possivel a jogada neste local! tente de novo')
#         continue
#
#     tabuleiro[linha][coluna] = jogador(jogada)
#     jogador += 1
#     f, g = fim()
#
# if g =='':
#     print('Deu velha')
# else:
#     print('%s ganhou'%g)

#

# O tabuleiro
velha="""               Posições
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6
---+---+---  ---+---+---
   |   |      1 | 2 | 3
"""
# Uma lista de posições (linha e coluna) para cada posição válida do jogo
# Um elemento extra foi adicionado para facilitar a manipulação
# dos índices e para que estes tenham o mesmo valor da posição
#
#  7 | 8 | 9
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  1 | 2 | 3

posições = [
       None,  # Elemento adicionado para facilitar índices
      (5, 1), # 1
      (5, 5), # 2
      (5, 9), # 3
      (3, 1), # 4
      (3, 5), # 5
      (3, 9), # 6
      (1, 1), # 7
      (1, 5), # 8
      (1, 9), # 9
    ]

# Posições que levam ao ganho do jogo
# Jogadas fazendo uma linha, um coluna ou as diagonais ganham
# Os números representam as posições ganhadoras
ganho = [
          [ 1, 2, 3], # Linhas
          [ 4, 5, 6],
          [ 7, 8, 9],
          [ 7, 4, 1], # Colunas
          [ 8, 5, 2],
          [ 9, 6, 3],
          [ 7, 5, 3], # Diagonais
          [ 1, 5, 9]
        ]

# Constroi o tabuleiro a partir das strings
# gerando uma lista de listas que pode ser modificada
tabuleiro = []
for linha in velha.splitlines():
    tabuleiro.append(list(linha))

jogador = "X" # Começa jogando com X
jogando = True
jogadas = 0 # Contador de jogadas - usado para saber se velhou
while True:
    for t in tabuleiro:  # Imprime o tabuleiro
        print("".join(t))
    if not jogando: # Termina após imprimir o último tabuleiro
        break
    if jogadas == 9: # Se 9 jogadas foram feitas, todas as posições já foram preenchidas
        print("Deu velha! Ninguém ganhou.")
        break
    jogada = int(input("Digite a posição a jogar 1-9 (jogador %s):" % jogador))
    if jogada<1 or jogada>9:
        print("Posição inválida")
        continue
    # Verifica se a posição está livre
    if tabuleiro[posições[jogada][0]][posições[jogada][1]] != " ":
        print("Posição ocupada.");
        continue
    # Marca a jogada para o jogador
    tabuleiro[posições[jogada][0]][posições[jogada][1]] = jogador
    # Verfica se ganhou
    for p in ganho:
        for x in p:
            if tabuleiro[posições[x][0]][posições[x][1]] != jogador:
                break
        else: # Se o for terminar sem break, todas as posicoes de p pertencem ao mesmo jogador
            print("O jogador %s ganhou (%s): "%(jogador, p))
            jogando = False
            break
    jogador = "X" if jogador == "O" else "O" # Alterna jogador
    jogadas +=1 # Contador de jogadas
