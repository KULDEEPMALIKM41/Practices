# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class AmazonPipeline(object):

    def __init__(self):
        self.create_connections()
        self.create_table()

    def create_connections(self):
        self.conn = sqlite3.connect('mybooks.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS books""")
        self.cursor.execute("""create table books(product_nm text,
                         author_nm text,
                         product_date text,
                         product_imagelink text
                         )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.cursor.execute("""INSERT INTO books VALUES(?,?,?,?)""",
                            (item['product_name'][0], item['product_author'][0], item['product_date'][0],item['product_imagelinks'][0]))
        self.conn.commit()