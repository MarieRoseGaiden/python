import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#HTML g1 news
findNews = site.find('div', attrs={'class': 'feed-post-body'})

#title g1 news
print(findNews.find('a', attrs={'class': 'feed-post-link'}).text)

#subtitle g1 news
print(findNews.find('div', attrs={'class': 'feed-post-metadata'}).text)
