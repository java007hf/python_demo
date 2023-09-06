import requests

target = "http://fanyi.baidu.com/"
req = requests.get(url = target)
req.encoding = 'utf-8'
print(req.text)

