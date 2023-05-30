import os
import time
import random as rand
import pyautogui as py
import webbrowser as browser

# acessando o navegador
url = 'https://'
browser.open_new_tab(url)
# espera 10 segundos o navegador
time.sleep(10)

# login - digitando o usuário e senha
py.write('leonardo')
py.press('tab')

# acessando o arquivo para pegar a senha
with open('C://Users//Suporte//Desktop//pass.txt') as passwd:
    password = passwd.read()

py.write(password)
py.press('tab', interval=0.25)
py.click(x=775, y=655, interval=18.0)

# abrindo menu o sistema
py.click(x=25, y=105, interval=1.5)
# acessando alterar senha
py.moveTo(x=65, y=175, duration=0.75)
py.click(x=65, y=175, clicks=2, duration=0.5)

# alterando as senhas
py.write(password)
py.press('tab', interval=0.25)

try:
	# removendo o arquivo com a senha antiga
	os.remove('C://Users//Suporte//Desktop//pass.txt')
	# se apagar, cria nova senha criando arquivo com a nova senha
	new_password  = str(rand.randrange(1995, 9999))
except FileNotFoundError:
  new_password = password

# reescrevendo o arquivo e guardando a nova senha
with open('C://Users//Suporte//Desktop//pass.txt', 'w') as passwd:
    passwd.write(new_password)
    
# acessando o arquivo para pegar a senha
with open('C://Users//Suporte//Desktop//pass.txt') as passwd:
    password = passwd.read()
    
# ocultando arquivo criado
os.system(command='attrib +s +h C://Users//Suporte//Desktop//pass.txt')

# digitando a nova senha
py.write(password)
py.press('tab', interval=0.25)
py.write(password)
py.click(x=165, y=270, duration=1.5)
time.sleep(2)
py.press('enter', interval=0.25)

# abrindo a lista de clientes do menu principal
py.click(x=465, y=280, interval=1.5)
# voltando para o menu principal
py.click(x=30, y=130, interval=3.0)

# abrindo os chamados do menu principal
py.click(x=465, y=341, clicks=2, interval=1.0)
