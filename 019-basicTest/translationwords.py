import urllib.request
import urllib.parse
import requests
import json

URL= "http://i.jandan.net/ooxx"

url = "http://www.baidu.com"
data = {}

header = {}
header['content-type'] = 'application/json'
header['User-Agent'] = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36'#
# data["i"] =  "我就是我"
# data["type"] = "AUTO"
# data["doctype"] =  "json"
# data["xmlVersion"] =  "1.6"
# data["keyfrom"] =  "fanyi.web"
# data["action"] = "FY_BY_CLICKBUTTION"
# data["typoResult"] = "true"
# data["ue"] = "UTF-8"



# data = urllib.parse.urlencode(data).encode('utf-8')
# req = urllib.request.Request(URL,data)
# req.add_header('User-Agent',"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36")
# response = urllib.request.urlopen(URL)
# response = requests.get(URL,header)
# html = response.status_code
#
# print(response.content.decode('utf-8'))

req = urllib.request.Request(url)
req.add_header('Use-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36')
response = urllib.request.urlopen(URL)
html = response.read().decode('utf-8')
print(html)