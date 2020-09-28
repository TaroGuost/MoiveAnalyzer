# -*- coding: utf-8 -*-
import scrapy
from ..items import MoiveItem
import json
from scrapy_splash import SplashRequest

class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=349&page_start=0']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5},
                                )



    def parse(self, response):
        #print(response.meta)
        # movie_items = response.xpath("//div[@class='list']/a[@class='item']")
        # for item in movie_items:
        #     next_page = item.xpath(".//@href").extract()
        #     print(next_page)
        #     if next_page is not None:
        #         yield scrapy.Request(next_page[0] , self.parse2)

        next_link = []
        print(response.body_as_unicode())
        sites = json.loads(response.body_as_unicode())

        for i in sites['subject']:
            next_link.append(i['title'])

        print(next_link)

        yield next_link
        # result_dic = json.loads(response.body)
        # for object in result_dic['subjects']:
        #     movie = MoiveItem()
        #     movie['title'] = object['title']
        #     movie['rate'] = object['rate']
        #     yield movie

        # next_page = response.xpath("//div[@class='list-wp']/a[@class='more']/@href")
        # if next_page is not None and count != 1:
        #     next_page_link = response.urljoin(next_page)
        #     yield scrapy.Request(url = next_page_link , callback=self.parse(count = 1))
        pass

    # def parse2(self,response):
    #     movie_items = response.xpath("//div[@id='content']")
    #     for item in movie_items:
    #         movie = MoiveItem()
    #
    #         # movie['rank'] = item.xpath('/a/p').extract()
    #         # movie['title'] = item.xpath(
    #         #     '/a/p').extract()
    #         # movie['poster'] = item.xpath('/a/p').extract()
    #         # movie['link'] = item.xpath('/a/p').extract()
    #         # movie['rating'] = item.xpath(
    #         #     '/a/p').extract()
    #         movie['title'] = item.xpath(".//h1/span/text()[1]").extract()
    #         movie['rating'] = item.xpath(".//div[@id='interest_sectl']//strong/text()[1]").extract()
    #         movie['kind'] = item.xpath(".//span[@property='v:genre']/text()[1]").extract()
    #         movie['country'] = item.xpath(".//div[@id='info']/text()[normalize-space()]").extract()
    #         movie['num_people'] = item.xpath(".//span[@property='v:votes']/text()[1]").extract()
    #
    #         movie['title'] = movie['title'][0].split()[0]
    #         for c in movie['country']:
    #             if c != ' ' and c != ' / ':
    #                 c = c.replace(' ' , '')
    #                 c = c.split('/')[0]
    #                 movie['country'] = c
    #                 break
    #
    #
    #         yield movie