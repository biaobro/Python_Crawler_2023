# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : icbc_metal_selenium.py
@Project            : S026_ICBC
@CreateTime         : 2023/3/10 14:21
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/10 14:21 
@Version            : 1.0
@Description        : None
"""
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from urllib.parse import quote

import init_webdriver

folder_name = r'..\\'
file_name = r'chromedriver.exe'

url = 'https://www.icbc.com.cn/ICBC/' + quote('网上黄金/贵金属资讯/市场快报/')

def getData():
    driver_path = init_webdriver.driver_seek(folder_name, file_name)
    if driver_path is None:
        driver_path = r'..\\'
        init_webdriver.driver_download(driver_path)

    options = webdriver.ChromeOptions()
    options.add_argument(r"--headless")
    # options.add_argument(r"user-data-dir=data")

    # 初始化浏览器
    browser = webdriver.Chrome(service=ChromeService(driver_path), options=options)

    # 地址必须带协议，否则报错参数不正确
    browser.get(url)
    time.sleep(1)

    # page_source 是渲染后的页面源代码，类型为字符串，包含了想要的数据
    # 如果直接从 Spider 中请求，得到的是没有渲染的
    page_source = browser.page_source
    print(page_source)

    # 这里因为要得到 渲染后的数据，所以获取 page_source
    # 但 page_source 已经是 string，所以只能配合 正则表达式来继续
    # Webdriver 的 find_elements() 也用不上

    browser.quit()

getData()