#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-23 09:45
# @Author  : 张江
# @Site    : 
# @File    : 005-煎蛋网图片.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup

def base_url():
    url = 'http://jandan.net/ooxx/page-'
    urls = []
    for i in range(1,2):
        urls.append(url+str(i))
    return urls

def request_result(url):
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    # 代理，免费的代理只能维持一会可能就没用了，自行更换
    proxies = {'http': '111.23.10.27:8080'}
    try:
        res = requests.get(url,headers=header)
    except:
        res = requests.get(url,header=header,proxies=proxies)
    # 处理对应的标签
    return res.text

def html_parse():
    with open('煎蛋网.txt','w',encoding='utf-8') as f:
        for url in base_url():
            soup = BeautifulSoup(request_result(url),'lxml')
            imglist = soup.select('div.text > p > img')
            for image in imglist:
                image_url = image['src']
                if image_url[0:5] != 'http:':
                    image_url = 'http:' + image_url
                f.write(image_url + '\n')

if __name__ == '__main__':
    html_parse()