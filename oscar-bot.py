from config import select_from_file, select_from_list, api
import argparse

categories = ['p', 'c', 'f', 's']  # picture, cinematography, foreign and screenplay
category = select_from_list(categories)

if category == 'p':
    options = ('oscar-best-picture', 'Mejor Película')
elif category == 'c':
    options = ('oscar-best-cinematography', 'Mejor Fotografía')
elif category == 'f':
    options = ('oscar-best-foreign', 'Mejor Película Extranjera')
else:
    options = ('oscar-best-screenplay', 'Mejor Guión')

random_picture = select_from_file(options[0])
title = random_picture.split('(')[0].strip()
year = random_picture.split('(')[1][:-1]

tweet = 'La película elegida aleatoriamente del día es "%s", ganadora del premio Oscar a %s en el ' \
        'año %s. Visítanos en https://random.uchile.cl para más información sobre nuestro servicio.' % \
        (title, options[1], year)

parser = argparse.ArgumentParser(description='Twitter Bot - Academy Winners Movies')
parser.add_argument("-t", "--tweet", action="store_true", dest="tweet", default=False)
options = parser.parse_args()

if options.tweet:
    api.update_status(tweet)
else:
    print(tweet)
