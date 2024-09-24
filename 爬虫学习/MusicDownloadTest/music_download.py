import requests
from selenium import webdriver
import time

def download(url):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    html = driver.page_source
    print(html)

    time.sleep(20)


if __name__ == "__main__":
    print("你好")
    download('https://music.163.com/#/playlist?id=2933222749')