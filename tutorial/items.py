# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AFLItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    state = scrapy.Field()
    establish = scrapy.Field()
    stadium = scrapy.Field()
    clubURL = scrapy.Field()
    logoURL = scrapy.Field()


    pass
