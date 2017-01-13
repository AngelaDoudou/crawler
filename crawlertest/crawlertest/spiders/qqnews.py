# -*- coding: utf-8 -*-
import scrapy

class QQNewsSpider(scrapy.Spider):
    name = 'qqnews'
    start_urls = ['http://news.qq.com/world_index.shtml']

    def parse(self, response):
        for href in response.xpath('//*[@id="news"]/div/div/div/div/em/a/@href'):
            full_url = response.urljoin(href.extract())
            print full_url
            yield scrapy.Request(full_url, callback = self.parse_page)

    def parse_page(self, response):
        print response.xpath('//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/h1/text()').extract()[0]
        yield {'title':response.xpath('//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/h1/text()').extract()[0].encode('utf-8')}



