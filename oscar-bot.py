from config import select_choice

random_picture = select_choice('oscar')
title = random_picture.split('(')[0].strip()
year = random_picture.split('(')[1][:-1]

tweet = 'La película elegida aleatoriamente del día es "%s", ganadora del premio Oscar a la mejor película en el ' \
        'año %s. Visítanos en https://random.uchile.cl para más información sobre nuestro servicio.' % (title, year)

# api.update_status(tweet)
print(tweet)
