import requests
from bs4 import BeautifulSoup


def get_today_films():
    url = 'http://www.lasexta.com/programacion/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    sexta3 = soup.find_all(class_='parrilla')[2]
    hoy = sexta3.find_all(class_='programacion')[0]
    fichas = hoy.find_all(class_='ficha')

    return [[ficha.contents[1].text, ficha.contents[3].get('title')] for ficha in fichas]