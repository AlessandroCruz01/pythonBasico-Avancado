from kivy.app import App
from kivy.uix.label import Label
from sqlite3 import *
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager as Manager, Screen
from kivy.uix.floatlayout import FloatLayout

class RedefinirSenha(Screen):
    pass

class Inicio(Screen):
    pass

class Login(Screen):
    # **********************************#
    def getNr_cpf(self):
        return self.ids.cpf.text

    def getNr_senha(self):
        return self.ids.senha.text

    def getNm_email(self):
        return self.ids.email.text
    # **********************************#
    def limparCamposLogin(self):
        self.ids.cpf.text = ''
        self.ids.senha.text = ''

    def verificarAcesso(self):
        cpf = self.getNr_cpf()
        senha = self.getNr_senha()

        conexao = connect('Login.db')
        cursor = conexao.cursor()
        sql = '''SELECT 
                        nr_cpf, 
                        nr_senha 
                FROM login 
                WHERE nr_cpf = ("%s")''' % (cpf)
        cursor.execute(sql)
        busca = cursor.fetchone()

        try:
            if (cpf == busca[0]):
                if (senha == busca[1]):
                    self.limparCamposLogin()
                    login.gerenciador.transferir('inicio', 'left')
        except:
            popup = Popup(title='Login',content=(Label(text='Login ou Senha incorretos.')))
            popup.open()



class Gerenciador(Manager):
    def transferir(self, tela, lado):
        self.current = tela
        self.transition.direction = lado

class TelaLogin(App):
    def build(self):
        self.gerenciador = Gerenciador()
        return self.gerenciador

login = TelaLogin()
login.run()