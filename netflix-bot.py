from config import select_from_file, api
import argparse

random_picture = select_from_file('netflix')

tweet = '¿No sabes que hacer esta noche? Te recomendamos la película "%s" disponible en Netflix. Una nueva ' \
        'recomendación todas las semanas. Visítanos en https://random.uchile.cl para más información sobre nuestro ' \
        'servicio.' % random_picture

parser = argparse.ArgumentParser(description='Twitter Bot - Best Netflix Movies')
parser.add_argument("-t", "--tweet", action="store_true", dest="tweet", default=False)
options = parser.parse_args()

if options.tweet:
    api.update_status(tweet)
else:
    print(tweet)
