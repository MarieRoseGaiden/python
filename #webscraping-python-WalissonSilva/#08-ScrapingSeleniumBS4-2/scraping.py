import requests
import pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

hosts_data = []

options = Options()
#options.add_argument('--headless')
options.add_argument('window-size=375,812')

driver = webdriver.Chrome(executable_path="C:\\WebDriver\\bin\\chromedriver",options=options)

url = 'https://airbnb.com.br'
driver.get(url)

sleep(2)

button_place1 = driver.find_element_by_tag_name('button')
button_place1.click()

sleep(1)

op_local = input('qual a cidade: ')
input_place = driver.find_element_by_id('GP-Explore-Autocomplete-Koan-input')
input_place.send_keys(op_local)
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

page_content = driver.page_source

site_soup = BeautifulSoup(page_content, 'html.parser')

hosts = site_soup.findAll('div', attrs={
    'class': '_1ify1icq'
})

# print(hosts.prettify())

for host in hosts:
    host_image = host.find('div', attrs={
        'class': '_1yfus1e'
    })
    host_descriptions = host.find('div', attrs={
        'class': '_5kaapu'
    })
    host_location = host.find('div', attrs={
        'style': 'margin-bottom: 2px;'
    })
    host_cost = host.find('span', attrs={
        'class': 'a8jt5op dir dir-ltr'
    })
    host_url = host.find('a', attrs={
        'class': '_1jhvjuo'
    })
    # print('\nimage - '+host_image['data-key'])
    # print('descriptions - '+host_descriptions.text)
    # print('location - '+host_location.text)
    # print('cost - '+host_cost.text)
    # print('url - '+url+host_url['href'])
    # print()

    hosts_data.append([
        host_image['data-key'],
        host_descriptions.text,
        host_location.text,
        host_cost.text,
        url+host_url['href']
    ])

hosts_save = pandas.DataFrame(hosts_data, columns=[
    'image',
    'description',
    'location',
    'cost',
    'url'
])

hosts_save.to_csv(
    '#08-ScrapingSeleniumBS4-2/hosts_'+op_local+'_scraping_airbnb.xlsx', 
    index=False
)



