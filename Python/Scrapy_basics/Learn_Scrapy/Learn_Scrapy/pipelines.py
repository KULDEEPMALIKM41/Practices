# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3
import json

class LearnScrapyPipeline(object):
    def __init__(self):
        self.create_connections()
        self.create_table()

    def create_connections(self):
        self.conn = sqlite3.connect('myquote.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS quotes""")
        self.cursor.execute("""create table quotes(quote text,
                         author text,
                         tag text
                         )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        tag = json.dumps(item['tag'])
        self.cursor.execute("""INSERT INTO quotes VALUES(?,?,?)""",
                            (item['quote'][0], item['author'][0], tag))
        self.conn.commit()

