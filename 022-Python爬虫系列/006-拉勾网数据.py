#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-26 13:29
# @Author  : 张江
# @Site    : 
# @File    : 006-拉勾网数据.py
# @Software: PyCharm

import pymysql
import random
import requests
import time
from bs4 import BeautifulSoup

def connect_db():
    db = pymysql.connect('localhost','root','12345678','lagouDataBase')
    # cursor = db.cursor()
    # cursor.execute('select * from Positions')
    # result = cursor.fetchall()
    # print(result)
    return db


def request_setting(url):
    '''
    设置request的配置信息
    :param url:
    :return:
    '''
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    ]
    user_agent = random.choice(user_agent_list)

    headers = {
        'Cookie': 'user_trace_token=20170603115043-d0c257a054ee44f99177a3540d44dda1; LGUID=20170603115044-d1e2b4d1-480f-11e7-96cf-525400f775ce; JSESSIONID=ABAAABAAAGHAABHAA8050BE2E1D33E6C2A80E370FE9167B; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; login=false; unick=""; _putrc=""; _ga=GA1.2.922290439.1496461627; X_HTTP_TOKEN=3876430f68ebc0ae0b8fac6c9f163d45; _ga=GA1.3.922290439.1496461627; LGSID=20170720174323-df1d6e50-6d2f-11e7-ac93-5254005c3644; LGRID=20170720174450-12fc5214-6d30-11e7-b32f-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500541369; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500543655',
        'User-Agent': user_agent,
    }
    proxy_list = [
        'http://140.224.76.21:808',
        'http://60.178.14.90:8081',
        'http://121.232.146.13:9000',
    ]
    proxy_ip = random.choice(proxy_list)
    proxies = {
        'http':proxy_ip,
        'https':proxy_ip,
    }

    resp = requests.get(url,headers=headers)#,proxies=proxies)
    # time.sleep(1)
    return resp

def lagou_page():
    base_url = 'https://lagou.com/zhaopin/Java/'
    db = connect_db()
    cursor = db.cursor()
    for page in range(1,30):
        url = base_url + str(page) + "/"
        # 开始请求网络
        resp = request_setting(url)

        if resp.status_code == 404:
            print("[33m没有这个页面0m]")
            continue
        soup = BeautifulSoup(resp.text,'lxml')
        # 获取对应的公司名称等信息保存到数据库
        names = soup.select('ul > li > div.list_item_top > div.position > div.p_top > a > h3')
        # 工作地址
        adds = soup.select('ul > li > div.list_item_top > div.position > div.p_top > a > span > em')
        # 发布时间
        publishs = soup.select('ul > li > div.list_item_top > div.position > div.p_top > span')
        # 薪资信息
        moneys = soup.select('ul > li > div.list_item_top > div.position > div.p_bot > div > span')
        # 工作需求
        needs = soup.select('ul > li > div.list_item_top > div.position > div.p_bot > div')
        # 发布公司
        companys = soup.select('ul > li > div.list_item_top > div.company > div.company_name > a')
        tags = []
        # 由于我发现有的招聘信息没有标签信息，if判断防止没有标签报错
        if soup.find('div', class_='li_b_l'):
            # 招聘信息标签
            tags = soup.select('ul > li > div.list_item_bot > div.li_b_l')
            # 公司福利
        fulis = soup.select('ul > li > div.list_item_bot > div.li_b_r')

        # 保存到数据库
        for name,add,publish,money,need,company,tag,fuli in zip(names,adds,publishs,moneys,needs,companys,tags,fulis):
            print("*"*50)
            print("职位:" + name.get_text())
            print("地址:" + add.get_text())
            print("时间:" + publish.get_text())
            print("薪资:" + money.get_text())
            print("要求:" + need.get_text().replace(" ","").replace("\n",""))
            print("公司:" + company.get_text())
            print("信息:" + tag.get_text().replace(" ","").replace("\n",""))
            print("福利:" + fuli.get_text())

            temp_name = name.get_text()
            temp_add = add.get_text()
            temp_time = publish.get_text()
            temp_money = money.get_text()
            temp_need = need.get_text().replace(" ", "").replace("\n", "")
            temp_company = company.get_text()
            temp_tag = tag.get_text().replace(" ", "").replace("\n", "")
            temp_fuli = fuli.get_text()

            # sql = "INSERT INTO Positions (name,time,address,require,money,company,fulis,tags) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" %(name.get_text(),publish.get_text(),add.get_text(),need.get_text(),money.get_text(),company.get_text(),fuli.get_text(),tag.get_text())
            # print(sql)
            sql = "INSERT INTO Positions (name,address,need,time,money,company,fulis,tags) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" %(temp_name,temp_add,temp_need,temp_time,temp_money,temp_company,temp_fuli,temp_tag)

            cursor.execute(sql)
            # print(result)
            db.commit()
    db.close()


if __name__ == "__main__":
    lagou_page()