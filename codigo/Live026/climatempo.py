import json

from scrapy import FormRequest, Request, Spider


class ClimatempoSpider(Spider):
    name = "climatempo"

    def start_requests(self):
        yield Request("https://www.climatempo.com.br/brasil", callback=self.parse_start_page)

    def parse_start_page(self, response):
        yield FormRequest("https://www.climatempo.com.br/json/busca-por-nome",
                          formdata={"name": self.search_term},
                          callback=self.parse_search)

    def parse_search(self, response):
        data = json.loads(response.body)
        city_id = data[0]["response"]["data"][0]["idcity"]
        yield Request("https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/{}/".format(city_id),
                      callback=self.parse)

    def parse(self, response):
        city_name = ' '.join(response.css('ul[itemprop="breadcrumb"] > li:last-child > a::text').extract_first().split())

        for day in response.css("#forecast-first-period .wrapper-forecast-day"):
            item = {}
            item["city"] = city_name
            item["date"] = day.css(".title::attr(data-dia)").extract_first()
            item["max"] = day.css('.temperature-block p[arial-label="temperatura máxima"]::text').extract_first()
            item["min"] = day.css('.temperature-block p[arial-label="temperatura mínima"]::text').extract_first()
            yield item
