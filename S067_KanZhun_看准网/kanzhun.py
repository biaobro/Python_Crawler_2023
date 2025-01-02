# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : kanzhun.py
@Project            : S067_KanZhun_看准网
@CreateTime         : 2023/6/17 10:41
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/6/17 10:41 
@Version            : 1.0
@Description        : None
"""
import requests
import execjs

ctx = execjs.compile(open('runtime.js', 'r', encoding='utf-8').read())

# 每个公司对应1个网页，网页有唯一id，可以在地址栏中找到
id = "0Xdz0ti1Fg~~"
kiv, b = ctx.call("encrypt", id)
params = {
    "kiv": kiv,
    "b": b
}
print(params)
headers = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

url = f"https://www.kanzhun.com/api_to/ci/stat.json?"

# 需要提供 headers，否则拿不到返回
resp = requests.get(url, params=params, headers=headers)
print(resp.text)

data = ctx.call("decrypt", resp.text, kiv)
print(data)
