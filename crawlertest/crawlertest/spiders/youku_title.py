# -*- coding: utf-8 -*-
import scrapy
from crawlertest.items import CrawlertestItem

import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")


class YoukuSpider(scrapy.Spider):
    name = 'youku'
    #减慢爬取速度 为1s
    download_delay = 1 
    start_urls = [#'http://list.youku.com/category/show/c_97.html',
            #'http://list.youku.com/category/show/c_96.html',
            #'http://list.youku.com/category/show/c_85.html',
            #'http://list.youku.com/category/show/c_100.html',
            #'http://list.youku.com/category/show/c_95.html',
            'http://list.youku.com/category/show/c_95_a__s_1_d_1.html.html',
            #'http://list.youku.com/category/show/c_87.html',
            #'http://list.youku.com/category/show/c_84.html',
            #'http://list.youku.com/category/show/c_98.html',
            #'http://list.youku.com/category/video/c_86.html',
            #'http://list.youku.com/category/video/c_91.html',
            #'http://list.youku.com/category/video/c_99.html',
            #'http://list.youku.com/category/video/c_94.html',
            #'http://list.youku.com/category/video/c_103.html',
            #'http://list.youku.com/category/video/c_104.html',
            #'http://list.youku.com/category/video/c_105.html',
            #'http://list.youku.com/category/video/c_89.html',
            #'http://list.youku.com/category/video/c_90.html',
            #'http://list.youku.com/category/video/c_88.html',
            #'http://list.youku.com/category/video/c_171.html',
            #'http://list.youku.com/category/video/c_172.html',
            #'http://list.youku.com/category/video/c_174.html',
            #'http://list.youku.com/category/video/c_175.html',
            #'http://list.youku.com/category/video/c_176.html',
            #'http://list.youku.com/category/video/c_102.html'
            ]

    def parse(self, response):
        label = response.xpath('//*[@id="filterPanel"]/div[1]/ul/li[@class="current"]/span/text()').extract_first()
        print label
        for title in response.xpath('/html/body/div[@class="s-body"]/div/div[@class="vaule_main"]/div[@class="box-series"]/ul/li/div/ul[@class="info-list"]/li[@class="title"]/a/@title').extract():
            item = CrawlertestItem()
            item['label'] = label
            item['title'] = title
            print item
            yield item

        url = response.xpath('/html/body/div[@class="s-body"]/div/div[@class="vaule_main"]/div[@class="yk-pager"]/ul/li[@class="next"]/a/@href').extract_first()
        full_url = response.urljoin(url)
        yield scrapy.Request(full_url, callback=self.parse)
            
