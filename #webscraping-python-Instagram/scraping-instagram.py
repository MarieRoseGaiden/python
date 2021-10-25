from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import os
import wget

login_username = input('Instagram username: ')
login_password = input('Instagram password: ')

browser = webdriver.Chrome(executable_path=r'C:\WebDriver\bin\chromedriver')#webdriver path

browser.get('https://instagram.com')

sleep(4)

username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.send_keys(login_username)
password.send_keys(login_password)

submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

submit.click()

not_now1 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))

not_now1.click()

not_now2 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))

not_now2.click()

search = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Pesquisar"]')))

keyword = input("what you'd like to search?")

search.send_keys(keyword)

element = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[5]/a')))

element.click()

sleep(4)

browser.execute_script('window-scrollTo(0, document.body.scrollHeight);')

images = browser.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path, keyword)
os.mkdir(path)

counter = 0

for image in images:
    save_as = os.path.join(path, keyword+str(counter)+'.jpg')
    wget.download(image, save_as)
    counter+=1