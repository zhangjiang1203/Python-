import requests

#执行API并相应存储
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
request = requests.get(url)
print("status code",request.status_code)
#将API响应存储在一个变量中
response_dict = request.json()

#处理结果
print(response_dict)