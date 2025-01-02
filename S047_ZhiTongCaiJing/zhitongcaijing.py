# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : zhitongcaijing.py
@Project            : S047_ZhiTongCaiJing
@CreateTime         : 2023/4/21 15:25
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/21 15:25 
@Version            : 1.0
@Description        : None
"""
import time
from urllib.parse import urlencode
import hashlib
import requests

url_page = "https://www.zhitongcaijing.com/immediately.html"
url_web = "https://www.zhitongcaijing.com"

# int(time.time()) 单位是 秒，30 是取当前时间倒数30s
ts = int(time.time()) - 30
data = {
    'last_update_time': ts,
    'platform': 'web',
    'roll': 'gt',
    'type': 'all',
}

sh = hashlib.sha1()
sh.update(urlencode(data).encode('utf-8'))
token = sh.hexdigest()
# print(token)

# data 和 payload 的顺序要固定，否则提示非法请求
# data 是在 JS 代码中做了排序的，我们在 Python 中直接将其写死
payload = {
    'type': 'all',
    'roll': 'gt',
    'token': token,
    'last_update_time': ts,
    'platform': 'web'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

url = url_web + "/immediately/content-list.html?" + urlencode(payload)
print(url)
resp = requests.get(url)
# print(resp.text)

datas = resp.json()['data']['list']

for data in datas:
    print(data)

