# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem

class AmazonspdrSpider(scrapy.Spider):
    page = 2
    name = 'amazonspdr'
    start_urls = ['https://www.amazon.com/s?k=last+30+days&i=stripbooks-intl-ship&page=1&crid=17B96T5R3ZVQG&qid=1559563195&sprefix=last+30%2Cstripbooks-intl-ship%2C424&ref=sr_pg_2']
    def parse(self, response):
        items = AmazonItem()

        all_div = response.css(".s-include-content-margin")

        for data in all_div:
            product_name = data.css(".a-color-base.a-text-normal").css("::text").extract()
            product_author = data.css(".a-color-secondary .a-size-base+ .a-size-base").css("::text").extract()
            product_date = data.css(".a-color-secondary.a-text-normal").css("::text").extract()
            product_imagelinks = data.css(".s-image::attr(src)").extract()

            product_author[0] = product_author[0].replace(" \n", "").replace(" ", "").replace("\n", "")

            items["product_name"]=product_name
            items["product_author"]=product_author
            items["product_date"]=product_date
            items["product_imagelinks"]=product_imagelinks
            yield items

        next_page = "https://www.amazon.com/s?k=last+30+days&i=stripbooks-intl-ship&page="+str(self.page)+"&crid=17B96T5R3ZVQG&qid=1559563195&sprefix=last+30%2Cstripbooks-intl-ship%2C424&ref=sr_pg_2"

        if self.page <= 4:
            self.page += 1
            yield response.follow(next_page, callback=self.parse)