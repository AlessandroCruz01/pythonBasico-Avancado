from selenium import webdriver
from time import sleep
class Bot():
    def nome(self):
        self.name = input('Digite o nome da pessoa/grupo do seu celular: ')
        self.user = driver.find_element_by_xpath(f'//span[@title = "{self.name}"]')
        self.user.click()
        self.menu()

    def aviso(self):
        self.name = input('Digite o nome da pessoa/grupo do seu celular: ')
        self.user = driver.find_element_by_xpath(f'//span[@title = "{self.name}"]')
        self.user.click()
        self.msg = []
        self.texto = input('Digite sua mensagem: ')
        self.msg.append(self.texto)
        self._enviar()

    def menu(self):
        self.msg = ['Bem vindo ao serviço de atendimento da Unimeta. Eu sou o Pedrinho, o seu robo digital e estou aqui para lhe ajudar a tirar duvidas sobre os serviços da secretaria. Por favor digite os numeros correspondentes para cada atendimento',\
                    '1- Solicitação de um documento', '2- Problemas financeiros', '3- Sair']

        self._enviar()
        self._resposta()
        if self.x == '1':
            self.documento()
        elif self.x == '2':
            self.financeiro()
        elif self.x == '3':
            self.msg = ['Tudo bem, foi um prazer lhe ajudar a tirar sua duvida :)']
            self._enviar()

    def _enviar(self):
        print(self.msg)
        self.msg_box = driver.find_element_by_class_name('_2S1VP')
        for i in range(len(self.msg)):
            self.msg_box.send_keys(self.msg[i])
            self.button = driver.find_element_by_class_name('_35EW6')
            self.button.click()

    def _resposta(self):
        sleep(20)
        self.x = driver.find_elements_by_class_name('Tkt2p')[-1].text
        print(x)
        print('------------------')
        self.x = self.x[0]
        print(self.x)

    def documento(self):
        self.msg = ['Então voce esta com duvidas sobre as solicitação de documentos hahaha, rlx é normal isso acontecer. Seguinte quero que voce me fala qual documento voce deseja:'
            ,'1- Carteira de estudante', '2- Declaração para Passe de Onibus', '3- Voltar','4- Sair']
        self._enviar()
        self._resposta()
        if self.x == '1':
            self.msg = ['Infelizmente por se tratar de uma simulação o programa sera fechado :(']
            self._enviar()
        elif self.x == '2':
            self.msg = ['Infelizmente por se tratar de uma simulação o programa sera fechado :(']
            self._enviar()
        elif self.x == '3':
            self.msg = ['Tudo bem, Voltando para a seção anterior :)']
            self._enviar()
            self.menu()
        elif self.x == '4':
            self.msg = ['Tudo bem, foi um prazer lhe ajudar a tirar sua duvida :)']
            self._enviar()

    def financeiro(self):
        self.msg = ['Então voce esta com duvidas sobre situações financeiras? Seguinte quero que voce me fala que tipo de situação voce deseja:'
            ,'1- Negociamento de dividas', '2- Financiamentos', '3- Voltar','4- Sair']
        self._enviar()
        self._resposta()
        if self.x == '1':
            self.msg = ['Infelizmente por se tratar de uma simulação o programa sera fechado :(']
            self._enviar()
        elif self.x == '2':
            self.msg = ['Infelizmente por se tratar de uma simulação o programa sera fechado :(']
            self._enviar()
        elif self.x == '3':
            self.msg = ['Tudo bem, Voltando para a seção anterior :)']
            self._enviar()
            self.menu()
        elif self.x == '4':
            self.msg = ['Tudo bem, foi um prazer lhe ajudar a tirar sua duvida :)']
            self._enviar()
b = Bot()
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
while True:
    print('1- Dar um aviso\n2- Realizar um atendimento\n3- Sair')
    x = int(input())
    if x == 1:
        b.aviso()
    elif x == 2:
        b.nome()
    elif x == 3:
        break
    else:
        print('Digite um numero do menu :)')