import time
import pyautogui

pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('youtube.com')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','t')
#melhor que achar a nova aba e usar o atalho para criar ela pois meu pc esta tv resolucao diferente notebook
#pyautogui.click(x=332, y=17)
pyautogui.write('netflix.com')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','shift','N')
pyautogui.write('https://www.youtube.com/@AlexandreBorgmannFPV')
pyautogui.press('enter')