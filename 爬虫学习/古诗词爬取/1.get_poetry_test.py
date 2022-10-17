import pymysql
import requests
from bs4 import BeautifulSoup

from lxml import etree

base_url = "https://so.gushiwen.cn/"

header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }

conn = pymysql.connect(host='localhost',
                           user='root',
                           password='zj901203',
                           database='gushici_data',
                           port=3306,
                           charset='utf8',
                           # cursorclass 设置返回的格式为数组套字典，不设置返回的就是元组套元组
                           cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()  # 获取一个光标

def get_dynasty_type():
    """
    获取朝代分类
    :return:
    """
    result = requests.get(base_url + "authors/", headers=header)
    html = etree.HTML(result.content.decode('utf-8'))
    items = html.xpath('//*[@id="html"]/body/div[2]/div[1]/div[1]/div[2]/div[2]/a/text()')
    for item in items:
        get_peotriers_with_dynasty(item)

def get_peotriers_with_dynasty(dynasty):
    """
    根据朝代获取诗人
    :param dynasty:
    :return:
    """
    url = base_url + "authors/Default.aspx?c="+dynasty
    print(url)
    result = requests.get(base_url + "authors/Default.aspx?c="+dynasty, headers=header)
    html = etree.HTML(result.content.decode('utf-8'))
    items = html.xpath('//div[@class="divimg"]//a/@href')

    authors = []
    for item in items:
        author = get_all_author_info(item,dynasty)
        authors.append(author)

    cursor = conn.cursor()  # 获取一个光标
    sql = 'insert into Author(name,dynasty,author_desc) values(%s,%s,%s);'
    # 插入数据
    cursor.executemany(sql, authors)
    conn.commit()

    #获取当前人的所有作品



def get_all_author_info(url,dynasty):
    """
    根据名称获取当前诗人的具体信息
    :param name:
    :return:
    """
    result = requests.get(base_url + url, headers=header)
    html = etree.HTML(result.content.decode('utf-8'))
    #获取诗人信息进行保存
    name = html.xpath('//*[@id="sonsyuanwen"]/div[1]/h1/span[1]/b/text()')
    desc = html.xpath('//*[@id="sonsyuanwen"]/div[1]/p/text()')
    return (name[0], dynasty, desc[0])


def get_all_author_page():
    """
    获取所有诗人跳转链接
    :return:
    """
    result = requests.get(base_url+"shiwens/default.aspx",headers=header)
    html = etree.HTML(result.content.decode('utf-8'))
    #获取所有作者的跳转链接
    items = html.xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div[2]/a/@href")
    for item in items:
        #获取作者信息 保存
        get_poetry_content_info(item)



def close_data_base():
    conn.close()


def get_all_author_portry(name):
    """
    根据名称获取当前作者的所有诗词
    :param name:
    :return:
    """
    result = requests.get(base_url+"shiwens/default.aspx?astr="+name, headers=header)
    html = etree.HTML(result.content.decode('utf-8'))
    # 获取作者所有的著作的跳转链接
    items = html.xpath("/html/body/div[2]/div[1]/div[3]/div/span/a/@href")
    print(items)



def get_poetry_content_info(url):
    """
    根据url获取当前诗词的内容
    :param url:
    :return:
    """
    result = requests.get(base_url+url, headers=header)
    html = etree.HTML(result.content.decode('utf-8'))
    title = html.xpath("/html/body/div[2]/div[1]/div[2]/div[1]/h1/text()")
    content = html.xpath('//*[@id="contsonee16df5673bc"]/text()')
    if(len(content) > 0 and len(title) > 0):
        print(title[0] + ''.join(content))



if __name__ == '__main__':
    #保存数据
    # get_dynasty_type()
    get_peotriers_with_dynasty("先秦")

    # close_data_base()