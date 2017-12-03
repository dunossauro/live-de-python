from scrapy import Request, Spider


class PyJobsSpider(Spider):
    name = "pyjobs"

    def start_requests(self):
        yield Request("http://pyjobs.com.br/jobs/")

    def parse(self, response):
        for row in response.css("body > div.container > div.row"):
            title = row.css("h3::text").extract_first()
            company = row.xpath(".//p[contains(text(), 'Empresa:')]/text()").extract_first()
            type_ = row.xpath(".//p[contains(text(), 'Tipo do Job:')]/text()").extract_first()
            date = row.xpath(".//p[contains(text(), 'Data de adição:')]/text()").extract_first()
            location = row.xpath(".//p[contains(text(), 'Local do job:')]/text()").extract_first()
            yield {
                "title": title,
                "company": company,
                "type": type_,
                "date": date,
                "location": location
            }

        for page_url in response.css("body > div.container > .pagination a::attr(href)").extract():
            yield Request(response.urljoin(page_url))
