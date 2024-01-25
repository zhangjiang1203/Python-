# 获取电视直播地址
import json

import requests
import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://www.foodieguide.com/iptvsearch/"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

source_name_list = [
    # 'CCTV1', 'CCTV2', 'CCTV3', 'CCTV4', 'CCTV5', 'CCTV6',
    # 'CCTV7', 'CCTV8', 'CCTV9', 'CCTV10', 'CCTV11', 'CCTV12', 'CCTV13', 'CCTV14', 'CCTV15', 'CETV-1', 'CETV-3', 'CETV-4', '北京卫视高清',
    # '北京影视高清', '北京体育高清', '北京新闻高清', '北京纪实高清', '北京卫视', '河南卫视', '安徽卫视高清','重庆卫视高清', '东方卫视高清', '天津卫视高清', '东南卫视高清',
    # '江西卫视高清', '河北卫视高清', '湖南卫视高清', '湖北卫视高清', '辽宁卫视高清','四川卫视高清', '江苏卫视高清', '浙江卫视高清', '江苏卫视高清',
    # '山东卫视高清', '广东卫视高清', '深圳卫视高清', '黑龙江卫视高清', '上海纪实高清','金鹰纪实高清', '全纪实高清', '安徽卫视', '兵团卫视', '重庆卫视', '东方卫视', '东南卫视',
    # '广东卫视', '广西卫视', '甘肃卫视', '贵州卫视', '湖北卫视', '湖南卫视','河北卫视', '黑龙江卫视', '江苏卫视', '江西卫视', '吉林卫视', '辽宁卫视',
    # '内蒙古卫视', '宁夏卫视', '青海卫视', '新疆卫视', '西藏卫视', '四川卫视','山东卫视', '山西卫视', '陕西卫视', '旅游卫视', '凤凰卫视中文台', '凤凰卫视资讯台','凤凰卫视电影台', '星空卫视', 'Channel[V]', '探索频道', '国家地理频道'
    # 'CHC高清电影', 'CHC家庭影院', 'CHC动作电影',

    'CCTV1',
    'CCTV2',
    'CCTV3',
    'CCTV4',
    'CCTV5',
    'CCTV6',
    'CCTV7',
    'CCTV8',
    'CCTV9',
    'CCTV10',
    'CCTV11',
    'CCTV12',
    'CCTV13',
    'CCTV14',
    'CCTV15',
    'CCTV16',
    'CCTV17',
    'CETV1',
    'CETV2',
    'CETV3',
    'CETV4',
    'CGTN',
    'CHC动作电影',
    'CHC家庭影院',
    'CHC高清电影',
    'CI罪案侦查频道',
    'HMC',
    'History历史频道',
    'HwaZanTV',
    'IPTV3+',
    'IPTV5+',
    'IPTV6+',
    'IPTV8+',
    'IPTVEFEL',
    'IPTV少儿动画',
    'IPTV热播剧场',
    'IPTV相声小品',
    'IPTV经典电影',
    'NEWTV东北热剧',
    'NEWTV中国功夫',
    'NEWTV军事评论',
    'NEWTV军旅剧场',
    'NEWTV古装剧场',
    'NEWTV家庭剧场',
    'NEWTV明星大片',
    'NEWTV欢乐剧场',
    'NEWTV武博世界',
    'NEWTV海外剧场',
    'NEWTV潮妈辣婆',
    'NEWTV炫舞未来',
    'NEWTV精品体育',
    'NEWTV精品大剧',
    'NEWTV精品纪录',
    'NEWTV超级体育',
    'NEWTV超级电影',
    'NEWTV超级电视剧',
    'NEWTV超级综艺',
    'NEWTV金牌综艺',
    'NEXTTVMovie',
    'NEXTTVZonghe',
    'NHK',
    'NHKWorld',
    'NOW新闻台',
    'NationalGeographic_taiwan',
    'NextTVNews',
    'NickJr',
    'Nickelodeon',
    'PiliPuppet',
    'PublicTV',
    'PublicTV2',
    'PublicTV3HD',
    'SinJiTVHD',
    'SkyNews',
    'StarChineseMovies',
    'TVBS',
    'TVBS亚洲',
    'TVBS新闻',
    'TVBS欢乐',
    'TVBS精采',
    'TVBclassic',
    'TVB明珠台',
    'TVB星河',
    'TVB翡翠台',
    'TaiwanPlus',
    'ThaiPBS',
    'TienLiangTVHD',
    'UniqueNews',
    'UniqueUSTVHDUSTVHD',
    'VOA美国之音',
    '七彩戏剧',
    '上海外语',
    '上海教育',
    '上海第一财经',
    '上海都市',
    '上视新闻',
    '世界地理',
    '东南卫视',
    '东方卫视',
    '东方影视',
    '东方财经',
    '东方购物',
    '东莞新闻综合',
    '东风卫视',
    '中华特产',
    '中华美食',
    '中国交通',
    '农林卫视',
    '凤凰中文',
    '凤凰卫视中文台',
    '凤凰卫视电影台',
    '凤凰卫视资讯台',
    '凤凰卫视香港台',
    '凤凰资讯',
    '动漫秀场',
    '咪咕体育',
    '咪咕音乐',
    '哈哈炫动',
    '哒啵电竞',
    '哒啵赛事',
    '嘉佳卡通',
    '湖南都市',
    '湖南金鹰卡通',
    '潮州综合',
    '澳亚卫视',
    '澳视澳门',
    '澳门莲花',
    '爱上4K',
    '爱尔达娱乐台',
    '爱看导视',
    '环球奇观',
    '环球旅游',
]

