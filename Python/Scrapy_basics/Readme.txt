1. open "project folder" with PyCharm
2. pip install scrapy
3. run commamd in pycharm terminal => "scrapy startproject <project_name>"
4. cd one directry
5. create spider : scrapy genspider <spider nm> <url>
6. for run project : scrapy crawl <Scrapy name>
7. for window shell : scrapy shell <url_for_scraping>
8. methods : # title =response.css('title::text').extract()
        # yield {'titletext' : title}
        # title =response.css('title::text').extract_first()
        # print(title)
        # title =response.css('title::text')[0].extract()
        # print(title)
        # quotes =response.css('span.text::text').extract()
        # print(quotes)
        # quotes =response.css('span.text::text').extract_first()
        # print(quotes)
        # author =response.css('.author::text').extract_first()
        # print(author)
        # author =response.css('.author::text').extract()
        # print(author)
        # title =response.xpath('//title/text()').extract()
        # print(title)
        # quotes =response.xpath("//span[@class='text']/text()").extract()
        # print(quotes)
        # author = response.xpath("//small[@class='author']/text()").extract()
        # print(author)
        # link = response.css("li.next a").xpath("@href").extract()
        # print(link)
        # link = response.css("a").xpath("@href").extract()
        # print(link)
        # link = response.css("li.next a::attr(href)").extract()
        # print(link)
        # link = response.css("li.next a::attr(href)").get()
        # print(link)

#backup 1

import scrapy
from ..items import LearnScrapyItem
from scrapy.cmdline import execute


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls =[ 'http://quotes.toscrape.com/' ]
    def parse(self, response):
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
        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            print(next_page)
            res=response.follow(next_page, callback = self.parse)
            print("tttttttttttttttttttttttttttttttttttttttttttttttttttt",res)
            yield res


#Backup 2

import scrapy
from ..items import LearnScrapyItem
from scrapy.cmdline import execute


class QuotesSpider(scrapy.Spider):
    page=2
    name = 'quotes'
    start_urls =[ 'http://quotes.toscrape.com/page/1/' ]
    def parse(self, response):
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
        next_page = "http://quotes.toscrape.com/page/"+str(self.page)+"/"

        if self.page < 11:
            self.page += 1
            yield response.follow(next_page, callback = self.parse)