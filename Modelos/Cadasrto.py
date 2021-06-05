nome = []
cpf  = []
mae  = []
pai  = []
rg   = []
telefone = []
celular  = []
email  = []
rua    = []
numcasa = []
bairro  = []
cidade  = []
estado  = []
cep     = []
pais    = []
lista=[]
salvo_banco=[]
def menu():
    print("---------------------------------------------")
    print("|       SISTEMA DE CADASTRO - SIDCAD        |")
    print("| ------------------MENU------------------- |")
    print("| 1)Inserir novo cliente                    |")
    print("| 2)Remover os clientes                     |")
    print("| 3)Lista os cliente                        |")
    print("| 4)Sair do sistema                         |")
    print("---------------------------------------------")
    opcao = input("DIGITE A OPCAO DESEJADA: ")
    return opcao

def inserir ():
    arquivo = open('Cadastro.txt','w')

    validacao(cpf)
    n = str(input("Informe o nome do cliente: "))
    while len(n)< 3 or len(n)>80:
        n = str(input("Informe o nome do cliente: "))
    nome.append(n)
    m = str(input('Informe sua filiação:'))
    while len(m) < 3 or len(m) > 80:
        m = str(input('Informe sua filiação:'))
    mae.append(m)
    p = str(input('Informe sua filiação paternal:'))
    pai.append(p)
    ok = False
    while not ok:
        r = input('Informe seu RG:')
        ok = r.isdigit()
        rg.append(r)
    cert = False
    while not cert:
        tel = input('Informe seu telefone:')
        cert = tel.isdigit()
        telefone.append(tel)
    val = False
    while not val:
        cel = input('Informe seu celular:')
        val = cel.isdigit()
        celular.append(cel)
    valida_email(email)
    ru = str(input("Informe o nome da rua: "))
    rua.append(ru)
    certo = False
    while not certo:
        num = input('informe o numero da sua casa:')
        certo = num.isdigit()
        numcasa.append(num)
    bai = str(input('Informe o nome do seu bairro:'))
    bairro.append(bai)
    cid = str(input('Informe sua naturalidade:'))
    cidade.append(cid)
    est = str(input('Informe seu UF:'))
    estado.append(est)
    ctr = False
    while not ctr:
        c = input('Informe seu CEP:')
        ctr = c.isdigit()
        cep.append(c)
    pa = str(input('Informe sua nacionalidade:'))
    pais.append(pa)
    salva_banco()
    arquivo.write(str(cpf)+'\n')
    arquivo.write(str(nome)+'\n')
    arquivo.write(str(mae)+'\n')
    arquivo.write(str(pai)+'\n')
    arquivo.write(str(rg)+'\n')
    arquivo.write(str(telefone)+'\n')
    arquivo.write(str(celular)+'\n')
    arquivo.write(str(email)+'\n')
    arquivo.write(str(rua)+'\n')
    arquivo.write(str(numcasa)+'\n')
    arquivo.write(str(bairro)+'\n')
    arquivo.write(str(cidade)+'\n')
    arquivo.write(str(estado)+'\n')
    arquivo.write(str(cep)+'\n')
    arquivo.write(str(pais)+'\n')
    arquivo.close()

    pass
def validacao (cpf):
    valido = True
    lista = []
    lista = input("Informe o CPF do cliente: ")
    i = 0
    encontrou = False
    for i in range(len(cpf)):
        if lista == cpf[i]:
            encontrou = True
            break
    if encontrou==True:
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
                and (lista[4] == lista[5]) and (lista[5] == lista[6]) and (lista[6] == lista[7]) and (
                        lista[7] == lista[8])
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

def valida_email(email):
    em = input('Informe o email:')
    email.append(em)
    if len(em)<9:
        print('E-mail invalida:')
    elif ' ' in em:
        print('E-mail invalido:')
    else:
        x = em.split('@')
        if len(x)!= 2 or len(x[0])==0:
            print('E-mail invalido')
        else:
            x = x[1].split('.')
            if len(x) != 2 or len(x[0])==0:
                print('E-amil invalido')
            elif len(x[1])==0:
                print('E-mail invalido')
            else:
                pass
def salva_banco():
    print("Digite 'sim ou s' para salvar e 'nao ou n' para nao salvar")
    salvar = input("Deseja salvar no banco:")
    if salvar == 'sim' or salvar == 's':
        print(" Salvo")
    else:
        salvar == 'nao' or salvar == 'n'
        print("não Salvo")
        pass

def remover():
    i = 0
    encontrou = False
    for i in range(len(cpf)):
        if documento == cpf[i]:
            encontrou = True
            break

    if encontrou:
        del cpf[i]
        del nome[i]
        del mae[i]
        del pai[i]
        del rg[i]
        del telefone[i]
        del celular[i]
        del email[i]
        del rua[i]
        del numcasa[i]
        del bairro[i]
        del cidade[i]
        del estado[i]
        del cep[i]
        del pais[i]
        print('concluido')
    else:
        print('O Cliente não possui cadastro!')

def lista1():

    '''cpf = arquivo.readline()
    nome = arquivo.readline()
    mae= arquivo.readline()
    pai= arquivo.readline()
    rg= arquivo.readline()
    telefone= arquivo.readline()
    celular= arquivo.readline()
    email= arquivo.readline()
    rua= arquivo.readline()
    numcasa= arquivo.readline()
    bairro= arquivo.readline()
    cidade= arquivo.readline()
    estado= arquivo.readline()
    cep= arquivo.readline()
    pais= arquivo.readline()'''
    lisst=cpf,nome
    lista.append(lisst)
    print(lista)
    print('CPF :',cpf)
    print('NOME :',nome)
    print('NOME DA MAE:',mae)
    print('NOME DO PAI:',pai)
    print('RG:',rg)
    print('TELEFONE:',telefone)
    print('CELULAR:',celular)
    print('E-MAIL:',email)
    print('NOME DA RUA:',rua)
    print('Nº DA CASA:',numcasa)
    print('BAIRRO:',bairro)
    print('CIDADE:',cidade)
    print('ESTADO:',estado)
    print('CEP:',cep)
    print('PAIS:',pais)

    #arquivo.close()
    pass
opcao = menu()
while opcao != '4':
    if opcao == '1':
        inserir()
    elif opcao == '2':
        documento = input("Informe o CPF do cliente que deseja excluir:")
        remover()
    elif opcao == '3':
        lista1()
    elif opcao == '4':
        break


    opcao = menu()

