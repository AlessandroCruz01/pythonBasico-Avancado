# -*- coding: latin1 -*-

import datetime
#modulo pra ano atual levando em considera��o a maquina


ano = int(input("DIGITE: *clique zero para analisar o ano atual! "))
if ano==0:
    ano = datetime.date.today().year#comando para pegar ano atual
if ano % 4 == 0 and (ano % 100)!=0 or ano % 400 == 0:
    print("O ano {} � BISSEXTO".format(ano))

else:
    print("O ano de {} N�O � BISSEXTO".format(ano))
