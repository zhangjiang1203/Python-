# 获取电视直播地址
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://www.foodieguide.com/iptvsearch/"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

source_name_list = [
    'CCTV1', 'CCTV2', 'CCTV3', 'CCTV4', 'CCTV5', 'CCTV6', 'CCTV7', 'CCTV8', 'CCTV9', 'CCTV10', 'CCTV11', 'CCTV12',
    'CCTV13', 'CCTV14', 'CCTV15', 'CCTV16', 'CCTV17',
    'CETV1', 'CETV2', 'CETV3', 'CETV4', 'CGTN', 'CHC动作电影', 'CHC家庭影院', 'CHC高清电影', 'CI罪案侦查频道', 'HMC',
    'History历史频道', 'HwaZanTV', 'IPTV3+', 'IPTV5+',
    'IPTV6+', 'IPTV8+', 'IPTVEFEL', 'IPTV少儿动画', 'IPTV热播剧场', 'IPTV相声小品', 'IPTV经典电影', 'NEWTV东北热剧',
    'NEWTV中国功夫', 'NEWTV军事评论', 'NEWTV军旅剧场',
    'NEWTV古装剧场', 'NEWTV家庭剧场', 'NEWTV明星大片', 'NEWTV欢乐剧场', 'NEWTV武博世界', 'NEWTV海外剧场',
    'NEWTV潮妈辣婆', 'NEWTV炫舞未来', 'NEWTV精品体育', 'NEWTV精品大剧',
    'NEWTV精品纪录', 'NEWTV超级体育', 'NEWTV超级电影', 'NEWTV超级电视剧', 'NEWTV超级综艺', 'NEWTV金牌综艺',
    'NEXTTVMovie', 'NEXTTVZonghe', 'NHK', 'NHKWorld', 'NOW新闻台',
    'NationalGeographic_taiwan', 'NextTVNews', 'NickJr', 'Nickelodeon', 'PiliPuppet', 'PublicTV', 'PublicTV2',
    'PublicTV3HD', 'SinJiTVHD', 'SkyNews',
    'StarChineseMovies', 'TVBS', 'TVBS亚洲', 'TVBS新闻', 'TVBS欢乐', 'TVBS精采', 'TVBclassic', 'TVB明珠台', 'TVB星河',
    'TVB翡翠台', 'TaiwanPlus', 'ThaiPBS', 'TienLiangTVHD',
    'UniqueNews', 'UniqueUSTVHDUSTVHD', 'VOA美国之音', '七彩戏剧', '上海外语', '上海教育', '上海第一财经', '上海都市',
    '上视新闻', '世界地理', '东南卫视', '东方卫视', '东方影视', '东方财经',
    '东方购物', '东莞新闻综合', '东风卫视', '中华特产', '中华美食', '中国交通', '农林卫视', '凤凰中文',
    '凤凰卫视中文台', '凤凰卫视电影台', '凤凰卫视资讯台', '凤凰卫视香港台', '凤凰资讯',
    '动漫秀场', '咪咕体育', '咪咕音乐', '哈哈炫动', '哒啵电竞', '哒啵赛事', '嘉佳卡通', '湖南都市', '湖南金鹰卡通',
    '潮州综合', '澳亚卫视', '澳视澳门', '澳门莲花', '爱上4K', '爱尔达娱乐台',
    '爱看导视', '环球奇观', '环球旅游'
]


def mockWebSearch():
    # 创建浏览器对象
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.get(base_url)

    with open('IPTVName.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        iptv_map = {}
        for item in data:
            iptv_names = data[item]
            iptv_sources = []
            for iptv_name in iptv_names:
                item_title = iptv_name["title"]

                # 设置搜索名, 设置之前 先清空之前的搜索
                inputField = browser.find_element(by=By.ID, value='search')
                inputField.clear()
                inputField.send_keys(item_title)
                # 开始搜索
                browser.find_element(by=By.XPATH, value='//*[@id="form1"]/input[2]').click()

                live_sources = browser.find_elements(by=By.XPATH, value='//div[@class="m3u8"]//td[2]')
                if len(live_sources) > 10:
                    live_sources = live_sources[0:10]
                live_sources = list(map(lambda item: item.text, live_sources))
                if len(live_sources) > 0:
                    iptv_sources.append({"name": item_title, "sources": live_sources, "icon": iptv_name["icon"]})
                    print(f"{item_title}, {live_sources}")

                time.sleep(0.5)

            if len(iptv_sources) > 0:
                iptv_map[item] = iptv_sources

    # total_source_list 转json保存为文件
    with open('live_source.json', 'w+', encoding='utf-8') as json_file:
        json.dump(iptv_map, json_file, ensure_ascii=False, indent=4)


def getAllLiveSource():
    # 获取电视资源信息
    with open('IPTVName.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for item in data:
            iptv_names = data[item]
            for iptv_name in iptv_names:
                print("数据展示" + iptv_name["title"])


if __name__ == '__main__':
    # getAllLiveSource()
    # getCategoryTVData()
    mockWebSearch()
