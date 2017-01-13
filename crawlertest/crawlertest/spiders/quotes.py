# -*- coding: utf-8 -*-
import scrapy

class JokeSpider(scrapy.Spider):
    name = 'joke'
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    def parse(self, response):
        for joke in response.xpath('//div[@class="quote"]'):
            print joke.xpath('span[1]/text()').extract_first()
            print joke.xpath('span[2]/small/text()').extract_first()

            yield {'joke':joke.xpath('span[1]/text()').extract_first(),
                   'author':joke.xpath('span[2]/small/text()').extract_first()}
        
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        print next_page
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print next_page
            yield scrapy.Request(next_page, callback = self.parse)

