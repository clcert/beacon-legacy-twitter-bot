from config import select_from_file, api
import argparse

random_picture = select_from_file('cannes-palme-dor')
title = random_picture.split('(')[0].strip()
year = random_picture.split('(')[1][:-1]

tweet = '¿Quieres algo diferente para ver esta noche? Te recomendamos la película "%s", ' \
        'ganadora del máximo premio del Festival de Cannes del año %s. Visítanos en ' \
        'https://random.uchile.cl para más información sobre nuestro servicio.' % (title, year)

parser = argparse.ArgumentParser(description='Twitter Bot - Cannes Winners Movies')
parser.add_argument("-t", "--tweet", action="store_true", dest="tweet", default=False)
options = parser.parse_args()

if options.tweet:
    api.update_status(tweet)
else:
    print(tweet)
