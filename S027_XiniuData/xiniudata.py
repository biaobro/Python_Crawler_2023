# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : xiniudata.py
@Project            : S027_XiniuData
@CreateTime         : 2023/3/10 16:30
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/10 16:30 
@Version            : 1.0
@Description        : None
"""
import json
import requests
import execjs

session = requests.Session()

url_init = 'https://www.xiniudata.com/industry/newest?from=data'

# 服务端会返回1个 名为 btoken 的 cookie，后续请求中需要带上
# 所以这里使用了 session， 否则就得单独提取并添加进 headers
session.get(url_init)

js_python = execjs.compile(open('common.js', 'r').read())

url = "https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort"

headers = {
    # 这个 content-type 是必须的，否则拿到的返回不全
    'content-type': 'application/json',
    'origin': 'https://www.xiniudata.com',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

payload_src = {'sort': 1, 'start': 20, 'limit': 20}
encrypt_data = js_python.call('encrypt_payload', payload_src)
payload_dst = {
    'payload': encrypt_data['payload'],
    'sig': encrypt_data['sig'],
    'v': 1
}
payload = json.dumps(payload_dst, separators=(',', ':'))

resp = session.post(url, data=payload, headers=headers)
data = resp.json()['d']

decrypt_data = js_python.call('decrypt_response', data)
print(decrypt_data['list'])

for item in decrypt_data['list']:
    print(item['name'], item['event'])
