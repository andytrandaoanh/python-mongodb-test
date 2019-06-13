import datetime
from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)


DB_NAME = 'lexicon'
COLLECTION_NAME = 'examples'

db = client[DB_NAME]
coll = db[COLLECTION_NAME]





