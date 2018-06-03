import urllib.request
import re


def addneihandata(url):
    header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36'}

    request = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(request)
    html = response.read().decode('gbk')
    return html

def inputmywantpage(page):
    url = 'http://www.neihanpa.com/article/list_5_' + str(page) + '.html'
    html = addneihandata(url)
    # 找到所有的段子内容<div class="f18 mb20"></div>
    #re.S 如果没有re.S 则只是匹配一行有没有符合规则的字符串，如果没有则下一行重新匹配
    #如果加上re.S 则是将所有的字符串将一个整体进行匹配
    pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)
    item_list = pattern.findall(html)
    dealneihandata(page,item_list)
    # return item_list

def dealneihandata(page,itemlist):
    print('********第 %d 页开始爬取********' % page)
    for item in itemlist:
        item = item.replace("<p>","").replace("</p>","").replace("<br />","")
        saveneihanduanzi(item)
    print('********第 %d 页爬取完毕********' % page)

def saveneihanduanzi(item):
    with open('myStory.txt','ab') as f:
        f.write(item.encode('gbk'))
        f.write(b'-----------------------------------------------------------------------------')

if __name__ == '__main__':
    print('''
    ==================
        内涵段子小爬虫
    ==================     
    ''')
    page = 0
    while page < 20:
        # page = input('请输入你要看的页数:')
        page += 1
        inputmywantpage(page)