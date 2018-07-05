import requests
import json
from lxml import etree
import re

# headers = {
# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
# }
#
# # 初始化请求URL
# orignalURL = 'https://www.ximalaya.com/shangye/top/'
# orignalRes = requests.get(orignalURL,headers=headers)
# # 通过etree.HTML()方法转换为xml，xml用数据可以通过xpath()表达式去获取数据
# html = etree.HTML(orignalRes.content)
# # 添加Xpath路径过滤
# result = html.xpath('//*[@id="root"]/main/section/div/div[2]/div[2]/div[2]/div/div[3]/a/@href')
# print(result)



# url = 'https://www.ximalaya.com/revision/album?albumId=269179&pageNum=1&sort=-1&pageSize=30'

# result = requests.get(url,headers=headers)
# jsondata = result.content.decode()
# info = json.loads(jsondata)
# audioData = info['data']['tracksInfo']['tracks']
# for value in audioData:
#     print(value)

#定义类去获取数据
class RequestData:
    def __init__(self,name):
        self.name = name
        self.header = {
             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        self.start_url =  'https://www.ximalaya.com/revision/play/album?albumId=269179&pageNum={}&sort=-1&pageSize=30'
        self.book_url = []#'https://www.ximalaya.com/shangye/top/'
        for i in range(1):
            url = self.start_url.format(i+1)
            self.book_url.append(url)

    def get_book_url(self):
        all_video_list = []
        for url in self.book_url:
            result = requests.get(url,headers=self.header)
            jsondata = result.content.decode()
            info = json.loads(jsondata)
            audioData = info['data']['tracksAudioPlay']
            for value in audioData:
                videolist = {}
                videolist['name'] = value['trackName']
                videolist['src'] = value['src']
                all_video_list.append(videolist)
        return  all_video_list

    def save(self,books):
        #遍历每一个音频 下载保存
        for book in books:
            print(book)
            #去除双引号
            book['name'] = re.sub('"',"",book['name'])
            with open('video/{}.m4a'.format(self.name+'-'+book['name']),'ab') as f:
                r = requests.get(book['src'],headers=self.header)
                result = r.content
                f.write(result)


    def run(self):
        all_list = self.get_book_url()
        self.save(all_list)

if __name__ == '__main__':
    request = RequestData('吴晓波频道')
    request.run()