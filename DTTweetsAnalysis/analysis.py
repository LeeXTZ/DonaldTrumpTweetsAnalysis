import pymongo

client = pymongo.MongoClient()
db = client['dttweets']
collection = db['tweets']

t = collection.find_one()
print(type(t))
print(len(t))
print(t)