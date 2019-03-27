from config import select_from_file, api, omdb_api_key
import argparse
import requests

random_picture = select_from_file('netflix')

hashtags = "#netflix #movies"

# get poster
omdb_api_endpoint = "https://www.omdbapi.com/?t=%s&apikey=%s" % (random_picture, omdb_api_key)
try:
    poster_url = requests.get(omdb_api_endpoint).json()['Poster']
    poster_response = requests.get(poster_url)
    with open('poster.jpg', 'bw') as poster_file:
        poster_file.write(poster_response.content)
        poster_file.close()
    no_poster = False
except KeyError:
    no_poster = True

tweet = '¿No sabes que hacer esta noche? Te recomendamos la película "%s" disponible en Netflix. Una nueva ' \
        'recomendación todas las semanas. Visítanos en https://random.uchile.cl/apps/movie-bot para más información ' \
        'sobre nuestro servicio. ' % random_picture + hashtags

parser = argparse.ArgumentParser(description='Twitter Bot - Best Netflix Movies')
parser.add_argument("-t", "--tweet", action="store_true", dest="tweet", default=False)
options = parser.parse_args()

if options.tweet:
    if no_poster:
        api.update_status(tweet)
    else:
        api.update_with_media(filename='poster.jpg', status=tweet)
else:
    print(tweet)
