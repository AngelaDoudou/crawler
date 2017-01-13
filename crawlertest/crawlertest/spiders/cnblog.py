# -*- coding: utf-8 -*-
import scrapy

class CnBlogSpider(scrapy.Spider):
    name = 'cnblog'
    start_urls = ['https://www.cnblogs.com/pick/#%s' % p for p in range(1,21)]

    def parse(self, response):
        for blog in response.xpath('//div[@class="post_item"]'):
            print blog.xpath('div[@class="digg"]/div/span/text()').extract_first()
            print blog.xpath('div[@class="post_item_body"]/h3/a/text()').extract_first()

            yield {'recom_num':blog.xpath('div[@class="digg"]/div/span/text()').extract_first().encode('utf-8'),
                    'title':blog.xpath('div[@class="post_item_body"]/h3/a/text()').extract_first().encode('utf-8')}
