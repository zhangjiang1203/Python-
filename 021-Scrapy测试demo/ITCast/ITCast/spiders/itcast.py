# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import scrapy
from ITCast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    # 爬虫名称
    name = 'itcast'
    # 爬虫允许的爬取范围
    allowed_domains = ['http://www.itcast.cn']
    # 爬虫开始请求的ULR
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ac']

    # 处理响应文件
    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")

        for node in node_list:

            #创建items字段对象，用来存储信息
            item = ItcastItem()
            #.extract() 将xpath对象转换为unicode字符串
            name = node.xpath('./h3/text()').extract()
            title = node.xpath('./h4/text()').extract()
            info = node.xpath('./p/text()').extract()

            #开始对对象赋值
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            #yield返回提取到的每个item数据，给管道文件处理，同时还回来继续执行后面的代码
            #return 返回之后整个函数就结束了
            yield item


