from scrapy import Request, Spider


class DelaySpider(Spider):
    name = "delay"

    def start_requests(self):
        for delay in [1, 2, 3, 4, 5]:
            url = "http://httpbin.org/delay/{}".format(delay)
            yield Request(url)

    def parse(self, response):
        pass
