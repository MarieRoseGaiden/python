import os
from gtts.tts import gTTS
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import random
from io import BytesIO
from pywhatkit import pywhatkit

love_phrases = [
    'Sabe quando você quer que um momento dure para sempre? Então, é assim quando estou com você.',
    'Você é o maior presente que Deus poderia me dar. Te amo hoje e sempre!',
    'Eu te amo. E nunca me imaginária amando alguém com tanta intensidade, nem sabia que tinha tanta capacidade para amar assim.',
    'Minha felicidade não tem preço, tem o seu nome.',
    'Não dá pra negar, é você, tem sido você e vai continuar sendo você... Minha escolha, minha certeza, meu amor.',
    'Amo seu jeito, seu riso, seu tudo e até as imperfeições eu amo em você!',
    'Um dia me perguntaram "O que você viu nela?" e eu respondi "O que faltava em mim!"',
    'Te amo. Com todas as letras, palavras e pronúncias. Em todas as línguas e sotaques. Em todos os sentidos e jeitos. Simplesmente, te amo.',
    'Eu não preciso de mil motivos para sorrir, você já é o suficiente.',
    'Meu amor, você é o que tenho de mais especial e nem consigo imaginar minha vida sem ser ao seu lado.',
    'O mundo é uma verdadeira imensidão e nunca consegui achar alguém tão especial como você!',
    'O tempo passa e o meu amor por você só aumenta a cada dia.',
    'O tempo passa e o meu amor por você só aumenta a cada dia.',
    'Para nós, todo o amor do mundo.',
    'Eu nunca me cansarei de dizer que é você quem eu amo, e é ao seu lado que eu quero acordar todos os dias.',
    'Todos vivem por uma razão, a minha é você.',
    'De qualquer jeito seu sorriso vai ser meu raio de sol.',
    'Você é realmente a razão da minha vida.',
    'Por sua causa, eu tenho lindos sonhos para sonhar. Por sua causa, minha vida está cheia de amor.',
    'Com você, o meu mundo é melhor.',
    'Naquele dia que você me olhou. Me balançou por dentro, me virou o mundo! Percebi, tinha que ser você.',
    'Não é exagero dizer que você me roubou no momento em que me olhou.',
    'E se eu puder fazer por ti o que ninguém jamais fez por mim, eu faço!',
    'Você chegou do nada para ser meu tudo.',
    'Sem você, eu posso tudo, menor ser feliz.',
    'Eu preciso dizer que eu te amo, te ganhar ou perder sem engano.',
    'Eu quero colo, eu quero carinho. E meu carinho eu quero te dar!'
]

instagram_username = input('Instagram username: ')
instagram_password = input('Instagram password: ')
whatsapp_number = input('whatsapp: ')

def text_to_speech(text):
    print('Enviando mensagem...')
    tts = gTTS(text, lang='en')
    tts.save('speech.mp3')
    os.system('speech.mp3')
def log_in_skip():
    log_in = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

    log_in.click()

    not_now1 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))

    not_now1.click()

    not_now2 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))

    not_now2.click()
def verify_followers():
    stop = 0
    last_followers_count = 0
    while stop == 0:
        browser.get('https://www.instagram.com/'+instagram_username)
        followers_element = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/ul/li[2]/a/span')))
        followers_count = int(followers_element.text)
        if(followers_count > last_followers_count):
            text_to_speech("new follow! I'll send message.")
            pywhatkit.sendwhatmsg_instantly(whatsapp_number, str(random.choice(love_phrases)), 30, False)
            last_followers_count = followers_count
        sleep(5)                                

options = Options()
options.add_argument('window-size=375,812')

browser = webdriver.Chrome(executable_path=r'C:\WebDriver\bin\chromedriver',options=options)

browser.get('https://instagram.com')

username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username'")))
password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password'")))

username.send_keys(instagram_username)
password.send_keys(instagram_password)

log_in_skip()
verify_followers()



