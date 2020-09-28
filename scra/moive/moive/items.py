# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoiveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 电影名称
    rating = scrapy.Field()  # 豆瓣评分
    kind = scrapy.Field()   # 类型
    country = scrapy.Field() # 国家
    num_people = scrapy.Field() #人数
    pass

class IfunItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    kind = scrapy.Field()
    country = scrapy.Field()
    people = scrapy.Field()