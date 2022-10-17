import pymysql
import requests
from bs4 import BeautifulSoup
import time
from lxml import etree

base_url = "https://so.gushiwen.cn"

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
    start_time = time.time()
    # dynasty_list = ['先秦','两汉','魏晋','南北朝','隋代','唐代','五代','宋代','金朝','元代','明代','清代']
    dynasty_list = ['魏晋','南北朝','隋代','唐代','五代','宋代','金朝','元代','明代','清代']

    for item in dynasty_list:
        get_peotriers_with_dynasty(item)

    end_time = time.time()
    print("总耗时 %s" %(end_time - start_time))


def get_peotriers_with_dynasty(dynasty):
    """
    根据朝代获取诗人
    :param dynasty:
    :return:
    """
    url = base_url + "/authors/Default.aspx?c="+dynasty

    for i in range(1,100):
        if i == 1:
            continue
        orignal_url = url + '&p=' + str(i)
        result = requests.get(orignal_url, headers=header)
        html = etree.HTML(result.content.decode('utf-8'))
        items = html.xpath('//div[@class="divimg"]//a/@href')
        if len(items) == 0: break

        authors = []
        for item in items:
            author = get_all_author_info(item,dynasty)
            if author[0] is not None:
                authors.append(author)
        try:
            sql = 'insert into Author(name,dynasty,author_desc,avator_img) values(%s,%s,%s,%s);'
            # 插入数据
            cursor.executemany(sql, authors)
            conn.commit()
        except:
            print("插入诗人出错==%s" %(authors))

        #获取当前人的所有作品
        for author in authors:
            # 获取当前作者的数据库索引
            sql = 'select id from Author where name = %s';
            cursor.execute(sql,author[0])
            result = cursor.fetchall()
            # result 是一个字典数组
            author_id = result[0]["id"]
            author_name = author[0]
            if author_name != "刘向" and  author_name != "阮籍":
                get_all_author_portry(author[0],author_id)


def get_all_author_info(url,dynasty):
    """
    根据url获取当前诗人的具体信息
    :param name:
    :return:
    """
    original_url = base_url + url
    result = requests.get(base_url + url, headers=header)
    html = etree.HTML(result.content.decode('utf-8'))
    try:
        # 获取诗人信息进行保存
        name = html.xpath('//*[@id="sonsyuanwen"]/div[1]/h1/span[1]/b/text()')
        desc = html.xpath('//*[@id="sonsyuanwen"]/div[1]/p/text()')
        avator = html.xpath('//*[@id="sonsyuanwen"]/div[1]/div/img/@src')
        # print("诗人头像===%s" %avator)
        return (name[0], dynasty, desc[0], avator)
    except:
        print("get_all_author_info解析出错==%s" %original_url)




def get_all_author_portry(name,author_id):
    """
    根据名称获取当前作者的所有诗词
    :param name:
    :return:
    """
    orignal_url = base_url+"/shiwens/default.aspx?astr="+name
    tem_url = ""
    for i in range(1,100):
        tem_url = orignal_url + '&page=' + str(i)
        result = requests.get(tem_url, headers=header)
        html = etree.HTML(result.text)
        try:
            items = html.xpath("/html/body/div[2]/div[1]/div[3]/div/span/a/@href")
            # # 获取作者所有的著作的跳转链接
            if len(items) == 0:
                break

            for item in items:
                get_poetry_content_info(item, author_id)
        except:
            print("get_all_author_portry error==%s" %tem_url)
            break

def get_poetry_content_info(url,author_id):
    """
    根据url获取当前诗词的内容
    :param url:
    :return:
    """
    original_url = base_url + url
    result = requests.get(original_url, headers=header)

    soup = BeautifulSoup(result.content.decode("utf-8"), 'lxml')
    #查找name content desc
    title = soup.select("#sonsyuanwen > .cont > h1")[0].text
    content = soup.select("#sonsyuanwen > .cont > .contson")[0].text
    comment = soup.select(".contyishang > p")
    if len(comment) > 0:
        comment = comment[0].text
    else:
        comment = ""

    # 插入数据
    try:
        sql = 'insert into Poetry(title,content,comment,author_id) values(%s,%s,%s,%s);'
        cursor.execute(sql, (title,content,comment,author_id))
        conn.commit()
        print("insert Poetry success %s ,title:%s" %(original_url,title))

    except:
        print("insert Poetry error %s ,title:%s,content:%s.comment:%s,author_id:%s" %(original_url,title,content,comment,author_id))

    # return (title,content,comment)


def close_data_base():
    conn.close()

if __name__ == '__main__':
    #保存数据
    get_dynasty_type()
    # get_all_author_portry("陆机",441)
    # get_poetry_content_info('/shiwenv_016ce61dae11.aspx')


    close_data_base()