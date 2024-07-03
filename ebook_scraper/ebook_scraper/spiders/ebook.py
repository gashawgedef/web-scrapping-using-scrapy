from turtle import title
from unittest import loader
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader
import scrapy
from scrapy.http import Response

    
class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/catalogue/category/books/travel_2/"]
    
    def parse(self, response: Response):
       ebooks =response.css("article.product_pod")
       for ebook in ebooks:
        #    ebook_item = EbookItem()
        loader = ItemLoader(item=EbookItem(),selector=ebook)
        loader.add_css('title',"h3 a::attr(title)")
        loader.add_css('price','p.price_color::text')
        #    ebook_item['title'] = ebook.css("h3 a").attrib['title']
        #    ebook_item['price'] = get_price(ebook.css('p.price_color::text').get())
        yield loader.load_item()
        
       
