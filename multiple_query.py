import datetime
import pprint
from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.test_database

posts = db.posts

#listing all documents
for post in posts.find({"author": "Mike"}):
	 pprint.pprint(post)



#listing some docs

