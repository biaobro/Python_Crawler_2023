# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : demo_002.py
@Project            : S046_JsRpc
@CreateTime         : 2023/4/18 15:09
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/18 15:09 
@Version            : 1.0
@Description        : 已验证
"""
import requests
import json

url = "http://localhost:12080/go"
data = {
    "group": "zzz",
    "name": "hlg",
    "action": "hello2",
    "param": "AAA"
}
print(data["param"])  # dumps后就是长这样的字符串{"user": "\u9ed1\u8138\u602a", "status": "\u597d\u56f0\u554a"}
res = requests.post(url, data=data)  # 这里换get也是可以的
print(res.text)


