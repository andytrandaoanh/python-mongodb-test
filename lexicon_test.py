
from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)

db = client.lexicon

names =  db.list_collection_names()


print(names)

examples = db.examples


pprint.pprint(examples.find_one())