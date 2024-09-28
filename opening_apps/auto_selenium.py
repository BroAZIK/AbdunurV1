import pyautogui
import time
import subprocess

# Telegramni ishga tushirish

def open_telegram():
    subprocess.Popen(["C:/Users/user/AppData/Roaming/Telegram Desktop/Telegram.exe"])
    time.sleep(5)
    return "Telegram ochildi"

def search_telegam(text):
    pyautogui.click(x=200, y=35)
    pyautogui.write(text)
    time.sleep(2)
    return "Qidiruv natijalari"
    # pyautogui.press('enter')


def open_youtube():
    

    subprocess.Popen(['C:/Program Files/Google/Chrome/Application/chrome.exe', 
                      '--profile-directory=Default', 
                      '--app-id=agimnkijcaahngcdmfeangaknmldooml'])
    time.sleep(1)
    pyautogui.press('f11')
    return "YouTube ochildi"

def search_youtube(text):
    pyautogui.click(x=1150, y=50)
    pyautogui.write(text)
    time.sleep(2)
    pyautogui.press('enter')
