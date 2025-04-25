from time import sleep

import requests
from lxml import etree
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

from 爬虫学习.MusicDownloadTest.music_download import download
# <a id="btn-download-mp3" download="孙燕姿 - 开始懂了[www.78497.com].mp3" target="_blank" href="/plug/down.php?ac=music&amp;id=93f260998a10f4ad6b46606af5c8ec72"><i class="fa fa-download" aria-hidden="true"></i> MP3下载</a>
# 根据A标签中的内容 自动下载文件
# //歌曲下载地址
# http://wwww.78497.com/plug/down.php?ac=music&amp;id=93f260998a10f4ad6b46606af5c8ec72
# https://lv.sycdn.kuwo.cn/baa31aa6a051767a48f00eb53d99a86f/680b907d/resource/30106/trackmedia/M800001tr7t43Ry7GG.mp3
# /// 歌词地址
# http://www.78497.com/plug/down.php?ac=lrc&id=93f260998a10f4ad6b46606af5c8ec72
# <a id="btn-download-mp3" download="孙燕姿 - 开始懂了[www.78497.com].mp3" target="_blank" href="/plug/down.php?ac=music&amp;id=93f260998a10f4ad6b46606af5c8ec72"><i class="fa fa-download" aria-hidden="true"></i> MP3下载</a>
# <a id="btn-download-mp3" download="孙燕姿 - 开始懂了[www.78497.com].mp3" target="_blank" href="/plug/down.php?ac=music&amp;id=93f260998a10f4ad6b46606af5c8ec72"><i class="fa fa-download" aria-hidden="true"></i> MP3下载</a>
# /// 歌曲地址
# http://lv.sycdn.kuwo.cn/baa31aa6a051767a48f00eb53d99a86f/680b907d/resource/30106/trackmedia/M800001tr7t43Ry7GG.mp3

base_url = "http://www.78497.com/"
header = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "cookie":"Hm_lvt_b54537254b1d49f62dd4d64991d870e3=1745496424; HMACCOUNT=C602AE6C30E7AEDE; Hm_tf_9ruco3wpq6b=1745496424; Hm_lvt_9ruco3wpq6b=1745496424; mode=1; songIndex=0; coin_screen=1512*982; 0fcea1373cf3b3e155d918d2a7a61217=9f0c11b127029f6e1dcf280297c13fd0; down_mima=ok; Hm_lpvt_9ruco3wpq6b=1745497281; Hm_lpvt_b54537254b1d49f62dd4d64991d870e3=1745497282"
}
driver = webdriver.Chrome()
driver.set_window_size(width=600,height=700)
def get_music_detail_page():
    # request = requests.get(url=base_url, headers=header)
    # # html = etree.HTML(request.content.decode('utf-8'))
    # tree = etree.HTML(request.content.decode('utf-8'))
    # data = tree.xpath('//div[@class="song"]/div/a/@href')
    # title = tree.xpath('//div[@class="song"]/div/a/text()')
    #
    # print(request.text)
    # # print(html)
    # print(data)
    # print(title)

    try:
        # driver.get("http://www.78497.com/mp3/93f260998a10f4ad6b46606af5c8ec72.html")  # 打开百度浏览器
        driver.get("http://www.78497.com/down.php?ac=music&id=93f260998a10f4ad6b46606af5c8ec72")
        # 等待网页加载完成
        sleep(2)
        # 找到指定按钮
        # download = driver.find_element(By.XPATH,'//*[@class="bt"]')
        # # print(download)
        # download.click()
        # sleep(3)
        download_mp3 = driver.find_element(By.XPATH,'//*[@id="btn-download-mp3"]')
        # download_mp3.click()
        # 模拟右键点击
        actions = ActionChains(driver)
        actions.context_click(download_mp3).perform() #send_keys(Keys.ARROW_DOWN).perform()
        # # 等待右键菜单弹出
        sleep(2)
        #
        # 执行方向键操作，例如向下箭头
        actions.send_keys(Keys.ARROW_DOWN).perform()
        # 也可以继续执行其他方向键操作，例如向上箭头
        actions.send_keys(Keys.ARROW_DOWN).perform()
        # 按回车键选择菜单项
        actions.send_keys(Keys.RETURN).perform()


        # for i in range(4):
        #     pyautogui.press("down")
        # # # 按下回车键确认
        # pyautogui.press('enter')
        # # 等待保存回话框弹出
        time.sleep(10)  # 等待3秒


        print("指定文件名")
    except Exception as e:
        print(f'发生错误:{e}')

    finally:
        driver.quit()
        print(f'执行完成')


if __name__ == '__main__':
    get_music_detail_page()