tvname = [
"MTV音乐",
"怀旧音乐",
"MTV音乐频道",
"MV音乐",
"新音乐",
"音乐_22",
"音乐_70",
"80后音乐",
"番薯音乐",
"鬥魚音樂",
"斗鱼音乐",
"车载音乐",
"风云音乐",
"音乐现场",
"咪咕音乐",
"中国音乐",
"音乐荟萃",
"鬥魚直播-T-ARA音樂",
"乐享汇_音乐正青春"
          ]


def mockWebSearch():
    # 创建浏览器对象
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.get(base_url)
    total_source_list = []

    for item_source in source_name_list:
        # 设置搜索名, 设置之前 先清空之前的搜索
        inputField = browser.find_element(by=By.ID, value='search')
        inputField.clear()
        inputField.send_keys(item_source)
        # 开始搜索
        browser.find_element(by=By.XPATH, value='//*[@id="form1"]/input[2]').click()

        live_sources = browser.find_elements(by=By.XPATH, value='//div[@class="m3u8"]//td[2]')
        if len(live_sources) > 10:
            live_sources = live_sources[0:10]
        live_sources = list(map(lambda item: item.text, live_sources))
        print(live_sources)

        total_source_list.append({"name": item_source, "sources": live_sources})
        time.sleep(1)

    # total_source_list 转json保存为文件
    with open('live_source.json', 'w+', encoding='utf-8') as json_file:
        json.dump(total_source_list, json_file, ensure_ascii=False, indent=4)


def getAllLiveSource():

    # 获取电视资源信息
    with open('IPTVName.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for item in data:
            print(data[item])


    # # 搜索以上所有支持的电视的直播源
    # for source_name in source_name_list:
    #     original_url = base_url
    #     print("开始请求============== url:", original_url)
    #     result = requests.post(original_url, data={"search": source_name}, headers=header)
    #     # result = requests.post(original_url, headers=header)
    #     try:
    #         print("当前返回数据===%s" % result.content)
    #         # html = etree.HTML(result.content.decode('utf-8'))
    #         # items = html.xpath('//div[@class="m3u8"]//td[2]/text()')
    #         # print("获取结果信息 %s" %items)
    #         #
    #         # if len(items) == 0: break
    #         #
    #         # authors = []
    #         # for item in items:
    #         #     print("拉流地址===%s" %item)
    #
    #     except:
    #         print("出错了展示设置")


if __name__ == '__main__':
    getAllLiveSource()
    # getCategoryTVData()
    # mockWebSearch()
