from selenium import webdriver
from time import sleep

browser = webdriver.Edge(executable_path='C:\\WebDriver\\bin\\msedgedriver.exe')

url = 'https://www.walissonsilva.com/blog'
browser.get(url)
print(browser.title)
print(browser.current_url)

sleep(3)

elementRaw = browser.find_element_by_tag_name('input')
elementRaw.send_keys('data')


