from config import select_from_file, select_from_list, api
import argparse

festivals = ['c', 's']
festival = select_from_list(festivals)

if festival == 'c':
    options = ('cannes-palme-dor', 'del Festival de Cannes', '#cannes')
else:
    options = ('spirit', 'de los Independent Spirit', '#spiritawards')

random_picture = select_from_file(options[0])
title = random_picture.split('(')[0].strip()
year = random_picture.split('(')[1][:-1]

hashtags = options[2] + " #movies"
tweet = '¿Quieres algo diferente para ver esta noche? Te recomendamos la película "%s", ' \
        'ganadora del máximo premio %s del año %s. Visítanos en ' \
        'https://random.uchile.cl para más información sobre nuestro servicio. ' % (title, options[1], year) + hashtags

parser = argparse.ArgumentParser(description='Twitter Bot - Alternative Awards Movies')
parser.add_argument("-t", "--tweet", action="store_true", dest="tweet", default=False)
options = parser.parse_args()

if options.tweet:
    api.update_status(tweet)
else:
    print(tweet)
    print(str(len(tweet)))
