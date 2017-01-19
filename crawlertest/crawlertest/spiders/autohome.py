# -*- coding: utf-8 -*-
import scrapy


class AutoHomeSpider(scrapy.Spider):
    name = 'AutoHome'
    start_urls = ['http://club.autohome.com.cn/bbs/forum-c-4204-1.html']

    def parse(self, response):
        #for weiling_class in response.xpath('//div[@id="subcontent"]'):#//*[@id="subcontent"]/dl[2]
        for href in response.xpath('//div[@id="subcontent"]/dl/dt/a/@href'):
            full_url = reponse.urljoin(href.extract())
            print full_url

            yield Scrapy.Request(full_url, call_back = page_parse)

    def page_parse(self, response):
        #//*[@id="F0"]/div[2]/div[2]/div[1]/div/div[2]
        #//*[@id="F1"]/div[2]/div/div[2]/div/text()
        #//*[@id="F2"]/div[2]/div/div[2]/div/text()
        for item in response.xpath().extract():
            print item
            
