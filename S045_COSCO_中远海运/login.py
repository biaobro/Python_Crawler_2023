# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : login.py
@Project            : S045_COSCO_中远海运
@CreateTime         : 2023/4/15 10:48
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/15 10:48 
@Version            : 1.0
@Description        : None
"""
import requests
import execjs

url = "https://synconhub.coscoshipping.com/"

ctx = execjs.compile(open('index.js','r',encoding='utf-8').read())
plainText = "88888888"
encryptedText = ctx.call('encrypt', plainText)
print(encryptedText)
