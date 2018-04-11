import get_auth
import tweepy as tp
import json
import ast
from pymongo import MongoClient

client = MongoClient()
db = client.get_database('dttweets')
collection = db.get_collection('tweets')

auth = get_auth.get_auth()
api = tp.API(auth)
# api = tp.API(auth, proxy='http://127.0.0.1:38251')
print("|username:", api.me().name, "|")

max_id = 983427438691708929
tweetslen = 1

while True:
    dttweets = api.user_timeline(
        id="realDonaldTrump", max_id=max_id, count=201)
    tweetslen = len(dttweets)
    print("--dttweets current len:", tweetslen)

    if tweetslen > 0:
        max_id = dttweets[-1]._json['id']
        print("-max_id:", max_id)

    for tweet in dttweets:
        collection.insert_one(tweet._json)
    print("----MongoDB current len:", collection.count())
    
