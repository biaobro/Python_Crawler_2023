# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 02_py_demo.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/23 13:24
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/23 13:24 
@Version            : 1.0
@Description        : None
"""

import execjs

with open('02_js_demo.js', mode='r', encoding='utf-8') as f:
    js = f.read()

JS = execjs.compile(js)

res = JS.call("func", 'BiaoBro')
print(res)
