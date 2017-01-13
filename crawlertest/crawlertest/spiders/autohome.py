# -*- coding: utf-8 -*-
import scrapy


class AutoHomeSpider(scrapy.Spider):
    name = 'AutoHome_weiling'
    start_urls = ['http://club.autohome.com.cn/bbs/forum-c-4204-1.html']

    def parse(self, response):
        #for weiling_class in response.xpath('//div[@id="subcontent"]'):#//*[@id="subcontent"]/dl[2]
        for weiling_class in response.xpath('//dl[@class="list_dl"]'):#//*[@id="subcontent"]/dl[2]
            print weiling_class.xpath('dt/a/text()').extract_first().encode('utf-8')
            
            yield {'titil':weiling_class.xpath('dt/a/text()').extract_first()}

