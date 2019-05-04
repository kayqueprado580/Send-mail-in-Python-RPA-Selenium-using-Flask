from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

global mail_list
global mail_user
global mail_pwd
global mail_assunt
global mail_msg

def start():
    openBrowser()
    login("kayqueprado2015@gmail.com", "Kayqueprado@2018")
    enviar_email("kayqueprado2015@gmail.com", "teste", "Ola esse e um email teste")
    sleep(30)
    kill()

def connection():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except:
        openBrowser()
def openBrowser():
    global driver
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.set_page_load_timeout(100)
    driver.get("https://gmail.com/")

    elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="initialView"]/div[2]'))
    )

def login(mail_user, mail_pwd):
    global user
    global pwd
    user = mail_user
    pwd = mail_pwd

    #inserir email
    email = driver.find_element_by_xpath('//*[@id="identifierId"]')
    email.send_keys(mail_user)

    #clicK next
    proximo = driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
    proximo.click()

    sleep(2)

    try:
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    except:
        print("Email informado é inválida!")
        sleep(10)
        kill()


    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="profileIdentifier"]'))
    )
    senha = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    senha.send_keys(mail_pwd)

    sleep(1)
    login = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
    login.click()

    sleep(5)

    try:
        driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div[2]')
    except:
        print("Senha informada é inválida!")
        sleep(10)
        kill()

def enviar_email(mail_list, mail_assunt, mail_msg):
    global emails
    global assunto
    global mensagem
    emails = mail_list
    assunto = mail_assunt
    mensagem = mail_msg
    contador = 0

    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")

    while contador < 3:
        try:
            email = driver.find_element_by_name('to')
            email.send_keys(emails)
            break
        except NoSuchElementException:
            email = driver.find_element_by_xpath('//*[@id=":pw"]')
            email.send_keys(emails)
        except NoSuchElementException:
            email = driver.find_element_by_xpath('//*[@id=":69"]')
            email.send_keys(emails)
        except NoSuchElementException:
            email = driver.find_element_by_xpath('//*[@id=":8s"]')
            email.send_keys(emails)
        contador = contador + 1
    sleep(2)
    contador = 0

    while contador < 3:
        try:
            assunt = driver.find_element_by_name("subjectbox")
            assunt.send_keys(assunto)
            break
        except NoSuchElementException:
            assunt = driver.find_element_by_xpath('//*[@id=":pe"]')
            assunt.send_keys(assunto)
        except NoSuchElementException:
            assunt = driver.find_element_by_xpath('//*[@id=":8c"]')
            assunt.send_keys(assunto)
        except NoSuchElementException:
            assunt = driver.find_element_by_xpath('//*[@id=":8x"]')
            assunt.send_keys(assunto)
        contador = contador + 1
    sleep(2)
    contador = 0

    while contador < 3:
        try:
            msg = driver.find_element_by_xpath('//*[@id=":a3"]')
            msg.send_keys(mensagem)
            break
        except NoSuchElementException:
            msg = driver.find_element_by_xpath('//*[@id=":9c"]')
            msg.send_keys(mensagem)
        except NoSuchElementException:
            msg = driver.find_element_by_xpath('//*[@id=":9h"]')
            msg.send_keys(mensagem)
        except NoSuchElementException:
            msg = driver.find_element_by_xpath('#//*[@id=":90"]')
            msg.send_keys(mensagem)
        contador = contador + 1
    sleep(2)
    contador = 0

    while contador < 3:
        try:
            enviar = driver.find_element_by_xpath('//*[@id=":8o"]')
            enviar.click()
            break
        except NoSuchElementException:
            enviar = driver.find_element_by_xpath('//*[@id=":7x"]')
            enviar.click()
        except NoSuchElementException:
            enviar = driver.find_element_by_xpath('//*[@id=":82"]')
            enviar.click()
        except NoSuchElementException:
            enviar = driver.find_element_by_xpath('//*[@id=":82"]')
            enviar.click()
        contador = contador + 1

    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div/div[1]/div[5]/div[1]/div/div[3]/div/div/div[2]'))
    )
    os.system('cls')
    print("Email enviado com sucesso!!!!!!")

def kill():
    print("Google Chrome finalizando... ")
    global driver
    driver.quit()
start()
