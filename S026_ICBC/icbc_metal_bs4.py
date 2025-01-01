# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : icbc_metal_bs4.py
@Project            : S026_ICBC
@CreateTime         : 2023/3/10 13:17
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/10 13:17 
@Version            : 1.0
@Description        : None
"""

import re
import requests
from urllib.parse import quote, urlencode
from bs4 import BeautifulSoup

url_listpage = 'https://www.icbc.com.cn/ICBC/' + quote('网上黄金/贵金属资讯/市场快报/')

resp = requests.get(url_listpage)
print(resp.status_code)
resp.encoding = 'utf-8'
soup = BeautifulSoup(resp.text, 'html.parser')

# data-collecting-sign text14da 这个样式是在页面上通过 script 生成的，所以无法提取到
# BeautifulSoup 方案是行不通的
infos = soup.find_all("a", attrs={"class": "data-collecting-sign text14da"})
print(len(infos))
for info in infos:
    print(info)
    url_subpage = info.get("href")
    print(url_subpage)
    break
