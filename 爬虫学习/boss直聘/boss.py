# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:张江

import requests
import json
import time
from lxml import etree
from positionModel import Position

# https://www.zhipin.com/c101020100-p100109/
# https://www.zhipin.com/c101020100-p100109/?page=2&ka=page-2


def getPositionList():

    url = 'https://www.zhipin.com/c101020100-p100109/'
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }

    result = requests.get(url,headers=header)
    html = etree.HTML(result.content)
    path = html.xpath('//*[@id="main"]/div/div[2]/ul/li/div/div[1]/h3/a/div/text()')

    # name, salary, position_desc, company
    position = Position('zhangsan','15k-19k','哈哈哈哈 ','shanghai')
    savePositionToDB(position)
    print(path)




def savePositionToDB(position):
    # 保存到数据库
    print(position.name,position.salary)


if __name__ == "__main__" :

    getPositionList()
