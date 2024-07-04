# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from itemloaders.processors import MapCompose, TakeFirst
from scrapy import Item, Field
def get_price(txt):
    return float(txt.replace("£",''))
def get_quantity(txt):
    return int(txt.replace('(','').split()[0])
class EbookItem(Item):
    title= Field(output_processor = TakeFirst())
    price =Field(
        input_processor =MapCompose(get_price),
        output_processor = TakeFirst()
    )
    quantity = Field(
        input_processor =MapCompose(get_quantity),
        output_processor = TakeFirst())
    
