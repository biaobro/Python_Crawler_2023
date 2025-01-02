# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : myria.py
@Project            : S041_Myria
@CreateTime         : 2023/4/5 11:20
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/5 11:20 
@Version            : 1.0
@Description        : None
"""
import requests

url = "https://myria.com/airdrop/?referCode=728977"

headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
'origin': 'https://myria.com',
'referer': 'https://myria.com/',
'x-api-key': 'dttd8biga8m5mxsuwddzzy6hjr2gx7zb8dntsg0iy02d2sqtjwsjhkgh2dsd24da',
}

wallet_address = "0x12BC003DBC3A8586fBf51D584Dce7bf56e97E22B"

url_users = "https://myriacore-api.myria.com/v1/users/" + wallet_address

session = requests.Session()
resp = session.get(url_users, headers=headers)
print(resp.text)

# Todo: 得到 x-api-key，在 _app.js 中提供，oe.PRODUCTION 属于固定值，不同环境，不同接口使用的 x-api-key 不同
# Todo: 得到 钱包ID，钱包ID也是固定的，只要插件登录就有，不需要点击页面上的 Connect。最早拿到 ID 的地方是在 inpage.js，在这个代码里叫 selectedAddress




