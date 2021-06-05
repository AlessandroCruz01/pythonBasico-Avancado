#Escrevam uma classe em python chamada Inteiro que receba como parametro um valor, que se for um numero inteiro válido.
# Ele guarda como atributo. Caso contrário gera um erro informando que nao é um numero inteiro válido;

#
# class Inteiro():
#     def __init__(self, num):
#         self.num = num
#5
# try:
#     a = Inteiro(num=int(input('Digite um numero inteiro: ')))
#     print(a.num)
#     raise Exception('Erro especifico')
# print('fim')

# class Real():
#     def __init__(self, valor):
#         try:
#             self.valor = float(valor)
#         except:
#             raise Exception('NUMERO NÃO É REAL')
#
#     def __str__(self):
#         return ('%.3f'%self.valor).replace('.',',')#TROCA PONTO POR VIRGULA
#
#     def __add__(self, y): #PARA SOMAR
#          return  self.valor+y
#
#     def __sub__(self, y): #PARA SUBTRAIR
#         return self.valor - y
#
#     def __truediv__(self, y):#PARA DIVIDIR
#         return self.valor / y
#
#     def __mul__(self, y):#PARA MULTIPLICAR
#         return self.valor * y
#
#     def __eq__(self, y):#PARA NUMEROS IGUAIS
#         return self.valor == y
#
#     def __gt__(self,y): #MAIOR QUE
#         return self.valor>y
#
#     def __lt__(self, y): #MENOR QUE
#         return self.valor<y
#
#     def __ge__(self, y): #MAIOR OU IGUAL QUE
#         return self.valor >= y
#
#     def __le__(self, y): #MENOR OU IGUAL QUE
#         return self.valor <= y
#
# x = Real(input('Digita: '))
# print(x)
# print(x + 10)
# print(x - 10)
# print(x / 10)
# print(x * 10)
# print(10.0==10)
# print(x==10)
# print(x>10) #__gt__
# print(x<10) #__lt__
# print(x>=10) #__ge__
# print(x<=10) #__le__

class Real():
    def __init__(self, valor):
        try:
            self.valor = float(valor)
        except:
            raise Exception('NUMERO NÃO É REAL')

    def __str__(self):
        return ('%.3f'%self.valor).replace('.',',')#TROCA PONTO POR VIRGULA

    def __add__(self, y): #PARA SOMAR
         return  self.valor+y

    def __sub__(self, y): #PARA SUBTRAIR
        return self.valor - y

    def __truediv__(self, y):#PARA DIVIDIR
        return self.valor / y

    def __mul__(self, y):#PARA MULTIPLICAR
        return self.valor * y

    def __eq__(self, y):#PARA NUMEROS IGUAIS
        return self.valor == y

    def __gt__(self,y): #MAIOR QUE
        return self.valor>y

    def __lt__(self, y): #MENOR QUE
        return self.valor<y

    def __ge__(self, y): #MAIOR OU IGUAL QUE
        return self.valor >= y

    def __le__(self, y): #MENOR OU IGUAL QUE
        return self.valor <= y




x = Real(input('Digita: '))
print(x)
print(x + 10)
print(x - 10)
print(x / 10)
print(x * 10)
print(10.0==10)
print(x==10)
print(x>10) #__gt__
print(x<10) #__lt__
print(x>=10) #__ge__
print(x<=10) #__le__