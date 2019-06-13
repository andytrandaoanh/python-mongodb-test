import datetime
import pprint
from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.test_database

posts = db.posts

new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]


result = posts.insert_many(new_posts)


print(result.inserted_ids)

