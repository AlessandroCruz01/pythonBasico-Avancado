nome = str(input("nome: ")).strip().capitalize()

n = nome.split()
print('Seu primeiro nome: {}'.format(n[0]))
print('Seu ultimo nome: {}'.format(n[len(n)-1]))
print(n[0], n[len(n)-1])