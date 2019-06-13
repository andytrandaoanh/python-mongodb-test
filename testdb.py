
from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)

db = client.test_database

names =  db.list_collection_names()


print(names)

posts = db.posts


pprint.pprint(posts.find_one())

