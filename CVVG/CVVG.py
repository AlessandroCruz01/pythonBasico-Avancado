from selenium import webdriver
from time import sleep
class Robo():
    def login(self):
        self.usuario = driver.find_element_by_id("DEALER-WSLXloginUserIdInput")
        self.usuario.send_keys('a-sou201')

        self.senha = driver.find_element_by_id('DEALER-WSLXloginPasswordInput')
        self.senha.send_keys('ALE19121998')

        self.botao = driver.find_element_by_id("DEALER-WSLXloginWSLSubmitButton")
        self.botao.click()



driver = webdriver.Chrome()
driver.get('https://www.wslx.dealerconnection.com/default.cgi')
sleep(5)
r = Robo()
r.login()