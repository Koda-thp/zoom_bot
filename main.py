import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
import webbrowser

def sign_in():
    url = 'https://us02web.zoom.us/j/6047234276?pwd=aStIMnVyanVPM2phakZUMEpSOTJSdz09'
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(url)
    time.sleep(10)
    print('signed in')
    grand_btn = pyautogui.locateOnScreen('grand.png')
    pyautogui.moveTo(grand_btn)
    pyautogui.doubleClick()
    print('full screen')
    time.sleep(1)
    pyautogui.keyDown('alt')  # hold down the shift key
    pyautogui.press('a')     # press the left arrow key
    pyautogui.keyUp('alt')    # release the shift key
    print('mute')
    time.sleep(1)
    pyautogui.keyDown('alt')  # hold down the shift key
    pyautogui.press('h')     # press the left arrow key
    pyautogui.keyUp('alt')    # release the shift key
    time.sleep(2)
    pyautogui.write('Bonjour, desolé pour le retard jai des gros soucis avec mon pc il plante souvent mais je suis la')
    pyautogui.press('enter') 
    print('appelle')

# Reading the file
df = pd.read_csv('timings.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):
        row = df.loc[df['timings'] == now]
        sign_in()
        time.sleep(50)
        print('end')
