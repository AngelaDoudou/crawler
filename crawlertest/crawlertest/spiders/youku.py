# -*- coding: utf-8 -*-
import scrapy

import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")


class YoukuSpider(scrapy.Spider):
    name = 'Youku'
    start_urls = ['http://list.youku.com/category/video/c_0.html']

    def parse(self, response):
        #for weiling_class in response.xpath('//div[@id="subcontent"]'):#//*[@id="subcontent"]/dl[2]
        for li in response.xpath('//*[@id="filterPanel"]/div/ul/li'):
            href = li.xpath('a/@href').extract_first()
            full_url = response.urljoin(href)
            text = li.xpath('a/text()').extract_first()
            #print href
            #print full_url
            #print text
            yield scrapy.Request(full_url, callback = self.page_parse)
            #yield {'url':full_url, 'title':text}
            
    def page_parse(self, response):
        #print 'hello'
        cl = response.xpath('//*[@id="filterPanel"]/div[1]/ul/li[@class="current"]/span/text()').extract_first()
        print cl
        for title in response.xpath('/html/body/div[@class="s-body"]/div/div[@class="vaule_main"]/div[@class="box-series"]/ul/li/div/ul[@class="info-list"]/li[@class="title"]/a/@title').extract():
            yield {"label":cl,"title":title}
        '''
        for li in response.xpath('//div[@class="item"]'):
            label = li.xpath('label/text()').extract_first()
            print label
            
            for slabel in li.xpath('ul/li'):
                href = slabel.xpath('a/@href').extract_first()
                full_url = response.urljoin(href)
                text = slabel.xpath('a/text()').extract_first()
                #print full_url
                print cl
                print label
                print text
                #yield {'label':label, 'sublabel':text, 'suburl':full_url}
                yield {'1st_label':cl, '2nd_label':label, '3rd_label':text}
        '''
        '''
        for li in response.xpath('/html/body/div/div/div/div/ul/li'):
            title = li.xpath('div/ul[2]/li/a/@title').extract_first()
            print title
            yield{'label':cl, 'title':title}
        '''    

