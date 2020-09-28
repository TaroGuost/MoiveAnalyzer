# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from ..items import IfunItem
import random
import time

class IfunTvSpider(scrapy.Spider):
    name = 'ifun.tv'
    allowed_domains = ['www.ifun.tv']
    start_urls = ['https://www.ifun.tv/list?keyword=&star=&page=51&pageSize=30&cid=0,1,3&year=-1&language=-1&region=-1&status=-1&orderBy=0&desc=true']
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    count = 51

    def start_requests(self):
        print("start")
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5},
                                )

    def parse(self, response):
        items = response.xpath("/html/body/div[2]/app-root/app-search/div/div[2]/div[3]/div/div[2]/app-video-teaser/div/a")
        print(len(items))
        for item in items:
            link = item.xpath("./@href").extract()
            next_page = 'https://www.ifun.tv'+link[0]
            print(next_page)
            time.sleep(3)
            yield SplashRequest(next_page, self.parse_next,
                                endpoint='render.html',
                                args={'wait': 0.5},
                                )
        next_url = self.start_urls[0]
        self.count +=1
        point = next_url.index('pageSize=30')
        page_num = int(next_url[45:point - 1]) + 1
        next_url = next_url[:44] + str(self.count) + next_url[point - 1:]
        print(next_url)
        if self.count < 100:
            yield SplashRequest(next_url, self.parse,
                                endpoint='render.html',
                                args={'wait': 1},
                                )
        pass


    def parse_next(self, response):
        items = response.xpath("//div[@class='root-container']")
        for item in items:
            ifun = IfunItem()
            ifun['title'] = item.xpath(".//div[@class='mb-4']/h1/text()[1]").extract()
            ifun['rating'] = round(random.uniform(0, 5), 2)
            ifun['kind'] = item.xpath(".//div[@class='genre d-flex']//a/text()[1]").extract()
            ifun['people'] = item.xpath(".//div[@class='ico'][1]/div/div[2]/text()[1]").extract()
            ifun['country'] = item.xpath(".//div[@class='region d-flex ng-star-inserted'][1]//a/text()[1]").extract()
            if len(ifun['title']) is not 0:
                yield ifun
        pass