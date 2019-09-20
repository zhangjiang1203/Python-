#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-18 13:17
# @Author  : 张江
# @Site    : 
# @File    : 002-requests基本用法.py
# @Software: PyCharm

import requests

# response = requests.get("https://www.baidu.com/")
# print(response.status_code)
# print(response.text)
# print(response.cookies)
# print(type(response.text))


# # 各种请求方式展示
# requests.get("")
# requests.post("")
# requests.put("")
# requests.delete("")


# 1.基本get请求
# resp = requests.get('http://www.baidu.com/')
# print(resp.text)

# 2.带参数的get请求
# data = {'name':'jack','age':20}
# resp1 = requests.get("http://httpbin.org/get",params=data)
# print(resp1)

import json
# 3.解析json数据
# resp = requests.get('http://httpbin.org/get')
# print(resp.text)
# print(resp.json())
# print(json.loads(resp.text))
# print(type(resp.json()))

# 4.获取二进制数据
# resp = requests.get('http://www.baidu.com/img/baidu_jgylogo3.gif')
# print(resp.content)
# print(resp.text)
# # 保存图片
# with open('logo.gif','wb') as f:
#     f.write(resp.content)

# 5.添加header
# headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
# resp = requests.get('http://www.baidu.com',headers=headers)
# print(resp.text)

# 6.基本post请求
# data = {'name':'zhangsan'}
# res = requests.post('http://httpbin.org/post',data=data)
# print(res.text)

# 7.文件上传,只需要把文件从文件夹中读取出来，并且赋值给files参数就可以了
# file = {'file':open('logo.gif','rb')}
# res = requests.post('http://httpbin.org/post',files=file)
# print(res.text)

# 8.获取cookies
# resp = requests.get('http://www.baidu.com/')
# print(resp.cookies)
# for (key,value) in resp.cookies.items():
#     print(key + "=" + value)

# 9.会话维持,可以模拟登陆设置session
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')  #设置cookies
# res = s.get('http://httpbin.org/cookies')
# print(res.text)

# 10.SSL证书验证
# res = requests.get("https://kennethreitz.com",verify=True) #verify参数的默认值为True
# print(res.text)

# 11.设置代理展示
# proxies = {'http':"http://10.0.2.23:1080"}
# res = requests.get('http://www.baidu.com',proxies=proxies)
# print(res.status_code)

# 12 超时设置
res = requests.get('http://httpbin.org/get',timeout=0.5)
print(res.status_code)

# 13.错误处理
# from requests.exceptions import ReadTimeout,ConnectionError,RequestException
#
# try:
#     res = requests.get('http://httpbin.org/get',timeout=0.5)
#     print(res.status_code)
# except ReadTimeout:
#     print('time out')
# except ConnectionError:
#     print('connect error')
# except RequestException:
#     #父类错误
#     print('Error')
