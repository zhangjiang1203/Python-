import urllib.request
import sys



# response = urllib.request.urlopen('https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=0')
# html = response.read().decode('utf-8')
# print(html)

# 添加请求的网络地址
def addRequestURL(url):

    header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36'}
    request = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(request)
    html = response.read()
    # 存储文件
    return html

    # 存储文件


def saveMyHTML(filename , html):
    print(filename)
    with open(filename, 'wb+') as f:

        f.write(html)

def dealmyurl(startpage,endpage):
    url = 'https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn='

    for i in range(startpage,endpage+1):
        pn = 50 * i ;
        html = addRequestURL(url+str(pn))

        file_name = 'test'+str(i) + '.html'
        saveMyHTML(file_name , html)


if __name__ == '__main__':
    while True:
        # url = input('请输入网址:')
        startpage = input('开始页面:')
        endpage = input('结束界面:')

        if startpage == 'q':
            break

        if endpage == 'q':
            break

        dealmyurl(int(startpage), int(endpage))




