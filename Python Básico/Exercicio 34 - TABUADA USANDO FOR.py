# -*- coding: latin1 -*-
from __future__ import division

num = 0

while num<=10:
    for i in range(0,11):
        print('{} + {} = {}'.format(num, i, (num+i)))
    num=num+1
    print('-=' * 30)

num=0

while num<=10:
    for i in range(0,11):
        print('{} x {} = {}'.format(num, i, (num*i)))
    num=num+1
    print('-=' * 30)

num=0

while num <= 10:
    for i in range(0, 11):
        print('{} - {} = {}'.format(num, i, (num - i)))
    num = num + 1
    print('-=' * 30)

num=0
(float(num))

while num <= 10:
    for i in range(1, 11):
        print('{} / {} = {:.2f}'.format(num, i,(num/i)))
    num = num + 1.0
    print('-=' * 30)
