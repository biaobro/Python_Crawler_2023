# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : bitcoin.py
@Project            : S033_Bitcoin
@CreateTime         : 2023/3/14 22:07
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/14 22:07 
@Version            : 1.0
@Description        : None
"""
import csv
import json

import requests
import time
from urllib.parse import urlencode
import uuid
import execjs

url_web = "https://www.oklink.com/cn/btc/tx-list"
session = requests.Session()

# get cookies from server
session.get(url_web)

payload = {
    't': str(int(time.time()) * 1000),
    'offset': '0',
    'limit': '20',
    'sort': ''
}

url = "https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict?" + urlencode(payload)

ctx = execjs.compile(open('index.js', 'r', encoding='utf-8').read())
apikey = ctx.call('getApiKey')

headers = {
    # 'devid' : # 这个值看起来就是 uuid，经过测试也能确认。最后发现不写也没关系
    'referer': 'https://www.oklink.com/cn/btc/tx-list',
    'x-apikey': apikey,
    'x-cdn': 'https://static.oklink.com',
    'x-utc': '8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

resp = session.get(url, headers=headers)

json_data = resp.json()
total = json_data['data']['total']

# hits 是个 字典列表
hits = json_data['data']['hits']

csvHeaders = ['idx', 'hash', 'blockHeight', 'blocktime', 'inputsCount', 'inputsValue', 'outputsCount', 'outputsValue',
              'fee', 'realTransferValue', 'index', 'blockHash', 'coinbase', 'size', 'version', 'doubleSpend',
              'inputsValueSat', 'outputsValueSat', 'inputs', 'outputs', 'lockTime', 'coindaysDestroyed', 'sigops',
              'coinString', 'strippedSize', 'virtualSize', 'weight', 'hasWitness', 'witnessHash', 'feePerKwu',
              'feePerKvbyte', 'confirm', 'allAddressList']

# newline是数据之间不加空行
with open('data.csv', 'w', newline='', encoding='utf-8-sig') as f:
    # 提前预览列名，当下面代码写入数据时，会将其一一对应。
    writer = csv.DictWriter(f, fieldnames=csvHeaders)

    # 写入列名
    writer.writeheader()

    # 写入数据，因为用了 DictWriter，所以可以直接把 字典列表写入 csv
    writer.writerows(hits)

    for idx, hit in enumerate(hits):
        # hit 是字典
        print(idx, hit)
        break
