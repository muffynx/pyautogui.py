#you must login on facebook before use
import time
import pyautogui as pg
pg.hotkey('win','r')
pg.write('chrome')
pg.hotkey('enter')
time.sleep(1)
pg.write("facebook.com")
pg.press('enter')
pg.press('f11')
time.sleep(1)
