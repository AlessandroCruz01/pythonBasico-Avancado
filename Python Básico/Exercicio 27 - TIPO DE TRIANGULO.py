sa=float(input("Segmento A: "))
sb=float(input("Segmento B: "))
sc=float(input("Segmento C: "))

if sa<sb+sc and sb<sa+sc or sc<sa+sb:
    print("pode formar um triangulo", end=' ')
    if sa==sb==sc:
        print('EQUILATERO')
    elif sa != sb != sc != sa:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print("Não forma um triangulo")