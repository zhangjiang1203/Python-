import requests
from bs4 import BeautifulSoup
import sys

def getPygerCode(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    req = requests.get(url, headers=header)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    imgStr = soup.find_all('img',class_='qrcode')[0]
    real = imgStr.attrs["src"]
    codeStr = '''<img src=%s width="120px" height="120px" />''' %real
    print("real src =%s" %codeStr)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[0]
        print("当前url===%s" %url)
        getPygerCode("https://www.pgyer.com/WH2g")
    else:
        print("python 参数输入不合法")

