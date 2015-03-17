# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PylectureItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    processor = scrapy.Field()
    processor_intro = scrapy.Field()
    datetime = scrapy.Field()
    description = scrapy.Field()
    position = scrapy.Field()
    suborg = scrapy.Field()
