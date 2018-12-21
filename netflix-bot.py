from config import select_choice

random_picture = select_choice('netflix')

tweet = '¿No sabes que hacer? Te recomendamos la película "%s" disponible en Netflix. Una nueva película todos los ' \
        'días. Visítanos en https://random.uchile.cl para más información sobre nuestro servicio.' % random_picture

# api.update_status(tweet)
print(tweet)
