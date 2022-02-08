import requests

response = requests.get('https://www.google.com/')

print('Status code:',response.status_code)
print('Header:')
print(response.headers)
print('\nContent:', response.content)