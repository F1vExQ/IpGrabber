import subprocess
import time
import random
import pyautogui as pyauto
import rotatescreen as rs
import webbrowser


pd = rs.get_primary_display()
angel_list = [90, 180, 270, 0]
for i in range(5):
    for x in angel_list:
        pd.rotate_to(x)
        time.sleep(0.5)
        webbrowser.open('https://whatismyipaddress.com/')
    subprocess.call('calc.exe')
