from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.webdriver.common.keys import Keys
import os
import random
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


def automatizar_conexoes_linkedin(profissao):
    driver, wait = iniciar_driver()
    # 1. Opening the linkedin website
    driver.get('https://linkedin.com/feed/')
    # 2. Enter the log in manually
    sleep(30)
    # 3. finding the search field by XPATH
    campo_pesquisar = wait.until(condicao_esperada.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search']")))
    sleep(random.randint(1, 3))
    # 4. Clicking on search field
    campo_pesquisar.click()
    sleep(random.randint(1, 3))
    # 5. Type the profession you wanna connect on LinkedIn
    campo_pesquisar.send_keys(profissao)
    sleep(random.randint(1, 3))
    campo_pesquisar.send_keys(Keys.ENTER)
    sleep(random.randint(5, 10))
    # 6. Identify the element "People"
    botoes_pessoa = wait.until(condicao_esperada.visibility_of_all_elements_located(
        (By.XPATH, "//button[text()='People']")))
    # 7. Clicking on "People" field
    botoes_pessoa[0].click()
    sleep(10)
    existe_proxima_pagina = True

    while existe_proxima_pagina == True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        # 8. Verify if the field contains the text "connect"
        botoes_conectar = wait.until(condicao_esperada.visibility_of_all_elements_located(
            (By.XPATH, "//button//span[text()='Connect']")))

        for botao in botoes_conectar:
            botao.click()
            sleep(random.randint(1, 3))
            # 9. Click in the connect field
            # 10. localize the add field
            botao_adicionar_nota = wait.until(condicao_esperada.visibility_of_element_located(
                (By.XPATH, "//button[@aria-label='Add a note']")))
            sleep(random.randint(1, 3))
            botao_adicionar_nota.click()
            sleep(random.randint(1, 3))
            # 11. Extract the name of the person for a personalized message
            nome_contato = wait.until(condicao_esperada.visibility_of_element_located(
                (By.XPATH, "//h2[@id='send-invite-modal']")))
            sleep(random.randint(1, 3))

            nome_contato = nome_contato.text
            nome_contato = nome_contato.split()[1]
            # 12. Include the name in a personalized message
            mensagem_personalizada = f'Hello {
                nome_contato}, my name is Joao. I’m a full stack developer, always looking to evolve in my field. I believe that connecting with talented people always motivates us to progress. Regardless, I liked your profile and would like to keep in touch. Best regards!'
            # 13. Finding the text area

            # 14. Typing the message

            campo_mensagem_convite = wait.until(condicao_esperada.visibility_of_element_located(
                (By.XPATH, "//textarea[@name='message']")))
            sleep(random.randint(1, 3))

            campo_mensagem_convite.send_keys(mensagem_personalizada)

            botao_enviar = wait.until(condicao_esperada.visibility_of_element_located(
                (By.XPATH, "//button[@aria-label='Send now']")))
            sleep(random.randint(1, 3))
            botao_enviar.click()
            sleep(random.randint(1, 3))
        try:
            botao_proximo = wait.until(condicao_esperada.element_to_be_clickable(
                (By.XPATH, "//button[@aria-label='Next']")))
            sleep(random.randint(1, 3))
            botao_proximo.click()
            sleep(random.randint(1, 3))
        except Exception as error:
            print('Automação chegou até a última página')
            existe_proxima_pagina = False
            driver.close()


automatizar_conexoes_linkedin('developer')
