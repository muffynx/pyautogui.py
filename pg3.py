import pyautogui as pg
pg.hotkey('ctrl','shift','t')
pg.write('sudo apt update && sudo apt upgrade -y')
pg.press('enter')