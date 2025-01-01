# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : chinaindex.py
@Project            : S028_ChinaIndex
@CreateTime         : 2023/3/11 10:19
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/11 10:19 
@Version            : 1.0
@Description        : None
"""
import requests
from urllib.parse import urlencode
import execjs

js_ctx = execjs.compile(open('ctx.js', 'r', encoding='utf-8').read())

payload = {'channel': 'movielist'}
payload['sign'] = js_ctx.call('getSign', payload)

url = "https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank?" + urlencode(payload)

# 浏览器的Response Headers 里，是带cookie的，还有1个单独的 uuid
# 但是看起来不写也没问题
resp = requests.get(url)

print(resp.status_code)
dataEnc = resp.json()['data']
lastFetchTime = resp.json()['lastFetchTime']

dataDec = js_ctx.call('aseDecrypt', dataEnc, lastFetchTime)
print(dataDec)

