# Make sure you have WhatsApp Desktop installed for this bot to work properly

import webbrowser
import pyautogui
from time import sleep
import random

phones = [14244130770, 5543991481870, 5543999756125]

for phone in phones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={phone}')
    sleep(random.randint(5, 10))
    pyautogui.click(750, 400, duration=1)
    sleep(random.randint(5, 10))
    pyautogui.typewrite(
        'Would you like to attend our event? (type yes if you would like to participate.')
    sleep(random.randint(5, 10))
    pyautogui.press('enter')
    sleep(10)

# /usr/local/bin/python3 /Users/joaomelo/Programacao/mestres_da_automacao/Pyautogui/whatsappbot.py
