# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pstats
from itemadapter import ItemAdapter
from openpyxl import Workbook
from pymongo import MongoClient
from sqlalchemy import false

class EbookScraperPipeline:
    def open_spider(self,spider):
        # self.client =MongoClient(
        #     host="mongodb+srv://gashawgedef:Enzakuna12@cluster0.qife2ux.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        #     connect=False
        #     )
        # self.collection = self.client.get_database("ebook").get_collection("travel")
        self.workbook = Workbook()
        self.sheet = self.workbook.active # get the active sheet
        self.sheet.title = "ebooks"
        
        self.sheet.append(spider.cols)
    
    def process_item(self, item, spider):
        # self.collection.insert_one(
        #     ItemAdapter(item).asdict()
        # )
        # return item
        self.sheet.append([item['title'],item['price']])
        return item
    
    def close_spider(self,spider):
        # self.client.close()
         
        self.workbook.save("ebooks.xlsx")