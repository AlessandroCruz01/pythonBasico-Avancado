
matriz = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def menu():
    continuar = 1
    while continuar:
        continuar = int(input("0. Sair  = 1. Jogar novamente"))
        if continuar:
            game()
        else:
            print("Saindo...")


def game():
    jogada = 0

    while ganhou() == 0:
        print("\nJogador ", jogada % 2 + 1)
        exibe()
        linha = int(input("\nLinha :"))
        coluna = int(input("Coluna:"))

        if matriz[linha - 1][coluna - 1] == 0:
            if (jogada % 2 + 1) == 1:
                matriz[linha - 1][coluna - 1] = 1
            else:
                matriz[linha - 1][coluna - 1] = -1
        else:
            print("Nao esta vazio")
            jogada -= 1

        if ganhou():
            print("Jogador ", jogada % 2 + 1, " ganhou apos ", jogada + 1, " rodadas")

        jogada += 1


def ganhou():
    # checando linhas
    for i in range(3):
        soma = matriz[i][0] + matriz[i][1] + matriz[i][2]
        if soma == 3 or soma == -3:
            return 1

    # checando colunas
    for i in range(3):
        soma = matriz[0][i] + matriz[1][i] + matriz[2][i]
        if soma == 3 or soma == -3:
            return 1

    # checando diagonais
    diagonal1 = matriz[0][0] + matriz[1][1] + matriz[2][2]
    diagonal2 = matriz[0][2] + matriz[1][1] + matriz[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0


def exibe():
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                print(" _ ", end=' ')
            elif matriz[i][j] == 1:
                print(" X ", end=' ')
            elif matriz[i][j] == -1:
                print(" O ", end=' ')

        print()


menu()