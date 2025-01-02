# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : beian.py
@Project            : S042_BeiAn
@CreateTime         : 2023/4/6 11:05
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/6 11:05 
@Version            : 1.0
@Description        : None
"""
import requests
import execjs
import re

url = "https://beian.miit.gov.cn"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

session = requests.Session()

# 首次请求会在响应头中包含1个 cookie，并在响应体中返回 index.js，其中包含生成第二个 cookie 的JS 代码
resp = session.get(url, headers=headers)

# 正则提取 JS 代码
regex = r"=(.*);location"
cookie = re.findall(regex, resp.text)[0]

# 调用 execjs，执行 JS 代码
cookie = execjs.eval(cookie)
# print(cookie)

# 添加这个新得到的 cookie，注意需要做2次切割
session.cookies["__jsl_clearance_s"] = cookie.split(';')[0].split('=')[1]
# print(session.cookies)

# 发起第二次请求，得到新的 JS 代码，这部分代码包含了生成新的 cookie 的功能
resp = session.get(url, headers=headers)
print(resp.text)

with open('app_src.js', 'w', encoding='utf-8') as f:
    f.write(resp.text)


