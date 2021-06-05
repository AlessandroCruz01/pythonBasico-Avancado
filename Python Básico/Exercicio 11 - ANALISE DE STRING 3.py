# -*- coding: latin1 -*-

#11)PROGRAMA QUE LEIA UMA FRASE
#QUANTAS VEZES APARECE A LETRA "A"
#EM QUE POSIÇÃO ELE APARECE PELA 1º VEZ
#EM QUE POSIÇÃO ELE APARECE PELA ULTIMA VEZ

#////////////////////////////////////////////////#

frase = str(input("Digite: ")).strip().upper()
print('Nessa frase temos {} letras "A"'.format(frase.count('A')))
print('A letra "A" aparece primeiro na posição {}'.format(frase.find("A")+1))
print('A letra "A" aparece pela ultima vez na posição {}'.format(frase.rfind("A")+1))
