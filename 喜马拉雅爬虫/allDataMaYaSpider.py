import requests
import json
import time
from lxml import etree

'''
文件太多 大概需要五分钟 才能完成，只是存储文字 还没有下载 下载磁盘内存不足
'''

class MaYaRequest:
    def __init__(self,path):
        self.header = {
             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        self.path = path
        self.start_url = 'https://www.ximalaya.com/top/'


    #获取所有的id目录
    def getRequestURL(self):
        print('开始获取所有请求的id')
        result = requests.get(self.start_url,headers=self.header)
        #通过etree.HTML()方法转换为xml，xml用数据可以通过xpath() 表达式去获取数据
        html = etree.HTML(result.content.decode('utf-8'))
        #xpath过滤信息,获取对应的id
        items = html.xpath('//*[@id="root"]/main/section/div/div[2]/div[2]/div[2]/div/div[@class]/a/@href')
        #获取对应的频道名称
        names = html.xpath('//*[@id="root"]/main/section/div/div[2]/div[2]/div[2]/div/div[@class]/a/div[3]/div[1]/span/text()')

        print('获取所有请求的id')
        return (items,names)


    #获取到每个id对应的播放音频的URL
    def getSubRequestURL(self):
        print("开始获取到每个频道对应的播放音频的URL")
        #请求html界面信息
        sourceURL = 'https://www.ximalaya.com'
        #获取video音频列表url
        appendURL = 'https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}&sort=-1&pageSize=30'
        orignalIDs = self.getRequestURL()
        item_name_urls = {}
        names = orignalIDs[1]
        itemurls = orignalIDs[0]

        for index,value in enumerate(itemurls):
            #每次重新清空列表
            videourls = []
            requestURL = sourceURL + value
            result = requests.get(requestURL, headers=self.header)
            # 通过etree.HTML()方法转换为xml，xml用数据可以通过xpath() 表达式去获取数据
            html = etree.HTML(result.content)
            maxPageStr = html.xpath('//*[@id="root"]/main/section/div/div[2]/div[1]/div[2]/div[2]/div/nav/ul/li[last()-1]/a/span/text()')
            if len(maxPageStr):
                maxPage = int(maxPageStr[0])
            else:
                maxPage = 1

            #拼接URL获取video的目录页面url
            for page in range(1,maxPage+1):
                videourl = appendURL.format(value.split('/')[2:3][0],str(page))
                videourls.append(videourl)

            item_name_urls[names[index]] = videourls
        print("获取到每个频道对应的播放音频的URL")
        return item_name_urls


    # 根据url获取对应的video下载路径资源
    def getAllVideoRequest(self):
        print('开始获取对应的video下载路径资源')
        video_url_dict = self.getSubRequestURL()
        all_video_list = []
        for name,urls in video_url_dict.items():
            for url in urls:
                result = requests.get(url, headers=self.header)
                jsondata = result.content.decode('utf-8')
                info = json.loads(jsondata)
                audioData = info['data']['tracksAudioPlay']
                for value in audioData:
                    videolist = {}
                    videolist['itemname'] = name;
                    videolist['name'] = value['trackName']
                    videolist['src'] = value['src']
                    all_video_list.append(videolist)
        print('获取对应的video下载路径资源')
        print('文件个数:{}'.format(len(all_video_list)))
        return all_video_list;

    #保存到文档中
    def saveVideo(self,videos):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        # 存二十个文件就行，太多硬盘会爆
        for video in videos[0:20]:
            with open('{}.txt'.format(video['name']),'w+', encoding='utf-8') as f_obj:
                video_dict = str(video)
                f_obj.write(video_dict)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    #开始执行脚本
    def runScript(self):
        videos = self.getAllVideoRequest()
        self.saveVideo(videos)


if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    model = MaYaRequest('video')
    model.runScript()

