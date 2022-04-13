import pyautogui as pg
import time
pg.hotkey('ctrl','shift','t')
pg.write('sudo apt update && sudo apt upgrade -y')
pg.press('enter')
pg.write('muffyn')
pg.press('enter')
pg.sleep(100)
