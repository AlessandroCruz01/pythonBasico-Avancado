sa=float(input("Segmento A: "))
sb=float(input("Segmento B: "))
sc=float(input("Segmento C: "))

if sa<sb+sc and sb<sa+sc or sc<sa+sb:
    print("pode formar um triangulo")
else:
    print("Não forma um triangulo")