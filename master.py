import pymongo
from pymongo import MongoClient
import pandas as pd
import os
import time

#time interval in seconds for each query
INTERVAL = 20

#db info
cluster = MongoClient("mongodb+srv://kellen:testtest@cluster0.yvmkr.mongodb.net/sportsbook?retryWrites=true&w=majority")
db = cluster['BetUS']
collection = db['betus']

def collector(database): #clear, run, and tabulate collection
    collection.delete_many({})
    os.system('cmd /c "scrapy crawl betus --nolog"')
    results = database.find()
    print(analyze(results))



def analyze(matches):
    currentmatches = [{
        't1':'',
        't2':'',
        'line1':'',
        'site1':'',
        'line2':'',
        'site2':''
        }]
        
    for match in matches:
        if match['t1'] > match['t2']:
            match['t1'], match['t2'], match['line1'], match['line2'] = match['t2'], match['t1'], match['line2'], match['line1']
        added = False
        for idx, currentmatch in enumerate(currentmatches):
            if currentmatch['t1'].lower() == match['t1'].lower(): #This is iffy since different sites have different spellings
                print("got here")
                if match['line1'] > currentmatch['line1']:
                    currentmatches[idx]['line1'],currentmatches[idx]['site1'] = match['line1'],match['sitename']
                if match['line2'] > currentmatch['line2']:
                    currentmatches[idx]['line2'],currentmatches[idx]['site2'] = match['line2'],match['sitename']
                added = True
                break
        if added == False:
            print("also got here")
            currentmatches.append({
                't1':match['t1'],
                't2':match['t2'],
                'line1':match['line1'],
                'site1':match['sitename'],
                'line2':match['line2'],
                'site2':match['sitename']
                    })

    print(currentmatches)
    return currentmatches
       


while True:
    collector(collection)
    time.sleep(INTERVAL)




