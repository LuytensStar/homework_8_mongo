from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://takixor119:z7ShIivdUIQH26kD@peoplecluster.ssjfkzz.mongodb.net/?retryWrites=true&w=majority&appName=PeopleCluster",
                     server_api = ServerApi('1')
         )

db = client.forpeople

result =db.author.find({})



for j in result:
    print(j)
db.author.delete_many({})
db.quote.delete_many({})
