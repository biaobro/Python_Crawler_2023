# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 01.threadpool.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/31 17:34
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/31 17:34 
@Version            : 1.0
@Description        : None
"""
import os
import requests
from concurrent.futures import ThreadPoolExecutor


def download(image_url):
    res = requests.get(
        url=image_url,
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
    )
    return res

# 注意这个写法，因为 add_done_callback 的参数(这里是save)对应的函数，只能有1个参数 response
# 但是这里还需要1个参数 file_name，所以把 save 放在内部
# 外面包裹1层 outer，这个方法叫做 【闭包】
def outer(file_name):
    def save(response):
        res = response.result()
        if not os.path.exists("images"):
            os.mkdir("images")
        file_path = os.path.join("images", file_name)
        with open(file_path, mode='wb') as img:
            img.write(res.content)
    return save


pool = ThreadPoolExecutor(10)

with open("my.csv", mode="r", encoding="utf-8") as file:
    for line in file:
        nid, name, url = line.split(",")
        file_name = "{}.png".format(name)
        future = pool.submit(download, url)
        future.add_done_callback(outer(file_name))
