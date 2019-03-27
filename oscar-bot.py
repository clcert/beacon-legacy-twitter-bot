from config import select_from_file, select_from_list, api, omdb_api_key
import argparse
import requests

categories = ['p', 'f', 's']  # picture, foreign and screenplay
category = select_from_list(categories)

if category == 'p':
    options = ('oscar-best-picture', 'Mejor Película')
elif category == 'f':
    options = ('oscar-best-foreign', 'Mejor Película Extranjera')
else:
    options = ('oscar-best-screenplay', 'Mejor Guión')

random_picture = select_from_file(options[0])
title = random_picture.split('(')[0].strip()
year = random_picture.split('(')[1][:-1]

hashtags = "#academyawards #oscars #movies"

# get poster
omdb_api_endpoint = "https://www.omdbapi.com/?t=%s&apikey=%s" % (title, omdb_api_key)
try:
    poster_url = requests.get(omdb_api_endpoint).json()['Poster']
    poster_response = requests.get(poster_url)
    with open('poster.jpg', 'bw') as poster_file:
        poster_file.write(poster_response.content)
        poster_file.close()
    no_poster = False
except KeyError:
    no_poster = True

tweet = 'La película elegida aleatoriamente del día es "%s", ganadora del premio Oscar a %s en el ' \
        'año %s. Visítanos en https://random.uchile.cl/apps/movie-bot para más información sobre nuestro servicio. ' % \
        (title, options[1], year) + hashtags

parser = argparse.ArgumentParser(description='Twitter Bot - Academy Winners Movies')
parser.add_argument("-t", "--tweet", action="store_true", dest="tweet", default=False)
options = parser.parse_args()

if options.tweet:
    if no_poster:
        api.update_status(tweet)
    else:
        api.update_with_media(filename='poster.jpg', status=tweet)
else:
    print(tweet)
