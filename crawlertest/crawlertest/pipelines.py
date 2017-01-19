# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class CrawlertestPipeline(object):
    def __init__(self):
        self.file = codecs.open('youku_title_video_pip.json',mode = 'wb',encoding = 'utf-8')
    '''
    def open_spider(self):
        self.file = open('youku_title_pipe.csv', 'wb', encoding = 'utf-8')
        head = "label,title"
        self.file.write(head)

    def close_spider():
        self.file.close()
    '''
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))
        #line = "%s,%s" % item.label, item.title
        #self.file.write(line)
        return item
