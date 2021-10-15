import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
#options.add_argument('--headless')
options.add_argument('window-size=375,812')

driver = webdriver.Chrome(executable_path="C:\\WebDriver\\bin\\chromedriver",options=options)

driver.get('https://www.airbnb.com/')

sleep(2)

button_place1 = driver.find_element_by_tag_name('button')
button_place1.click()

sleep(1)

input_place = driver.find_element_by_id('GP-Explore-Autocomplete-Koan-input')
input_place.send_keys('Montes Claros - MG')
input_place.submit()

sleep(2)

button_place2 = driver.find_element_by_css_selector('button > img')
button_place2.click()

sleep(1)

button_place3 = driver.find_element_by_class_name('_12fun97')
button_place3.click()
button_place4 = driver.find_element_by_class_name('_f8btejl')
button_place4.click()

sleep(1)

button_place5 = driver.find_element_by_class_name('_3t1kklr')
button_place5.click()

sleep(1)

button_place6 = driver.find_element_by_class_name('_rcyqgr0')
button_place6.click()

sleep(4)

source = driver.page_source

site_soup = BeautifulSoup(source, 'html.parser')

print(site_soup.prettify())



