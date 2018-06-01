import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('Use-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('img src=')
    b = html.find(']',a)
    return html[a:b]


def find_img(page_url):
    html = url_open(page_url).decode('utf-8')
    print(html)
    img_address = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('.png',a,a+255)
        if b != -1:
            img_address.append(html[a+9:b+4])
        else:
            b = a + 9

        a = html.find('img src=',b)
    print("得到的数组== %s" %img_address)

    for each in img_address:
        print(each)

def save_image(folder,img_address):
    for each in folder:
        file_name = each.split('/')[-1]
        with open(file_name,'wb') as f:
            img = url_open(each)
            f.write(img)

def downloadimage(folder='ooxx',page=10):
    # name = os._exists(folder)
    # print(type(name))
    # if name:
    #     os.chdir(folder)
    # else:
    #     os.mkdir(folder)
    #     os.chdir(folder)

    url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0"
    images = find_img(url)


    # for i in images:
    #     # page_url = url + 'page-' + str(page_num) + '#comment'
    #     print(page_url)
    #     img_adress = find_img(i)
    #     save_image(folder,img_adress)

if __name__ == '__main__':
    downloadimage()