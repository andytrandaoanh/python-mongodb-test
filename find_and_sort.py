import datetime
import pprint
from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.test_database

posts = db.posts

#listing all documents
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
	pprint.pprint(post)
