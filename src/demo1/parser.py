from scrapper_sexta3 import get_today_films
from scrapper_imdb import get_film_info


def get_films():
    films = []
    for film in get_today_films():
        title = film[1]
        if title == "TODO CINE" or title == "COMPRAS DE CINE":
            continue
        if "TELETIENDA" in title:
            continue
        if title[0:5] == "CINE ":
            title = title[5:]
            film[1] = title
        film_info = get_film_info(title.title())
        films.append(map(lambda s: s.strip(), film + film_info))
    return films
