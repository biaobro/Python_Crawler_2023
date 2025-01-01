# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : endata.py
@Project            : S029_EnData
@CreateTime         : 2023/3/13 22:56
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/13 22:56 
@Version            : 1.0
@Description        : None
"""
import requests
import execjs

url_web = "https://www.endata.com.cn/BoxOffice/BO/Year/index.html"

payload = {'year': 2023, 'MethodName': 'BoxOffice_GetYearInfoData'}
url = "https://www.endata.com.cn/API/GetData.ashx"
resp = requests.post(url, payload)


ctx = execjs.compile(open('webDES.js', 'r', encoding='utf-8').read())
decData = ctx.call('dec', resp.text)
movies = decData['Data']['Table']

for movie in movies:
    print(movie)
