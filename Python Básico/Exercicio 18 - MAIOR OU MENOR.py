a = int(input("1º digito: "))
b = int(input("2º digito: "))
c = int(input("3º digito: "))

#VERIFICANDO O MENOR:
menor = a
if a>b and b<c:
    menor=b
if c<a and c<b:
    menor =c

#VERIFICANDO O MAIOR
maior = a
if a<b and b>c:
    maior = b
if c>a and c>b:
    maior=c

print("o maior é {} e o menor é {}".format(maior , menor))