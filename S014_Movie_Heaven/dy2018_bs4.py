"""
# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
#File               : dy2018_bs4.py
#Project            : Crawler_2022
#CreateTime         : 2022/2/27 10:17
#Author             : biaobro
#Software           : PyCharm
#Last Modify Time   : 2022/2/27 10:17 
#Version            : 1.0
#Description        : B站樵夫视频

    # 重点
    1，正则表达式的使用
"""
import requests
from bs4 import BeautifulSoup
import re

# 网页源代码中，我们要找的目标区域的div class 并不唯一，当然可以通过全部获取然后循环筛选，但相对低效
# 我们用正则表达式来进行匹配
url_host = 'https://www.dy2018.com'

resp = requests.get(url_host)
resp.encoding = 'gb2312'

# 从 ul 中提取到 li 列表
li_pattern = re.compile(r'2023必看热片.*?<ul>(?P<html>.*?)</ul>', re.S)
li_list = li_pattern.search(resp.text).group('html')
# print(li_list)

# 从 li 中提取到 a 属性, href  和  title
a_pattern = re.compile(r"<li><a href='(?P<href>.*?)' title=\"(?P<title>.*?)\">")
# a_list = a_pattern.findall(li_list)  # 得到的是元组列表
a_list = a_pattern.finditer(li_list)  # 得到的是迭代器
# print(a_list)

for a in a_list:
    title = a.group('title')
    href = url_host + a.group('href')
    # print(title, href)

    resp = requests.get(href)
    resp.encoding = 'gb2312'
    target_pattern = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<name>.*?)<br \/>.*? <td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download_addr>.*?)">', re.S)
    movie = target_pattern.search(resp.text)

    movie_name = movie.group('name')
    movie_address = movie.group('download_addr')
    print(movie_name, movie_address)

