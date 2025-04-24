
import requests
from lxml import etree



base_url = "http://www.78497.com/"
header = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "cookie":"Hm_lvt_b54537254b1d49f62dd4d64991d870e3=1745496424; HMACCOUNT=C602AE6C30E7AEDE; Hm_tf_9ruco3wpq6b=1745496424; Hm_lvt_9ruco3wpq6b=1745496424; mode=1; songIndex=0; coin_screen=1512*982; 0fcea1373cf3b3e155d918d2a7a61217=9f0c11b127029f6e1dcf280297c13fd0; down_mima=ok; Hm_lpvt_9ruco3wpq6b=1745497281; Hm_lpvt_b54537254b1d49f62dd4d64991d870e3=1745497282"
}


def get_music_detail_page():
    request = requests.get(url=base_url, headers=header)
    # html = etree.HTML(request.content.decode('utf-8'))
    tree = etree.HTML(request.content.decode('utf-8'))
    data = tree.xpath('//div[@class="song"]/div/a/@href')
    title = tree.xpath('//div[@class="song"]/div/a/text()')

    print(request.text)
    # print(html)
    print(data)
    print(title)



if __name__ == '__main__':
    get_music_detail_page()