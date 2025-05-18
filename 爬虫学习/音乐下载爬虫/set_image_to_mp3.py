import requests
import os
import time
from lxml import etree

from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3
from selenium import webdriver
from selenium.webdriver.common.by import By

from urllib.parse import urlencode

base_url = "http://www.78497.com/so.php?"
header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "cookie": "Hm_lvt_b54537254b1d49f62dd4d64991d870e3=1745496424; HMACCOUNT=C602AE6C30E7AEDE; Hm_tf_9ruco3wpq6b=1745496424; Hm_lvt_9ruco3wpq6b=1745496424; mode=1; songIndex=0; coin_screen=1512*982; 0fcea1373cf3b3e155d918d2a7a61217=9f0c11b127029f6e1dcf280297c13fd0; down_mima=ok; Hm_lpvt_9ruco3wpq6b=1745497281; Hm_lpvt_b54537254b1d49f62dd4d64991d870e3=1745497282"
}
#
# driver = webdriver.Chrome()
# driver.set_window_size(width=1000, height=800)


def get_all_mp3_data():
    # 获取MP3列表展示页数据
    music_path = "/Users/zhangjiang/Desktop/2023年1月榜单歌曲/"


    for filename in os.listdir(music_path):
        if filename.lower().endswith('.mp3'):
            print(f"{filename} 是 mp3 文件")
            filename = filename.replace(".mp3","")
            params = {
                "wd": filename
            }
            full_url = base_url + urlencode(params)
            print(full_url)

            #下载图片
            request = requests.get(url=full_url, headers=header)
            tree = etree.HTML(request.content.decode('utf-8'))
            data = tree.xpath("//div[@class='pic']/a/img/@src")
            print(data)
            if len(data) > 0:
                img_path = data[0]
                time.sleep(2)
                response = requests.get(img_path)
                img_data = response.content

                # 如果没有ID3标签则添加
                audio = MP3(music_path+filename+'.mp3', ID3=ID3)
                try:
                    audio.add_tags()
                except error:
                    pass

                audio.tags.add(
                    APIC(
                        encoding=3,  # 3为utf-8
                        mime='image/jpeg',  # 如果是png图片请改为'image/png'
                        type=3,  # 3为封面(front cover)
                        desc='Cover',
                        data=img_data
                    )
                )
                audio.save()
                print(f"{filename}==网络图片已成功写入MP3文件！")



if __name__ == "__main__":
    get_all_mp3_data()