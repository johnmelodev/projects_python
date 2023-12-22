# 1 - Navigate to the site https://www.instagram.com
import webbrowser
import pyautogui
from time import sleep

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

while True:
    webbrowser.get(chrome_path).open_new_tab('https://www.instagram.com')

    sleep(1)
    # 2 - Enter my username
    pyautogui.click(1539,362,duration=1)
    sleep(1)
    pyautogui.typewrite('yourlogin')
    sleep(1)
    # 3 - Enter my password
    pyautogui.click(1546,398,duration=1)
    sleep(1)
    pyautogui.typewrite('yourpassword')
    sleep(1)
    # 4 - Click on "log in"
    pyautogui.click(1567,445,duration=1)
    sleep(20)
    # 5 - Click on "Not now" to not save browser
    pyautogui.click(1590,603,duration=1)
    sleep(20)
    # 6 - Close "save password" window
    pyautogui.click(1662,88,duration=1)
    sleep(1)
    # 7 - Search for the page
    pyautogui.click(1526,105,duration=1)
    sleep(1)
    pyautogui.typewrite('nike')
    sleep(1)
    # 8 - Enter the page
    pyautogui.move(0,50,duration=1)
    sleep(1)
    pyautogui.click()
    sleep(20)
    # 9 - Click on the most recent post
    pyautogui.click(1398,595,duration=1)
    sleep(10)
    # 10 - Check if I have already liked the post or not
    heart = pyautogui.locateCenterOnScreen('heart.png')
    sleep(1)
    # 11 - If I have already liked it, do nothing, and pause the bot for 24 hours
    if heart is not None:
        sleep(86400)
    # 12 - If I have not liked it, like the photo
    elif heart == None:
        pyautogui.click(1468,746,duration=1)
        sleep(5)
        # 13 - If I have not liked it, comment on the photo
        pyautogui.click(1505,749,duration=1)
        sleep(3)
        pyautogui.click(1568,834,duration=1)
        sleep(1)
        pyautogui.typewrite('Good picture!')
        sleep(5)
        pyautogui.click(1715,832,duration=1)
        # 14 - Pause for 24 hours
        sleep(86400)
