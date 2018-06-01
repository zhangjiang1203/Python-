import urllib.request

url = 'http://www.ip138.com'
proxy_support = urllib.request.ProxyHandler({'http':'119.6.144.73:81'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent',"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"
)]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
print("hahahah")