print('product image:', imgFind['data-src'])
    print('product title:', titleFind.text)
    print('product link:', linkFind['href'])

    if(centsFind):
        print('product cost: R$', realFind.text+','+centsFind.text)
    else:
        print('product cost: R$', realFind.text)

    print('\n\n')