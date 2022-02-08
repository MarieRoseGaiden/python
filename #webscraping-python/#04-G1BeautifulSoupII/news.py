import requests
from bs4 import BeautifulSoup
import pandas as pd

newsList = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#HTML g1 news
findNews = site.findAll('div', attrs={'class': 'feed-post-body'})

for findNew in findNews:
    #title g1 news

    findTitle = findNew.find('a', attrs={'class': 'feed-post-link'})
    
    #print(findTitle.text)
    #print(findTitle['href'])

    #subtitle g1 news
    findSubtitle = findNew.find('div', attrs={'class', 'feed-post-body-resumo'})

    #metadata g1 news
    findMetadata = findNew.find('div', attrs={'class': 'feed-post-metadata'})
    
    if(findSubtitle):
        #print(findSubtitle.text)
        newsList.append([
            findTitle.text,
            findSubtitle.text,
            findTitle['href'],
            findMetadata.text      
        ])
    else:
        newsList.append([
            findTitle.text,
            '',
            findTitle['href'],
            findMetadata.text
        ])

saveNews = pd.DataFrame(newsList, columns=[
    'Title',
    'Subtitle',
    'link',
    'Date'
])

saveNews.to_csv('newsSavedScrapingG1.xlsx', index=False)

#print(saveNews)