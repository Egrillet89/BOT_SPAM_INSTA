import pyautogui as pg
import time


time.sleep(3)

for i in range (100):
    pg.write(f'Lista.push(obj[{i}].innerText);')
    pg.press('enter')
    time.sleep(2)