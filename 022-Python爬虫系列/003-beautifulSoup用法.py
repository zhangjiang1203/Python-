#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-18 15:49
# @Author  : 张江
# @Site    : 
# @File    : 003-beautifulSoup用法.py
# @Software: PyCharm

#beautifulSoup的安装
# pip3 install beautifulsoup4
'''
beautiful是一个标准的网页解析库，支持多种解析器，最主流的两个为python标准库，一个是lxml解析器
from bs4 import BeautifulSoup
# python的标准库
BeautifulSoup(html,'html.parser')

#lxml
BeautifulSoup(html,'lxml')
Python内置标准库的执行速度一般，但是低版本的Python中，中文的容错能力比较差。
lxmlHTML 解析器的执行速度快，但是需要安装 C语言的依赖库。
'''


from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'lxml')
# 获取标签
# print(soup.title)
# #获取标签
# print(soup.title.name)
# # 获取内容
# print(soup.title.string) #获取标签对应的值

# beautifulsoup 的常用API
# find_all(name, attrs, recursive, text, **kwargs)
'''
name 参数可以查找所有名字为 name 的 tag,字符串对象会被自动忽略掉。
'''
# 搜索id为link2的a标签
# print(soup.find_all('a',id='link2'))
# 获取class为title的p标签的内容
# 这里注意下，class是Python的内部关键词，我们需要在css属性class后面加一个下划线'_'，不然会报错
# print(soup.find_all('p',class_='title')[0].string)
# for tempDiv in soup.find_all('p',class_='title'):
#     print(tempDiv.string)

# limit 关键字，限制返回结果的数量
# soup.find_all('a',limit=2)

# find返回的是单个元素,没有查找到目标的时候返回None，find_all()没有查找到目标的时候返回的是一个空列表

# CSS选择器
'''
BeautifulSoup 支持大部分的CSS选择器，在tag或者BeautifulSoup对象的```.select()```方法中传入字符串即可使用css选择器的语法找到tag
在写CSS的时候标签class类名加. id属性加#
'''

# print(soup.select('title'))
# # 通过tag标签逐层查找
# print(soup.select('body a'))
# print(soup.select('html head title'))
# # 找到某个标签下的直接子标签
# print(soup.select('head > title'))
# print(soup.select('p > #link'))
# print(soup.select('body > a'))
# # 通过类名查找
# print(soup.select('.sister'))
# # 通过tag的id查找
# soup.select('#link1')
# # 同时用多种CSS选择器查询元素，使用,号隔开
# soup.select('#link1,#link2')
# 如果提取如tr标签下的第二个td标签，一般的css选择器选择是tr > td:ntn:child(2)，
# 而在bs4中这么写是会报错的，我们需要将他改为tr > td:nth-of-type(2)。
# 提取标签内容
# list = [<a href="http://www.baidu.com/">百度</a>,<a href="http://www.163.com/">网易</a>,<a href="http://www.sina.com/"新浪</a>]
for i in  soup.select('.sister'):
    print(i.get_text()) #获取标签内容
    # print(i.get['href'])
    print(i['href']) #获取标签属性
