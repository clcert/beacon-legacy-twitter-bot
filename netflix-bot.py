from config import select_from_file

random_picture = select_from_file('netflix')

tweet = '¿No sabes que hacer esta noche? Te recomendamos la película "%s" disponible en Netflix. Una nueva ' \
        'recomendación todas las semanas. Visítanos en https://random.uchile.cl para más información sobre nuestro ' \
        'servicio.' % random_picture

# api.update_status(tweet)
print(tweet)
