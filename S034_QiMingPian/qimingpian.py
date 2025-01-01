# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : qimingpian.py
@Project            : S034_QiMingPian
@CreateTime         : 2023/3/15 14:41
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/15 14:41 
@Version            : 1.0
@Description        : None
"""
import requests
import execjs

url_web = "https://www.qimingpian.com/finosda/project/pinvestment"
ctx = execjs.compile(open('app.js', 'r', encoding='utf-8').read())
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}


def get_single_page(page):
    # 登录状态下的请求中，会填充 unionid
    payload = {
        'time_interval': '',
        'tag': '',
        'tag_type': '',
        'province': '',
        'lunci': '',
        'page': str(page),
        'num': '20',
        'unionid': '1AR3NXS808A11vNct7yhWGZErxmwJ4bV8mOfQ4nxSIOGFvLCW1VGcykxCM/XgkQTeJWqqIs6kiQsM8IbOYgM5A=='
    }

    url_req = "https://vipapi.qimingpian.cn/DataList/productListVip"

    resp = requests.post(url_req, headers=headers, data=payload)
    # print(resp.text)

    encrypt_data = resp.json()['encrypt_data']

    decrypt_data = ctx.call('decrypt', encrypt_data)
    records = decrypt_data['list']
    for record in records:
        print(record['product'], record['hangye1'], record['yewu'],
              record['province'], record['lunci'], record['jieduan'], record['money'],
              record['time'], record['investor_info'])


for i in range(1, 3):
    get_single_page(str(i))
