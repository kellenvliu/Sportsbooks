# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo

class MongodbPipeline(object):
    collection_name = "betus"

    def open_spider(self, spider):
        logging.debug("pipeline opened")
        self.client = pymongo.MongoClient("mongodb+srv://kellen:testtest@cluster0.yvmkr.mongodb.net/BetUS?retryWrites=true&w=majority")
        self.db = self.client["BetUS"]
        

    def close_spider(self, spider):
        logging.debug("pipeline closed")
        self.client.close()
    
    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)
        return item
