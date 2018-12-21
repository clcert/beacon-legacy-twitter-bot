from bs4 import BeautifulSoup
import requests


films = []
base_url = "https://www.revistaprivilege.net/peliculas-recomendadas-en-netflix/"

for i in range(1,15):

    if i >= 2:
        url = base_url + str(i)
    else:
        url = base_url

    req = requests.get(url)
    web = req.content
    soup = BeautifulSoup(web, "html.parser")

    for film in soup.find_all("h3"):
        with open('lists/netflix', 'a') as f:
            f.write(str(film.string) + '\n')
