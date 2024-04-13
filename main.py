import json
from bson.objectid import ObjectId

from models import Author, Quote
import connect

with open('authors.json', 'r', encoding='utf-8') as f:
    authors_data = json.load(f)

with open('quotes.json', 'r', encoding='utf-8') as g:
    quotes_data = json.load(g)

authors = {}

for author in authors_data:
    b = Author(fullname = author['fullname'], born_date = author['born_date'], born_location = author['born_location'], description=author['description'] )
    b.save()
for quote in quotes_data:
    print(type(quote['tags']))
    author_id = Author.objects(fullname=quote['author']).first().id
    b = Quote(tags= quote['tags'],   author =author_id , quote=quote['quote']) # zminyw tut
    b.save()

