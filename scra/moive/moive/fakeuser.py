from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class FakeUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')