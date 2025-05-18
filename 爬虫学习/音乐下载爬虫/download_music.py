from time import sleep

import requests
from lxml import etree
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import pyperclip

base_url = "http://www.78497.com"
header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "cookie": "Hm_lvt_b54537254b1d49f62dd4d64991d870e3=1745496424; HMACCOUNT=C602AE6C30E7AEDE; Hm_tf_9ruco3wpq6b=1745496424; Hm_lvt_9ruco3wpq6b=1745496424; mode=1; songIndex=0; coin_screen=1512*982; 0fcea1373cf3b3e155d918d2a7a61217=9f0c11b127029f6e1dcf280297c13fd0; down_mima=ok; Hm_lpvt_9ruco3wpq6b=1745497281; Hm_lpvt_b54537254b1d49f62dd4d64991d870e3=1745497282"
}

chrome_options = Options()
# 禁用下载保护，允许下载所有类型的内容
chrome_options.add_experimental_option("prefs", {"download_restrictions": 0})
chrome_options.add_experimental_option("prefs", {"safebrowsing.enabled": False})

# 配置文件下载路径
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/path/to/download/directory",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False
})

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(width=1000, height=800)
# 模拟右键点击
actions = ActionChains(driver)


def get_music_detail_page():

    rank_url = "http://www.78497.com/list/hktop.html"

    request = requests.get(url=rank_url, headers=header)
    # html = etree.HTML(request.content.decode('utf-8'))
    tree = etree.HTML(request.content.decode('utf-8'))
    # data = tree.xpath("//div[@class='list_r'][last()]/div/a[@target='_mp3']/@href")
    data = tree.xpath("//div[@class='list_r']/div/a[@target='_mp3']/@href")

    # title = tree.xpath("//div[@class='list_r'][last()]/div/a[@target='_mp3']/text()")

    print(f"获取的歌词数据=={data}")

    num = 0
    for i in range(len(data)):
        music_url = data[i]
        song_url = music_url.split("/")[-1].replace(".html","")
        download_url = base_url + "/down.php?ac=music&id=" + song_url
        #print(f"文件下载地址==={download_url}")
        num += 1
        try:
            # 拼接下载地址，执行下载逻辑
            driver.get(download_url)
            try:
                element = driver.find_element(By.XPATH,
                                              '//input[@type="text" and @name="lkpwd" and contains(@class, "layui-input")]')
                element.send_keys("5312")
                print("存在该输入框")

                button = driver.find_element(By.XPATH,
                                             '//button[contains(@class, "layui-btn") and contains(@class, "copy") and contains(text(),"提交口令")]')
                # 存在则点击
                button.click()
            except:
                print("不存在该输入框")

            sleep(3)
            # 查找输入框
            download_title = driver.find_element(by=By.XPATH, value='//a[@id="btn-download-mp3"]')
            download_name = download_title.get_attribute("download").replace(".mp3", "")
            # 等待网页加载完成
            sleep(3)
            # 双击 下载按钮
            download_mp3 = driver.find_element(By.XPATH, '//*[@id="btn-download-mp3"]')
            actions.context_click(download_mp3).perform()
            # 右键菜单弹出
            sleep(2)
            # 等待右键菜单弹出
            music_action(download_name,True)

            sleep(3)
            # 下载歌词
            download_lrc_content = driver.find_element(By.XPATH, '//*[@id="btn-download-lrc"]')
            actions.context_click(download_lrc_content).perform()
            # 右键菜单弹出
            sleep(2)
            # 等待右键菜单弹出
            # 歌词格式特殊处理替换之前的.mp3
            music_action(download_name)

            # 下载歌曲时间
            time.sleep(5)  # 等待3秒
            print(f"{download_name}, download complete, 还剩 {len(data) - num}待下载")
        except Exception as e:
            print(f'发生错误:{e}')
            time.sleep(2)


        finally:
            time.sleep(2)
            print(f'执行完成')

    print(f'任务全部执行完成，共下载{len(data)}')

    driver.quit()


# 弹出右键菜单之后 的操作
def music_action(name, is_music: bool = False):
    # 用 PyAutoGUI 模拟键盘操作（假设“另存为”是下箭头两次，然后回车）
    pyautogui.press('down', presses=4)
    sleep(1)
    pyautogui.press('enter')
    # 等待另存为弹窗
    sleep(2)

    pyperclip.copy(name)
    sleep(0.5)
    # 复制粘贴
    pyautogui.hotkey('command', 'v')  # 粘贴
    sleep(0.5)
    pyautogui.press('enter')  # 回车

    # if is_music:
    #     # 防止出现 mp3 和 acc格式选择的弹窗 直接选择其中一个
    #     sleep(0.5)
    #     pyautogui.press('enter')

    sleep(1)


if __name__ == '__main__':
    get_music_detail_page()
