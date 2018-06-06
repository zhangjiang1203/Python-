import scrapy
from mySpider.items import itcastitem

class ItcastSpider(scrapy.spiders.Spider):
    # 爬虫的识别名称
    name = 'itcast'
    # 搜索的域名范围
    allowed_domains = ['http://www.itcast.cn']
    # 爬虫开始抓取的列表
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ac']


    def parse(self, response):
        items = []
        for site in response.xpath('//div[@class="li_txt"]'):

            item = itcastitem()
            teacher_name = site.xpath('h3/text()').extract()
            teacher_level = site.xpath('h4/text()').extract()
            teacher_info = site.xpath('p/text()').extract()

            # print(teacher_name[0].decode('utf-8'))
            # print(teacher_level[0])
            # print(teacher_info[0])

            item['name'] = teacher_name[0]
            item['level'] = teacher_level[0]
            item['info'] = teacher_info[0]
            # print(itcastitem.name,itcastitem.level,itcastitem.info)
            items.append(item)
            # print(items[0].name)

        return items

# 运行命令 在同级文件中生成一个json文件  scrapy crawl itcast -o itcast_teacher.json -t json