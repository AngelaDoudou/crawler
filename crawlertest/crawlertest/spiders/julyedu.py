# -*- coding: utf-8 -*-
import scrapy

class JulySpider(scrapy.Spider):
    name = 'julyedu'
    start_urls = ['https://www.julyedu.com/category/index',]

    def parse(self, response):
        for july_class in response.xpath('//div[@class="course_info_box"]'):
            print july_class.xpath('a/h4/text()').extract_first()

            yield {'title':july_class.xpath('a/h4/text()').extract_first()}
