from config import sarpurURLS
from requests import get
import json


class Image:
    def __init__(self, url, title, filename):
        self.url = url
        self.title = title
        self.filename = filename


class Role:
    def __init__(self, role, name):
        self.role = role
        self.name = name


class Movie:
    "A single movie from Sarpur"

    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]["rendered"]
        self.content = data["content"]["rendered"]
        if data["acf"]["mynd_stilla"]:
            self.image = Image(
                data["acf"]["mynd_stilla"]["url"],
                data["acf"]["mynd_stilla"]["title"],
                data["acf"]["mynd_stilla"]["filename"],
            )
        else:
            self.image = Image("", "", "")
        self.trailerURL = data["acf"]["mynd_trailer"]
        self.playtime = data["acf"]["mynd_lengd"]
        self.director = data["acf"]["mynd_leikstjori"]
        self.producer = data["acf"]["mynd_framleidandi"]
        self.otherCredits = []
        if data["acf"]["mynd_adrir"]:
            for item in data["acf"]["mynd_adrir"]:
                self.otherCredits.append(
                    Role(item["mynd_adrir_hlutverk"], item["mynd_adrir_nafn"])
                )

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def fetch_movies_by_year(year):
    response = get(sarpurURLS[year])
    movies = []

    for data in response.json():
        sarpurItem = Movie(data)
        movies.append(sarpurItem)
    return movies
