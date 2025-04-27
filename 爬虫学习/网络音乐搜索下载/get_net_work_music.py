from bs4 import BeautifulSoup
from selenium import webdriver
import requests
# from selenium.webdriver
from lxml import etree
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

# base_url = "https://www.myfreemp3.com.cn/?page=audioPage&type=netease&name="
base_url = "https://www.toomic.com/searchr/?token=9eyJFSUQiOiI4MDQ1NjMxNyIsIk5hbWUiOiJcdTY2NzRcdTU5MjkiLCJUYWciOiJcdTU0NjhcdTY3NzBcdTRmMjYiLCJJbWciOiIzMjRcLzM0XC8xNFwvMzYzMzIyOTE5Mi5qcGciLCJUeXBlIjoia3ciLCJWaXAiOiIxIn0%3D"

def searchMusic(author, name):
    # 歌曲名称
    print("搜索歌曲==作者:%s,名称:%s", author, name)

    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.get(base_url)

    # 根据id 进行查找
    # download = browser.find_element(by=By.CLASS_NAME,value="aplayer-list-download")
    # download.click()

    # inputField = browser.find_element(by=By.ID, value="input")
    # inputField.clear()
    # inputField.send_keys(name)

    # input.clear()
    # input.send_keys(name + " " + author)
    # # browser.find_element(by=By.ID, value="j-submit").click()
    #
    # input.send_keys(Keys.ENTER)
    #
    # # 右键另存为
    # music = browser.find_element(by=By.ID,value="j-src-btn")
    #
    # action = ActionChains(browser).move_to_element(music)  # 移动到该元素
    # action.context_click(music)
    # action.perform()

    # 找到 链接另存为
    # save_as_option = browser.find_element(By.LINK_TEXT, "链接存储为…")
    # save_action = ActionChains(browser).move_to_element(save_as_option).context_click(save_as_option)

    # save_action.perform()

    #模拟右键另存为


    print("执行完成")

    time.sleep(30)


if __name__ == "__main__":
    searchMusic("张学友", "偷心")
