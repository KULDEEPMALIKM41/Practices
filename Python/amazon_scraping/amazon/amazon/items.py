# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
     product_name = scrapy.Field()
     product_author = scrapy.Field()
     product_date = scrapy.Field()
     product_imagelinks = scrapy.Field()

