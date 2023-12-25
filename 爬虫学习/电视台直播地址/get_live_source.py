# 获取电视直播地址

import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://www.foodieguide.com/iptvsearch/"

header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

source_name_list = [
    'CCTV1'
    # 'CHC高清电影', 'CHC家庭影院', 'CHC动作电影', 'CCTV1', 'CCTV2', 'CCTV3', 'CCTV4', 'CCTV5', 'CCTV6',
    # 'CCTV7', 'CCTV8', 'CCTV9', 'CCTV10', 'CCTV11', 'CCTV12', 'CCTV13', 'CCTV14', 'CCTV15', 'CETV-1', 'CETV-3', 'CETV-4', '北京卫视高清',
    # '北京影视高清', '北京体育高清', '北京新闻高清', '北京纪实高清', '北京卫视','北京文艺', '北京科教', '北京影视', '北京财经', '北京体育', '北京生活',
    # '北京青年', '北京新闻', '北京卡酷', '北京文艺高清', '河南卫视', '安徽卫视高清','重庆卫视高清', '东方卫视高清', '天津卫视高清', '东南卫视高清',
    # '江西卫视高清', '河北卫视高清', '湖南卫视高清', '湖北卫视高清', '辽宁卫视高清','四川卫视高清', '江苏卫视高清', '浙江卫视高清', '江苏卫视高清',
    # '山东卫视高清', '广东卫视高清', '深圳卫视高清', '黑龙江卫视高清', '上海纪实高清','金鹰纪实高清', '全纪实高清', 'CCTV-第一剧场', 'CCTV-国防军事',
    # 'CCTV-怀旧剧场', 'CCTV-风云剧场', 'CCTV-风云足球', 'CCTV-风云音乐','CCTV-世界地理', '安徽卫视', '兵团卫视', '重庆卫视', '东方卫视', '东南卫视',
    # '广东卫视', '广西卫视', '甘肃卫视', '贵州卫视', '湖北卫视', '湖南卫视','河北卫视', '黑龙江卫视', '江苏卫视', '江西卫视', '吉林卫视', '辽宁卫视',
    # '内蒙古卫视', '宁夏卫视', '青海卫视', '新疆卫视', '西藏卫视', '四川卫视','山东卫视', '山西卫视', '陕西卫视', '旅游卫视', '山东教育', '中国教育-1',
    # '中国教育-3', '中国教育-4','凤凰卫视中文台', '凤凰卫视资讯台','凤凰卫视电影台', '星空卫视', 'Star Sports', 'Channel[V]', '探索频道', '国家地理频道'
]

#创建浏览器对象
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)


def mockWebSearch():
    browser.get(base_url)
    title = browser.title
    print("当前直播源====3%s" % title)
    time.sleep(5)

    # for source_name in source_name_list:
    #     search = browser.find_element(by=By.ID, value='kw')
    #     print("当前直播源====1%s" % search)
    #     search.send_keys(source_name)
    # #
    #     submit = browser.find_element(by=By.ID, value='su')
    #     print("当前直播源====2%s" % submit)
    #     submit.click()
    #
    #     time.sleep(10)
    #     #获取对应的网络数据
    #     live_sources = browser.find_elements(by=By.XPATH,value='//div[@class="m3u8"]//td[2]/text()')
    #     print("当前直播源====3%s" %live_sources)


def getAllLiveSource() -> None:
    #搜索以上所有支持的电视的直播源
    for source_name in source_name_list:
        orignal_url = base_url
        print("开始请求============== url:%s" % orignal_url)
        result = requests.post(orignal_url,data={"search":source_name},headers=header)
        # result = requests.post(orignal_url, headers=header)
        try:
            print("当前返回数据===%s" %result.content)
            # html = etree.HTML(result.content.decode('utf-8'))
            # items = html.xpath('//div[@class="m3u8"]//td[2]/text()')
            # print("获取结果信息 %s" %items)
            #
            # if len(items) == 0: break
            #
            # authors = []
            # for item in items:
            #     print("拉流地址===%s" %item)

        except:
            print("出错了展示设置")


if __name__ == '__main__':
    mockWebSearch()
