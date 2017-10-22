# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    detailTitle = scrapy.Field() 
    detailDesc = scrapy.Field()
    price = scrapy.Field()
    allinfo = scrapy.Field()
    url = scrapy.Field()