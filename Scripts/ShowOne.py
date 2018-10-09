import pyautogui as pg
import time

pg.hotkey('winleft','i')
time.sleep(1)
pg.click(380,240) #clicks system

time.sleep(1)
pg.scroll(-500) #scrolls to display change

time.sleep(1)
pg.click(490,840) #clicks to choose display options

time.sleep(1)
pg.click(400,874) #clicks to show only 1 display

time.sleep(1)
pg.click(1134,561) #clicks to keep changes

time.sleep(1)
pg.hotkey('alt','f4')
