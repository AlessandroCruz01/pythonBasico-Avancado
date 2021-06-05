salario = float(input("DIGITE SEU SALÁRIO: "))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print("Quem recebia R${:.2f} passa a ganhar {:.2f}".format(salario, novo))