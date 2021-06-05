class JogodaVelha():
    x = y = campo = cada = v1 = v2 = None
    linha = []
    coluna = []
    d1 = []
    cada1 = []
    def __init__(self):
        while len(self.coluna) != 3:
            self.linha.append('1')
            if len(self.linha) == 3:
                self.coluna.append(self.colunalinha)
                self.linha = []
        counter = 1
        for i in save:
            print(f'Linha {counter}: ', i)
            counter += 1
        for i in range(len(save)):
            for y in save[i]:
                x = x + y
            linha.append(x)
            x = ''

    def atualizar(self, x, y):
        self.d1 = ['1','2','3','4','5','6','7','8','9']
        for i in x:
            self.cada = self.campo.find(i)
            self.cada1.append(self.cada)
        print(self.cada1)




        self.campo = self.campo.replace(x,'x')
        self.campo = self.campo.replace(y,'0')
        print('\n\n',self.campo)
    def seila(self):
        self.linha.insert(0, self.campo[3])
        self.linha.insert(1, self.campo[11])
        self.linha.insert(2, self.campo[20])



        print(self.linha)
        self.coluna = ['1','2','3']

class Intel(JogodaVelha):
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = None
    def __init__(self):
        self.p1 = self.campo.find()




jogo = JogodaVelha()
x = False
c = 0
while x == False:
    j1 = input('\nJogador 1: ')
    j2 = input('Jogador 2: ')
    jogo.atualizar(j1, j2)
    jogo.seila()
    c += 1
    if c == 4:
        x = True
