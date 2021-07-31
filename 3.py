import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

db_client = MongoClient()
my_db = db_client.cursos
my_posts = my_db.posts

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)


def find_1st(string, substring):
    return string.find(substring, string.find(substring))


response = requests.get("https://www.elcomercio.com/deportes/otros/anicka-delgado-cronometro-50metros-libre-juegos-olimpicos-tokio.html")
soup = BeautifulSoup(response.content)

Contenidos = []
Provider = []
Duration = []
Start_Date = []
Offered_By = []
No_Of_Reviews = []
Rating = []
ListSearch = []

titulos = soup.find_all("h3", class_="css-xxaj7r e1lsht870")
contenido = soup.find_all("p", class_="css-oemrl2")

'''post_course=soup.find_all("span", class_="text-1 weight-semi line-tight")
post_provider=soup.find_all("a", class_="color-charcoal italic")'''

extracted = []
for element in contenido:
    # print(element)
    element = str(element)
    limpio = str(element[find_1st(element, '>') + 1:find_2nd(element, '<')])
    ListSearch.append({"Content": limpio.strip()})
CLIENT = MongoClient("mongodb://localhost:27017/")

try:
        CLIENT.admin.command('ismaster')
        print('MongoDB connection: Success')
except ConnectionFailure as cf:
        print('MongoDB connection: failed', cf)
db = CLIENT["exam"]
game = db["juegos_olimpicos"]

x = game.insert_many(ListSearch)