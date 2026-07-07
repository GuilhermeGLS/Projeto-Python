import pyautogui
import time

pyautogui.PAUSE = 0.5

link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'

# entrar no (sistema)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=650, y=1255, clicks=1)
pyautogui.write(link)
pyautogui.press('enter')

# Navegar no Sistema
time.sleep(1)
pyautogui.click(x=425, y=450, clicks=2)
pyautogui.press('f11')
time.sleep(1.4)
pyautogui.click(x=2328, y=304, clicks=1)
time.sleep(4)
pyautogui.click(x=1004, y=734, clicks=1)
pyautogui.press('f11')

#Calcular os indicadores
import pandas

caminho = r"C:\Users\Guimas\Downloads\Vendas - Dez.xlsx"
tabela = pandas.read_excel(caminho)

#print(tabela)
#dentro do ipynb, para exibir a tabela de forma mais bonita, podemos usar o display
display(tabela)

faturamento = tabela["Valor Final"].sum()

qtde_produto = tabela["Quantidade"].sum()

print(faturamento)
print(qtde_produto)


import pyautogui
import time

pyautogui.PAUSE = 1.2

link_email = 'https://mail.google.com/mail/u/0/#inbox?compose=new'
email_destinatario = "marilumaildo@gmail.com"

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
print(pyautogui.position())
pyautogui.click(x=1129, y=853, clicks=1)
pyautogui.write(link_email)
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=89, y=292, clicks=1)
time.sleep(3)
pyautogui.write(email_destinatario)
time.sleep(2)
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.write("relatório de vendas")
pyautogui.press('tab')
pyautogui.write(f"faturamento: {faturamento}")
pyautogui.press('enter')
pyautogui.write(f"Quantidade venda {qtde_produto}")
pyautogui.click(x=1647, y=1485, clicks=1)

