#obtendo produtos do mercado livre a partir de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup
import pandas as pd

productsList = []

urlBase = 'https://lista.mercadolivre.com.br/'

productName = input('qual produto você deseja? ')
productName = productName.replace(" ", "-")

response = requests.get(urlBase + productName)

site = BeautifulSoup(response.text, 'html.parser')

productsFind = site.findAll('div', attrs={
    'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'
})

# print(site.find('div', attrs={
#     'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'
# }).prettify())

for productFind in productsFind:
    imgFind = productFind.find('img', attrs={
        'class': 'ui-search-result-image__element'
    })
    titleFind = productFind.find('h2', attrs={
        'class': 'ui-search-item__title'
    })
    linkFind = productFind.find('a', attrs={
        'class': 'ui-search-link'
    })
    realFind = productFind.find('span', attrs={
        'class': 'price-tag-fraction'
    })
    centsFind = productFind.find('span', attrs={
        'class': 'price-tag-cents'
    })
  
    # print('product image:', imgFind['data-src'])
    # print('product title:', titleFind.text)
    # print('product link:', linkFind['href'])

    # if(centsFind):
    #     print('product cost: R$', realFind.text+','+centsFind.text)
    # else:
    #     print('product cost: R$', realFind.text)

    # print('\n\n')

    if(centsFind):
        productsList.append([
            titleFind.text,
            'R$ '+realFind.text+','+centsFind.text,
            imgFind['data-src'],
            linkFind['href']
        ])
    else:
        productsList.append([
            titleFind.text,
            'R$ '+realFind.text,
            imgFind['data-src'],
            linkFind['href']
        ])
    
productsSave = pd.DataFrame(productsList, columns=[
    'title',
    'cost',
    'image',
    'link'
])

productsSave.to_csv('productsSavedScrapingMercadoLivre.xlsx', index=False)

# print(productsSave)

