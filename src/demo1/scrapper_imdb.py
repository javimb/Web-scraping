import requests
from bs4 import BeautifulSoup


def get_film_info(film):
    url = "http://www.imdb.com%s" % _get_film_url(film)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    try:
        rating = soup.find(class_='star-box-giga-star').text
    except:
        rating = "Any"

    return [rating, url]


def _get_film_url(film):
    url = 'http://www.imdb.com/find?q=%s' % film.replace(' ', '+')
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    return soup.find_all(class_='result_text')[0].contents[1].get('href')
