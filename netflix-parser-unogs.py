import requests
import json

url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

cnt = 1
movies_titles = []

while True:
    querystring = {"q": "-!1900,2019-!0,5-!8,10-!0-!Movie-!Any-!Any-!gt1000-!Any", "t": "ns", "cl": "21",
                   "st": "adv", "ob": "Relevance", "p": "%d" % cnt, "sa": "and"}

    headers = {
        'x-rapidapi-key': "97a6cd8581msheed10f826abaf6dp1074f9jsn74a9c07241f0"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    count = json.loads(response.content)["COUNT"]
    movies = json.loads(response.content)["ITEMS"]

    for movie in movies:
        movies_titles.append(movie["title"].replace("&#39;", "'"))

    if len(movies_titles) >= int(count):
        break

    cnt += 1

for movie_title in movies_titles:
    print(movie_title)
