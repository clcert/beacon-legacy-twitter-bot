from config import select_from_file, select_from_list

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

# api.update_status(tweet)
print(tweet)
