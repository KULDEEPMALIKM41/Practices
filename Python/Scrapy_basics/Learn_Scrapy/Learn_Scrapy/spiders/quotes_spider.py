import scrapy
from scrapy.http import FormRequest
from ..items import LearnScrapyItem
from scrapy.utils.response import open_in_browser

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response, formdata={
            "csrf_token": token,
            "username": "kuldeep@123.com",
            "password": "123456789"
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
        items = LearnScrapyItem()
        all_div_quoutes = response.css("div.quote")
        # print(all_div_quoutes)
        for data in all_div_quoutes:
            quote = data.css(".text::text").extract()
            author = data.css(".author::text").extract()
            tag = data.css(".tag::text").extract()
            items['quote'] = quote
            items['author'] = author
            items['tag'] = tag
            yield items



