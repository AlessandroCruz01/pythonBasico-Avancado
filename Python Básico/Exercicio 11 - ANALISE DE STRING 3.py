# -*- coding: latin1 -*-

#11)PROGRAMA QUE LEIA UMA FRASE
#QUANTAS VEZES APARECE A LETRA "A"
#EM QUE POSI��O ELE APARECE PELA 1� VEZ
#EM QUE POSI��O ELE APARECE PELA ULTIMA VEZ

#////////////////////////////////////////////////#

frase = str(input("Digite: ")).strip().upper()
print('Nessa frase temos {} letras "A"'.format(frase.count('A')))
print('A letra "A" aparece primeiro na posi��o {}'.format(frase.find("A")+1))
print('A letra "A" aparece pela ultima vez na posi��o {}'.format(frase.rfind("A")+1))
