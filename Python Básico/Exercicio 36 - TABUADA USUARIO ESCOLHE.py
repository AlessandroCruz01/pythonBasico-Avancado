# -*- coding: latin1 -*-

def linha():
    print('-='*30)

num=int(input("Digite o numero: "))

for i in range(0,11):
    print('{} + {} = {}'.format(num, i, (num+i)))

linha()

for i in range(0,11):
    print('{} - {} = {}'.format(num, i , (num-i)))

linha()

for i in range(0,11):
    print('{} x {} = {}'.format(num, i , (num*i)))

linha()

for i in range(1,11):
    num=float(num)
    print('{} / {} = {:.2f}'.format(num, i , (num/i)))