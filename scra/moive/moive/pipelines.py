# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoivePipeline(object):
    def process_item(self, item, spider):
        print('豆瓣排名：' + item['title'][0])
        print('电影名称：' + item['rating'][0])
        print('链接地址：' + item['kind'][0])
        print('豆瓣评分：' + item['country'][0] + '\n')

        return item
