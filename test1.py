
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


time.sleep(2)
pg.click(100,564) #click ตรงขอบ Point(x=100, y=564)
pg.keyDown('tab')
pg.hotkey('tab')  
pg.keyDown('tab')
pg.hotkey('tab')  
pg.keyDown('tab')
pg.press('enter')
time.sleep(2)
pg.click(625,315) #select server linux
pg.hotkey('down')
pg.hotkey('enter')
time.sleep(1)
pg.click(638,450) 
pg.hotkey('tab')
pg.write('Muffyn29300.')
pg.hotkey('tab')
pg.write('muffyn2')
#pg.hotkey('enter')