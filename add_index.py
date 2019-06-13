import datetime
import pprint
import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.test_database

posts = db.posts



result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
                                  unique=True)


sorted_data = sorted(list(db.profiles.index_information()))

print(sorted_data)