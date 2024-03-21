from selenium.common.exceptions import TimeoutException
import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.common.exceptions import *
# You can use headless mode to not show the google chrome window open


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=en', '--window-size=1300,1000']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1

    })

    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )

    return driver, wait

# Campo Login


def automatizar_conexoes_linkedin(profissao):
    driver, wait = iniciar_driver()
    # 1. Opening the linkedin website
    driver.get('https://www.linkedin.com/login')
    # 2. Enter the log in
    campo_login = wait.until(condicao_esperada.visibility_of_element_located(
        (By.XPATH, "//input[@id='username']")))
    sleep(random.randint(1, 3))
    campo_login.click()
    sleep(random.randint(1, 3))
    campo_login.send_keys('joaohenrique1231500@gmail.com')
    sleep(random.randint(1, 3))
    campo_senha = wait.until(condicao_esperada.visibility_of_element_located(
        (By.XPATH, "//input[@id='password']")))
    sleep(random.randint(1, 3))
    campo_senha.click()
    sleep(random.randint(1, 3))
    campo_senha.send_keys('your_custom_password')
    sleep(random.randint(1, 3))
    campo_sign = wait.until(condicao_esperada.visibility_of_element_located(
        (By.XPATH, "//button[text()='Sign in']")))
    sleep(random.randint(1, 3))
    campo_sign.click()
    sleep(random.randint(3, 6))

    driver.get(
        'https://www.linkedin.com/search/results/people/?keywords=developer&origin=SWITCH_SEARCH_VERTICAL&sid=~Mn')

    sleep(3)
    existe_proxima_pagina = True

    while existe_proxima_pagina is True:
        sleep(3)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollTop);")

        try:
            # 8. Verify if the field contains the text "connect"
            botoes_conectar = wait.until(condicao_esperada.visibility_of_all_elements_located(
                (By.XPATH, "//button//span[text()='Connect']")))
        except TimeoutException:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            botao_proximo = wait.until(condicao_esperada.element_to_be_clickable(
                (By.XPATH, "//span[@class='artdeco-button__text' and text()='Next']")))
            sleep(random.randint(1, 3))
            botao_proximo.click()
            sleep(random.randint(1, 3))
            continue

        for botao in botoes_conectar:
            botao.click()
            sleep(random.randint(1, 3))
            # 9. Click in the connect field
            nome_contato = wait.until(condicao_esperada.visibility_of_element_located(
                (By.XPATH, "//span[@class='flex-1']//strong")))
            sleep(random.randint(1, 3))
            nome_contato = nome_contato.text
            nome_contato = nome_contato.split()[0]

            # 10. localize the add field
            botao_adicionar_nota = wait.until(condicao_esperada.visibility_of_element_located(
                (By.XPATH, "//button[@aria-label='Add a note']")))
            sleep(random.randint(2, 4))
            botao_adicionar_nota.click()
            sleep(random.randint(1, 3))
            # 11. Extract the name of the person for a personalized message

            # 12. Include the name in a personalized message
            mensagem_personalizada = f"Hi {
                nome_contato}, my name is Joao. I’m a Python software developer, always looking to evolve in my field. I believe that connecting with talented people always motivates us to progress. Regardless, I liked your profile and would like to keep in touch. Best regards!"

            # 14. Typing the message
            campo_mensagem_convite = wait.until(condicao_esperada.visibility_of_element_located(
                (By.XPATH, "//textarea[@name='message']")))
            sleep(random.randint(1, 3))

            campo_mensagem_convite.send_keys(mensagem_personalizada)
            sleep(5)
            botao_enviar = wait.until(condicao_esperada.visibility_of_element_located(
                (By.XPATH, "//button[@aria-label='Send now']")))
            sleep(random.randint(1, 3))
            botao_enviar.click()
            sleep(random.randint(1, 3))

        try:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            botao_proximo = wait.until(condicao_esperada.element_to_be_clickable(
                (By.XPATH, "//span[@class='artdeco-button__text' and text()='Next']")))
            sleep(random.randint(1, 3))
            botao_proximo.click()
            sleep(random.randint(1, 3))
        except Exception as error:
            print('Automação chegou até a última página')
            existe_proxima_pagina = False
            driver.close()


automatizar_conexoes_linkedin("Python")
