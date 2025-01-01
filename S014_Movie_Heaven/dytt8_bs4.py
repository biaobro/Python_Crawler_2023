"""
# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
#File               : dytt8_bs4.py
#Project            : Crawler_2022
#CreateTime         : 2022/2/27 9:46
#Author             : biaobro
#Software           : PyCharm
#Last Modify Time   : 2022/2/27 9:46 
#Version            : 1.0
#Description        : None
"""
import requests
from bs4 import BeautifulSoup

url_host = 'https://dy.dytt8.net'
url_index = url_host + '/index2.htm'
resp = requests.get(url_index)
resp.encoding = 'gb2312'
html = BeautifulSoup(resp.text, 'html.parser')
content_area = html.select_one('.co_content8')
td_area = content_area.findAll('td', attrs={'class': 'inddline'})
# print(td_area)
for td in td_area:
    movies = td.findAll('a')
    # 过滤掉第1条广告链接
    if len(movies) < 2:
        continue
    for movie in movies:
        # 过滤掉开头的广告
        if movie.text != '最新电影下载':
            print(movie.text, url_host + movie.get('href'))
    # print(movies)

# if __name__ == '__main__':
#     pass
