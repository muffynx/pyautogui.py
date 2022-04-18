#you must login on my.xver before usetime
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


pg.click(690,47) #click
pg.keyDown('tab')

pg.hotkey('tab')  
pg.keyDown('tab')

pg.hotkey('tab')  
pg.keyDown('tab')

pg.hotkey('tab')

time.sleep(1)
pg.press('enter')
time.sleep(1)
pg.click(1207,120) #click icon del server
