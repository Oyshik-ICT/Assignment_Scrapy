# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelscrapItem(scrapy.Item):
    country = scrapy.Field()
    title = scrapy.Field()
    img_src_list = scrapy.Field()
    rating  =  scrapy.Field()
    room = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
