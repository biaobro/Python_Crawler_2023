# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : fujian_gov.py
@Project            : S036_FuJian_GOV
@CreateTime         : 2023/3/15 22:29
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/15 22:29 
@Version            : 1.0
@Description        : None
"""
import json
import time
import requests
import execjs

ctx = execjs.compile(open('app.js', 'r', encoding='utf-8').read())

url_web = 'https://ggzyfw.fj.gov.cn/business/list/'

payload = {
    "pageNo": 1,
    "pageSize": 20,
    "total": 0,
    "AREACODE": "",
    "M_PROJECT_TYPE": "",
    "KIND": "GCJS",
    "GGTYPE": "1",
    "PROTYPE": "",
    "timeType": "6",
    "BeginTime": "2022-09-15 00:00:00",
    "EndTime": "2023-03-15 23:59:59",
    "createTime": [],
    "ts": int(time.time() * 1000)
}

sign = ctx.call('getSign', payload)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'portal-sign': sign,

    # 这个 Content-Type 必须，否则返回的数据不准确，包含了其他类型的 GGTYPE
    'Content-Type': 'application/json;charset=UTF-8'
}

url_req = 'https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo'
resp = requests.post(url_req, headers=headers, data=json.dumps(payload, separators=(',', ':')))
# print(resp.text)

encrypt_data = resp.json()['Data']
decrypt_data = ctx.call('decrypt', encrypt_data)
# print(decrypt_data)

records = decrypt_data['Table']
for record in records:
    print(record)
