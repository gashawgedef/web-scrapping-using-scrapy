from turtle import title
from typing import Any
import scrapy
from scrapy.http import Response

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]
    
    def parse(self, response: Response):
        print(["parse"])
        print( response.css("h3 a::text")[0])
        print(response.xpath("//h3/a/text()")[0])
        #  article_html = response.css("article")
        #  for ebook in article_html:
        #      title = ebook.css("a::text").get()
        #      price = ebook.css("p.price_color::text").get()
        #      yield {
        #          "title":title,
        #          "price":price
        #      }
            
             
        #  print(article_html)
     
