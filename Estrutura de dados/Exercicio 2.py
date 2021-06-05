# '''1. Escreva um programa em Python que lê três números inteiros do teclado, e imprime os três números em ordem crescente.'''
# print('Exercicio 1')
#
# lista = []
# a=0
# for i in range(3):
#     x = (input("Digita o {}º numero inteiro: ".format(i+1)))
#     lista.append(x)
#
# menor=lista[0]
# if lista[0] > lista[1] and lista[1] < lista[2]:
#     menor = lista[1]
# if lista[2] < lista[1] and lista[2] < lista[1]:
#     menor = lista[2]
#
# meio = lista[0]
# if lista[0] < lista[1] and lista[1] < lista[2]:
#     meio = lista[1]
# if lista[2] > lista[0] and lista[2]< lista[1]:
#     meio = lista[2]
#
# maior=lista[0]
# if lista[0] < lista[1] and lista[1] > lista[2]:
#     maior = lista[1]
# if lista[2] > lista[1] and lista[2] > lista[1]:
#     maior = lista[2]
#
#
# print("{} , {}, {}".format(menor,meio, maior))
#
#
#
#
# '''2. Idem, três números reais.'''
# print('\n','Exercicio 2')
# lista = []
# a=0
# for i in range(3):
#     x = float(input("Digita {}º numero real: ".format(i+1)))
#     lista.append(x)
#
# menor=lista[0]
# if lista[0] > lista[1] and lista[1] < lista[2]:
#     menor = lista[1]
# if lista[2] < lista[1] and lista[2] < lista[1]:
#     menor = lista[2]
#
# meio = lista[0]
# if lista[0] < lista[1] and lista[1] < lista[2]:
#     meio = lista[1]
# if lista[2] > lista[0] and lista[2]< lista[1]:
#     meio = lista[2]
#
# maior=lista[0]
# if lista[0] < lista[1] and lista[1] > lista[2]:
#     maior = lista[1]
# if lista[2] > lista[1] and lista[2] > lista[1]:
#     maior = lista[2]
#
# print("{} , {}, {}".format(menor,meio, maior))
#
#
# '''3. Escreva uma função em Python que recebe como parâmetro uma frase e calcule o número de letras (maiúsculas e minúsculas) da frase passada, transformando a frase em uma lista.
# *para transforma uma string em uma lista utilize a função list()'''
#
# print('\n','Exercicio 3')
# def Lista_string(frase):
#     list(frase)
#     mai = 0
#     men = 0
#     for i in frase:
#         if i == i.upper():
#             mai +=1
#         else:
#             men +=1
#     print("Nessa frase há {} maiusculas e {} minusculas".format(mai, men))
# x = input("Digita uma frase: ").replace(' ', '')
# Lista_string(x)
#
# '''4. Escreva uma função que converte todas as letras de uma lista para maiúsculas.'''
# print('\n', 'Exercicio 4')
# x = str(input("DIGITA UMA FRASE: "))
# list(x)
# for i in x:
#     i = i.upper()
#     print(i, end='')
#
# '''5. Escreva uma função que recebe como entrada uma lista, e devolve como saída uma cópia da cadeia invertida. O último elemento vira o primeiro e o primeiro vira o último.'''
#
# print("\n", "Exercicio 5")
# lista = []
# el = int(input("Quantos elementos deseja adicionar a lista: "))
# for i in range(el):
#     x = int(input("Digite o {}º elemento inteiro: ".format(i+1)))
#     lista.append(x)
# lista1 = lista #Cópia
# lista1.reverse()
# for i in lista1:
#     print(i, end=" ")

'''7. Idem, convertendo as letras da cópia para maiúsculas.
'''

print("\n", "Exercicio 7")

x = str(input("Digite o uma frase: "))
list(x)
x = x.reverse()
for i in x:
    print(i)






