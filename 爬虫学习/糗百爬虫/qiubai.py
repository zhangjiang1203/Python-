import requests
import re


# 配合正则表达式去获取糗百的显示内容，过滤元素
headers = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

}

res = requests.get('https://www.qiushibaike.com/',headers=headers)
result = res.content.decode('utf-8')
#
content = re.findall('<div class="content">.*?<span>(.*?)</span>.*?</div>', result,re.S)
print(type(content));
for value in content:
    print(value);


