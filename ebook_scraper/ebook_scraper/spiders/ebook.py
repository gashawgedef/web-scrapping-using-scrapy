from turtle import title
from typing import Iterable
from unittest import loader
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader
import scrapy
from scrapy.http import Response

    
class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/catalogue/category/books/travel_2/"]
    cols = ["Title","Price"]
    
   
        
    # def __init__(self):
    #     super().__init__()
    #     # self.page_count = 0
    #     self.page_count = 1
    #     self.total_pages = 4
        
    # def start_requests(self):
    #     base_url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5"
    #     while self.page_count <= self.total_pages:
    #         yield scrapy.Request(
    #             f"{base_url}/page-{self.page_count}.html"
    #         )
    #         self.page_count +=1
    def parse(self, response: Response):
        ebooks =response.css("article.product_pod")
        for ebook in ebooks:
            """The functionality is scrapping details following the link"""
            url = ebook.css('h3 a').attrib['href']
            yield scrapy.Request(
                url=self.start_urls[0]+url,
                callback= self.parse_details
            )
            """
            Get tile and price from the main web site
            ebook_item = EbookItem()
            ebook_item['title'] = ebook.css("h3 a").attrib['title']
            ebook_item['price'] = get_price(ebook.css('p.price_color::text').get())
            yield loader.load_item()
            """
    def parse_details(self,response):
        main = response.css("div.product_main")
        loader = ItemLoader(item=EbookItem(),selector=main)
        loader.add_css('title',"h1::text")
        loader.add_css('price','p.price_color::text')
        quantity_p = main.css("p.availability")
        loader.add_value("quantity",quantity_p.re(r'\(.+ available\)')[0])
        yield loader.load_item()
        
        """
        The functionality is scrapping base web site using pagination
        print("[PAGE COUNT:]",self.page_count)
       next_btn = response.css("li.next a")
       if next_btn:
           next_page_url = next_btn.attrib["href"]
           print("[Next Page Url:]", next_page_url)
       else:
        print("[Next Page Url:] None")
    Takes the href value and attach to the main url
    
        next_btn  =  response.css("li.next a")
        if next_btn:
             next_page =  f"{self.start_urls[0]}/{next_btn.attrib["href"]}"
             yield scrapy.Request(url=next_page)
            
    """
        
       
