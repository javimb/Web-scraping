# -*- encoding: utf-8 -*-
import requests

from bs4 import BeautifulSoup
from celery.task import task

from .models import Film
from .utils import get_object_or_none


@task
def sexta3_scraper():
    url = 'http://www.lasexta.com/programacion/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    sexta3 = soup.find_all(class_='parrilla')[2]
    hoy = sexta3.find_all(class_='programacion')[0]
    fichas = hoy.find_all(class_='ficha')

    for ficha in fichas:
        title = ficha.contents[3].get('title').strip()
        hour = ficha.contents[1].text.strip()
        _sexta3_create_film.delay(title, hour)


@task
def _sexta3_create_film(title, hour):
    if title == "TODO CINE":
        return
    if title == "COMPRAS DE CINE":
        return
    if "TELETIENDA" in title:
        return
    if title[0:5] == "CINE ":
        title = title[5:]

    film = get_object_or_none(Film.objects.get_today_films(),
        title=title, channel="Sexta 3")
    if not film:
        film = Film()
        film.title = title
        film.hour = hour
        film.channel = "Sexta 3"
        film.rating, film.url = imbd_scraper(film.title)
        film.save()


@task
def sexta_scraper():
    url = 'http://www.lasexta.com/programacion/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    sexta = soup.find_all(class_='parrilla')[0]
    hoy = sexta.find_all(class_='programacion')[0]
    fichas = hoy.find_all(class_='ficha')

    for ficha in fichas:
        title = ficha.contents[3].get('title').strip()
        hour = ficha.contents[1].text.strip()
        _sexta_create_film.delay(title, hour)


@task
def _sexta_create_film(title, hour):
    if title[0:6] == "CINE: ":
        title = title[6:]
        if title[-10:] == " (ESTRENO)":
            title = title[0:-10]

        film = get_object_or_none(Film.objects.get_today_films(),
            title=title, channel="Sexta")
        if not film:
            film = Film()
            film.title = title
            film.hour = hour
            film.channel = "Sexta"
            film.rating, film.url = imbd_scraper(film.title)
            film.save()


@task
def nova_scraper():
    url = 'http://www.antena3.com/programacion/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    nova = soup.find_all(class_='parrilla')[2]
    hoy = nova.find_all(class_='programacion')[0]
    fichas = hoy.find_all(class_='ficha')

    for ficha in fichas:
        title = ficha.contents[3].get('title').strip()
        hour = ficha.contents[1].text.strip()
        _nova_create_film.delay(title, hour)


@task
def _nova_create_film(title, hour):
    if title[0:6] == "CINE: ":
        title = title[6:]
    elif title[0:5] == "CINE ":
        title = title[5:]
    else:
        return

    film = get_object_or_none(Film.objects.get_today_films(),
        title=title, channel="Nova")
    if not film:
        film = Film()
        film.title = title
        film.hour = hour
        film.channel = "Nova"
        film.rating, film.url = imbd_scraper(film.title)
        film.save()


@task
def nitro_scraper():
    url = 'http://www.antena3.com/programacion/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    nitro = soup.find_all(class_='parrilla')[3]
    hoy = nitro.find_all(class_='programacion')[0]
    fichas = hoy.find_all(class_='ficha')

    for ficha in fichas:
        title = ficha.contents[3].get('title').strip()
        hour = ficha.contents[1].text.strip()
        _nitro_create_film.delay(title, hour)


@task
def _nitro_create_film(title, hour):
    if title[0:6] == "CINE: ":
        title = title[6:]
    elif title[0:5] == "CINE ":
        title = title[5:]
    else:
        return

    film = get_object_or_none(Film.objects.get_today_films(),
        title=title, channel="Nitro")
    if not film:
        film = Film()
        film.title = title
        film.hour = hour
        film.channel = "Nitro"
        film.rating, film.url = imbd_scraper(film.title)
        film.save()


@task
def neox_scraper():
    url = 'http://www.antena3.com/programacion/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    neox = soup.find_all(class_='parrilla')[1]
    hoy = neox.find_all(class_='programacion')[0]
    fichas = hoy.find_all(class_='ficha')

    for ficha in fichas:
        title = ficha.contents[3].get('title').strip()
        hour = ficha.contents[1].text.strip()
        _neox_create_film.delay(title, hour)


@task
def _neox_create_film(title, hour):
    if title[0:6] == "CINE: ":
        title = title[6:]
    elif title[0:5] == "CINE ":
        title = title[5:]
    else:
        return

    film = get_object_or_none(Film.objects.get_today_films(),
        title=title, channel="Neox")
    if not film:
        film = Film()
        film.title = title
        film.hour = hour
        film.channel = "Neox"
        film.rating, film.url = imbd_scraper(film.title)
        film.save()


@task
def antena3_scraper():
    url = 'http://www.antena3.com/programacion/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    antena3 = soup.find_all(class_='parrilla')[0]
    hoy = antena3.find_all(class_='programacion')[0]
    fichas = hoy.find_all(class_='ficha')

    for ficha in fichas:
        title = ficha.contents[3].get('title').strip()
        hour = ficha.contents[1].text.strip()
        _antena3_create_film.delay(title, hour)


@task
def _antena3_create_film(title, hour):
    if title[0:6] == "CINE: ":
        title = title[6:]
    elif title[0:5] == "CINE ":
        title = title[5:]
    elif title[0:11] == "MULTICINE: ":
        title = title[11:]
    elif title[0:14] == "EL PELICULÓN: ".decode('utf-8'):
        title = title[14:]
    else:
        return

    if title[-10:] == " (ESTRENO)":
        title = title[0:-10]

    film = get_object_or_none(Film.objects.get_today_films(),
        title=title, channel="Antena 3")
    if not film:
        film = Film()
        film.title = title
        film.hour = hour
        film.channel = "Antena 3"
        film.rating, film.url = imbd_scraper(film.title)
        film.save()


def imbd_scraper(film):
    url = "http://www.imdb.com%s" % _get_imdb_url(film)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    try:
        rating = soup.find(class_='star-box-giga-star').text
    except:
        rating = "Any"

    return (rating, url)


def _get_imdb_url(film):
    url = 'http://www.imdb.com/find?q=%s' % film.replace(' ', '+')
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    return soup.find_all(class_='result_text')[0].contents[1].get('href')
