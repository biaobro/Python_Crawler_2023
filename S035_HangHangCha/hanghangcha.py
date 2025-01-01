# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : hanghangcha.py
@Project            : S035_HangHangCha
@CreateTime         : 2023/3/15 16:12
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/15 16:12 
@Version            : 1.0
@Description        : None
"""
import csv
import json

import requests
from urllib.parse import urlencode, quote
from utils import flat_dict
import execjs

url_web = "https://www.hanghangcha.com/products-local"

params = {
    'filter': {
        "city": "",
        "lv": "null",
        "province": "",
        "userId": 3042387,
        "companyId": "null",
        "limit": 20,
        "skip": 0,
        "keyword": "null",
        "companyType": "local"
    }
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Cookie': 'UM_distinctid=186e4553b794d5-07004a9c96a919-26031851-144000-186e4553b7a5d0; Hm_lvt_1521e0fb49013136e79181f2888214a7=1678868044; Hm_lpvt_1521e0fb49013136e79181f2888214a7=1678868044; JSESSIONID=028D54F8E32A3F9D165E73C92189F913; WX_OPEN=fM4grYo2Anyzq+I1BkCitQJCYCSa/hgYcXb4d9Z0GttH+0obCpmXL7hsnqmDQdCiW4/+OjGS6L44Sl8/KpGzeUTbLH6PDreA25rPRLDlSriBRk9hYiyhZFxdyZV0ZC3d; _ACCOUNT_=NjY2MzE0MjdmZTI3NGI1OTliYTNkODg1OWJmOWQwNGQlNDAlNDBtb2JpbGU6MTY4MDA3NzY2NDEwMzowYjVjMWViMmQ3ZGNlOTg2MGMyN2U0NTBjZDM3MjcyNQ'
}

# urlencode 只能处理1维字典，对于2维字典，需要先将其打扁
url_req = "https://api.hanghangcha.com/hhc/invest/getProduct?filter=%7B%22city%22%3A%22%22%2C%22lv%22%3Anull%2C%22province%22%3A%22%22%2C%22userId%22%3A3042387%2C%22companyId%22%3Anull%2C%22limit%22%3A20%2C%22skip%22%3A0%2C%22keyword%22%3Anull%2C%22companyType%22%3A%22local%22%7D"
print(url_req)

resp = requests.get(url_req, headers=headers)
# print(resp.text)
decrypt_str = resp.json()['data']

ctx = execjs.compile(open('app.js', 'r', encoding='utf-8').read())
decrypt_data = ctx.call('decrypt', decrypt_str)
# print(decrypt_data)

records = decrypt_data['data']['data']

csvHeaders = ['company_type', 'financing_date', 'competitor_id', 'core_personnel', 'hhcTags', 'investors',
              'hhc_province', 'hhc_one_tag_name', 'hhc_round', 'product_id', 'hhc_tags', 'logo', 'competitor_list',
              'hasStore', 'hhc_city', 'stock_code', 'start_date', 'timestamp', 'brief', 'area', 'website', 'amount',
              'company_id', 'business', 'hhc_tags_name', 'product_name', 'province_name', 'tags', 'investor', 'round',
              'hhc_tag_length', 'company_name']

# newline是数据之间不加空行
with open('data.csv', 'w', newline='', encoding='utf-8-sig') as f:
    # 提前预览列名，当下面代码写入数据时，会将其一一对应。
    writer = csv.DictWriter(f, fieldnames=csvHeaders)

    # 写入列名
    writer.writeheader()

    # 写入数据，因为用了 DictWriter，所以可以直接把 字典列表 写入 csv
    writer.writerows(records)

for record in records:
    print(record)
