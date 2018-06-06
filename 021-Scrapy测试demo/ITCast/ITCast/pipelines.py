# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ItcastPipeline(object):

    def __init__(self):
        self.f = open('itcast_pipeline.json','w')
        print('初始化代码')

    def process_item(self, item, spider):
        content = json.dump(dict(item),ensure_ascii=False) + ', \n'
        self.f.write(content.encode('utf-8'))
        return item

    def close_spider(self,spider):
        self.f.close()
