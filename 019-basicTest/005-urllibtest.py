import urllib.request
import requests

response = urllib.request.urlopen("http://placekitten.com/g/500/600")
# 图片下载处理
print(response.geturl(),response.info())



cat_image = response.read()
with open('cate.jpg','wb') as f:
    f.write(cat_image)


