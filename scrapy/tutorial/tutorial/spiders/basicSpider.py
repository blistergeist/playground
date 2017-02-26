# first_scraper.py

import scrapy

class basicSpider(scrapy.Spider):
    name = 'basicSpider'
    start_urls = ['www.wsj.com']

    def parse(self, response):
    	page = response.url.split("/")[-2]
    	fileName = 'quotes-{}.html'.format(page)
    	with open(fileName, 'wb') as f:
    		f.write(response.body)