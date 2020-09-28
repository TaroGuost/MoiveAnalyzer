import scrapy

class moiveSpider(scrapy.Spider):
    name = 'joke'

    start_urls = [
        'https://movie.douban.com/'
    ]

    #user_agent = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"]

    def parse(self, response):
        for joke in response.xpath("//div[@class='slide-page']"):
            yield{
                "joke_text": joke.xpath(".//a/p").extract_first()
            }



