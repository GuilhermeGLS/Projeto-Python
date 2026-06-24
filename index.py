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