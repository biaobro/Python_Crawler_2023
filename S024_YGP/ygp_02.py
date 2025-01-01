# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : ygp_02.py
@Project            : S024_YGP
@CreateTime         : 2023/3/8 23:03
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/8 23:03 
@Version            : 1.0
@Description        : None
"""
import json

import requests
import execjs

payload = {
    "type": "trading-type",
    "publishStartTime": "",
    "publishEndTime": "",
    "siteCode": "44",
    "secondType": "A",
    "projectType": "",
    "thirdType": "",
    "dateType": "",
    "total": 0,
    "pageNo": 1,
    "pageSize": 10,
    "openConvert": False
}

js_code = open('index.aa.js', 'r', encoding='utf-8').read()
data = execjs.compile(js_code).call('hash256', payload)

headers = {
    'Content-Type': 'application/json',
    'Host': 'ygp.gdzwfw.gov.cn',
    'Origin': 'https://ygp.gdzwfw.gov.cn',
    'Referer': 'https://ygp.gdzwfw.gov.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Dgi-Req-App': data['App'],
    'X-Dgi-Req-Nonce': data['Nonce'],
    'X-Dgi-Req-Signature': data['Signature'],
    'X-Dgi-Req-Timestamp': str(data['Timestamp'])
}
print(headers)

uuids = execjs.compile(js_code).call('generate_cookies')
cookies = {
    '_horizon_sid': uuids['sid'],
    '_horizon_uid': uuids['uid'],
}
print(cookies)

url_data = "https://ygp.gdzwfw.gov.cn/ggzy-portal/search/v1/items"
resp = requests.post(
    url_data,
    headers=headers,

    # 这里也要记得将 字典格式转换成 json 字符串，不要空格美化
    data=json.dumps(payload, separators=(',', ':')),
    cookies=cookies)
print(resp.text)

