import json

from scrapper_sexta3 import get_today_films
from scrapper_imdb import get_film_info


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
    film_info = get_film_info(title)
    films.append(map(lambda s: s.strip(), film + film_info))

data = {'films': []}

for film in films:
    film_data = {'title': film[1].title(),
                 'hour': film[0],
                 'rating': film[2],
                 'url': film[3][:-16]}
    data['films'].append(film_data)

json_file = open('films.json', 'w')
json_file.write(json.dumps(data, indent=4))
