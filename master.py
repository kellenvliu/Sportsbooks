import pymongo
from pymongo import MongoClient
import pandas as pd
import os
import time

#time interval in seconds for each query
INTERVAL = 10


cluster = MongoClient("mongodb+srv://kellen:testtest@cluster0.yvmkr.mongodb.net/sportsbook?retryWrites=true&w=majority")
db = cluster['BetUS']
collection = db['betus']

results = collection.find()


def collector(database):
    os.system('cmd /c "scrapy crawl betus"')
    
    for result in database:
        print(result)

    collection.delete_many({})

while True:
    collector(results)
    time.sleep(INTERVAL)




