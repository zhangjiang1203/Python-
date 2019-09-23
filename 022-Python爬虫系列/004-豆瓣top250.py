#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-20 15:48
# @Author  : 张江
# @Site    : 
# @File    : 004-豆瓣top250.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup

def url_list():
    url = "https://book.douban.com/top250?start=0"
    url_list = []
    for i in range(0,255,25):
        url_list.append(url+str(i))
    return url_list

def get_html(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    res = requests.get(url,headers=headers)
    return res.text

def html_parse():
    with open('豆瓣top250.txt','w',encoding='utf-8') as f:
        for url in url_list():
            soup = BeautifulSoup(get_html(url), 'lxml')
            # 书名
            alldiv = soup.find_all('div', class_='pl2')
            book_names = [a.find('a').get_text() for a in alldiv]
            # 作者
            allp = soup.find_all('p', class_='pl')
            authors = [a.get_text() for a in allp]
            # 获取评分
            starspan = soup.find_all('span', class_='rating_nums')
            stars = [a.get_text() for a in starspan]
            # 简介
            sum_div = soup.select('tr.item > td:nth-of-type(2)')
            sums = []
            for div in sum_div:
                sumspan = div.find('span',class_='inq')
                summary = sumspan.get_text() if sumspan else '无'
                sums.append(summary)

            for name, author, score, sum in zip(book_names, authors, stars, sums):
                name = "书名：" + str(name.replace(" ","").replace('\n','')) + '\n'
                author = "作者：" + str(author) + '\n'
                score = '评分：' + str(score) + '\n'
                sum = "简介：" + str(sum) + '\n'
                data = name + author + score + sum
                # 保存数据 seconds (remaining:
                f.write('\n' + '='*30 + '\n' + data + '='*30 + '\n')

if __name__ == '__main__':
    html_parse()











