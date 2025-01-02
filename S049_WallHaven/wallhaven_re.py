# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : wallhaven_re.py
@Project            : S049_WallHaven
@CreateTime         : 2023/4/24 12:05
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/24 12:05 
@Version            : 1.0
@Description        : None
"""
import requests
import re

url_list = "https://wallhaven.cc/hot?page=" + '1'
resp = requests.get(url_list)
# print(resp.text)

regex = r"(?<=a class=\"preview\" href=\")(.*?)(?=\"  target=\"_blank\")"
hrefs = re.findall(regex, resp.text)
# print(len(hrefs))

for href in hrefs:
    print(href)
    resp = requests.get(href)

    regex = r"(?<=<img id=\"wallpaper\" src=\")(.*?)(?=\")"
    # findall 的返回类型是 list，即便只有1个元素
    url_img = re.findall(regex, resp.text)[0]
    print(url_img)
    filename = url_img.split('/')[-1]
    print(filename)
    with open(f"{filename}", 'wb') as f:
        f.write(requests.get(url_img).content)
    break
