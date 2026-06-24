import pyautogui
import time

pyautogui.PAUSE = 0.5

link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveTo(650, 1255)
pyautogui.click()
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)
pyautogui.hotkey('alt', 'f4')