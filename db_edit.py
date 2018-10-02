from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb://<admin>:<codethechange1>@ds119343.mlab.com:19343/c4e21-group1"

client = MongoClient(uri)
db = client.get_default_database()

quote = db["quote"]

cond = {
    "topic": "power"
}

quote.delete_many(cond)