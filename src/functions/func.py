from time import sleep
from faker import Faker
from functions.geradores import Geradores
import pyautogui

fake = Faker()


class Metra:

    def acessa():
        pyautogui.moveTo(131, 45)
        pyautogui.doubleClick(131, 45)
        sleep(15)
        pyautogui.moveTo(636, 182)
        pyautogui.click(636, 182)
        sleep(2)
        pyautogui.hotkey('ctrl', 'alt', 'shift', 'enter')
        sleep(2)

    def CadastraUsuario():
        #clica no botão clientes 
        pyautogui.moveTo(16, 69)
        pyautogui.click(16, 69)

        #clica no botão Novo Funcionario 
        pyautogui.moveTo(351, 240)
        pyautogui.click(351, 240)

        #inserindo os dados 
        pyautogui.moveTo(363, 134)
        pyautogui.click(363, 134)
        pyautogui.typewrite(fake.name())

        pyautogui.moveTo(310, 272)
        pyautogui.click(310, 272)
        pyautogui.typewrite(Geradores.gera_cpf())


    def CadastraEmpresa():
        #clica no botão empresa
        pyautogui.moveTo(639, 68)
        sleep(1)
        pyautogui.click(639, 68)
        pyautogui.moveTo(967, 551)
        pyautogui.click(967, 551)

        #insere o nome
        pyautogui.moveTo(323, 185)
        pyautogui.click(323, 185)
        pyautogui.typewrite(f'{fake.name()} inc')

        #insere CNPJ
        pyautogui.moveTo(513, 262)
        pyautogui.click(513, 262)
        pyautogui.typewrite(Geradores.gera_cnpj())

        #seleciona Convênio
        pyautogui.moveTo(750, 499)
        pyautogui.click(750, 499)
        pyautogui.moveTo(750, 515)
        pyautogui.click(750, 515)

        #Configuração eSocial
        pyautogui.moveTo(724, 135)
        pyautogui.click(724, 135)
        pyautogui.moveTo(451, 495)
        pyautogui.click(451, 495)
        pyautogui.moveTo(451, 535)
        pyautogui.click(451, 535)
      

        #clica no botão "Salvar"
        pyautogui.moveTo(844, 658)
        pyautogui.click(844, 658)
        pyautogui.moveTo(840, 765)
        pyautogui.click(840, 765)
    
    def GeraPGR():
        ...


        
