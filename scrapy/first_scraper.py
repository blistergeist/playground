# first_scraper.py

import scrapy

class basicSpider(scrapy.Spider):
    name = 'basicSpider'
    start_urls = ['www.wsj.com']

    def parse(self, response):
        for title in response.css('h3.wsj-headline dj-sg wsj-card-feature heading-3'):
            yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('div.prev-post > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
