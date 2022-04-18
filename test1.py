
#you must login on my.xver before use
import time
import pyautogui as pg
pg.hotkey('win','r')
pg.write('chrome')
pg.hotkey('enter')
time.sleep(1)
pg.write("https://my.xver.cloud")
pg.press('enter')
pg.press('f11') 


time.sleep(1)
pg.click(1250,110)  #click depoly server
time.sleep(1)
pg.click(625,315)  #celecp server linux
pg.hotkey('down')
pg.hotkey('enter')
time.sleep(1)
pg.click(638,450) #click plan server
pg.hotkey('tab')
pg.write('Muffyn29300.') #write password
pg.hotkey('tab')
pg.write('muffyn1')     #name server
#pg.hotkey('enter')