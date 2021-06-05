cpf = []
lista = []
def validacao (cpf):
    valido = True
    lista = []
    lista = input("Informe o CPF do cliente: ")
    i = 0
    encontrou = False
    # for i in range(len(cpf)):
    #     if lista == cpf[i]:
    #         encontrou = True
    #         break
    # if encontrou==True:
    #     print('CPF JA ESTAR CADASTRADO')
    #     lista = input("Informe o CPF do cliente, novamente: ")
    #     cpf.append(lista)
    # else:
    cpf.append(lista)
    if ((lista[0] == lista[1]) and (lista[1] == lista[2]) and (lista[2] == lista[3]) and (lista[3] == lista[4])
            and (lista[4] == lista[5]) and (lista[5] == lista[6]) and (lista[6] == lista[7]) and (lista[7] == lista[8])
            and (lista[8] == lista[9]) and (lista[9] == lista[10]) and (lista[10] == lista[11])):
            valido = False
    # primeiro calculo
    dig1 = (int(lista[0]) * 10 + int(lista[1]) * 9 + int(lista[2]) * 8 + int(lista[3]) * 7 + int(lista[4]) * 6 +
            int(lista[5]) * 5 + int(lista[6]) * 4 + int(lista[7]) * 3 + int(lista[8]) * 2)
    dig1 = dig1 * 10 % 11
    if (dig1 == 0) and (dig1 == 1):
            print('O primeiro digito sera', dig1)
    elif (dig1 == [2, 3, 4, 5, 6, 7, 8, 9]) and (dig1 == 10):#estranho
            dig1 = 11 - dig1
    # Segundo calculo
    dig2 = (int(lista[0]) * 11 + int(lista[1]) * 10 + int(lista[2]) * 9 + int(lista[3]) * 8 +
             int(lista[4]) * 7 + int(lista[5]) * 6 + int(lista[6]) * 5 +
            int(lista[7]) * 4 + int(lista[8]) * 3 + int(lista[9]) * 2)
    dig2 = dig2 * 10 % 11
    if (dig2 == 0) and (dig2 == 1):
            print('O segundo digito e: ', dig2)
    elif (dig2 == [2, 3, 4, 5, 6, 7, 8, 9]) and (dig2 == 10):#estranho
            dig2 = 11 - dig2
    if dig1 == int(lista[9]) and dig2 == int(lista[10]):
        pass
    else:
        valido = True
        lista = []
        lista = input(" CPF informado e invalido! Digite novamente: ")
        i = 0
        encontrou = False
        for i in range(len(cpf)):
            if lista == cpf[i]:
                encontrou = True
                break
        if encontrou:
            print('CPF JA ESTAR CADASTRADO')
            lista = input("Informe o CPF do cliente, novamente: ")
            cpf.append(lista)
        else:
            cpf.append(lista)
        if ((lista[0] == lista[1]) and (lista[1] == lista[2]) and (lista[2] == lista[3]) and (lista[3] == lista[4])
                and (lista[4] == lista[5]) and (lista[5] == lista[6]) and (lista[6] == lista[7]) and (lista[7] == lista[8])
                and (lista[8] == lista[9]) and (lista[9] == lista[10]) and (lista[10] == lista[11])):
            valido = False
        # primeiro calculo
        dig1 = (int(lista[0]) * 10 + int(lista[1]) * 9 + int(lista[2]) * 8 + int(lista[3]) * 7 + int(lista[4]) * 6 +
                int(lista[5]) * 5 + int(lista[6]) * 4 + int(lista[7]) * 3 + int(lista[8]) * 2)
        dig1 = dig1 * 10 % 11
        if (dig1 == 0) and (dig1 == 1):
            print('O primeiro digito sera', dig1)
        elif (dig1 == [2, 3, 4, 5, 6, 7, 8, 9]) and (dig1 == 10):
            dig1 = 11 - dig1
        # Segundo calculo
        dig2 = (int(lista[0]) * 11 + int(lista[1]) * 10 + int(lista[2]) * 9 + int(lista[3]) * 8 +
                int(lista[4]) * 7 + int(lista[5]) * 6 + int(lista[6]) * 5 +
                int(lista[7]) * 4 + int(lista[8]) * 3 + int(lista[9]) * 2)
        dig2 = dig2 * 10 % 11
        if (dig2 == 0) and (dig2 == 1):
            print('O segundo digito e: ', dig2)
        elif (dig2 == [2, 3, 4, 5, 6, 7, 8, 9]) and (dig2 == 10):
                dig2 = 11 - dig2
        if dig1 == int(lista[9]) and dig2 == int(lista[10]):
                return cpf
                print('OK')


validacao(cpf)