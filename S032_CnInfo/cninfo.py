# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : cninfo.py
@Project            : S032_CnInfo
@CreateTime         : 2023/3/14 17:16
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/14 17:16 
@Version            : 1.0
@Description        : None
"""
import requests
import execjs

url_web = "https://webapi.cninfo.com.cn/#/marketDataDate"

url = "https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007"
ctx = execjs.compile(open('json2csv_part.js', 'r', encoding='utf-8').read())

headers = {
    # 必须，"未经授权的访问,code:005"
    'Referer': 'https://webapi.cninfo.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    # 必须，"无授权访问，请联系apidata@cninfo.com.cn"
    'mcode': ctx.call('getMCode')
}


# 深圳证券交易所
# 上海证券交易所
# 香港联合交易所
# 郑州商品交易所
# 上海期货交易所
# 大连商品交易所
# 中国金融期货交易所
# Security 证券， Feature 期货 联合 Combine 商品 G
sites = {
    'shenzhenS': 'SZE',
    'shanghaiS': 'SHE',
    'hongkongC': 'HKG',
    'zhengzhouG': 'ZCE',
    'shanghaiF': 'SHFE',
    'dalianG': 'DCE',
    'china': 'CFFE'
}
transactionDate = "2023-03-13"
payload = {'tdate': transactionDate, 'market': sites['shenzhenS']}
resp = requests.post(url, headers=headers, data=payload)
print(resp.text)

records = resp.json()['records']
for idx, record in enumerate(records):
    print(idx, record)
