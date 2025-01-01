"""
# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
#File               : lottery_requests_bs4.py
#Project            : Crawler_2022
#CreateTime         : 2022/2/21 21:12
#Author             : biaobro
#Software           : PyCharm
#Last Modify Time   : 2022/2/21 21:12
#Version            : 1.0
#Description        : None
"""
import requests
from bs4 import BeautifulSoup

# 500彩票，双色球，历史数据
url = 'https://datachart.500.com/ssq/history/history.shtml'

resp = requests.get(url)

# 解析html
html = BeautifulSoup(resp.text, 'html.parser')

# find() 找1个，findall() 找全部
trlist = html.findAll('tr', attrs={'class': 't_tr1'})

# tr 行，定义行列表
tr_tbr = []

with open('data/lottery.txt', mode='w', encoding='utf-8') as f:
    for tr in trlist:
        tdlist = tr.findAll('td')

        # td 单元格，定义单元格列表
        td_tbr = []

        for td in tdlist:
            td_tbr.append(td.text.replace(',', ''))
        print(td_tbr)
        f.write(",".join(td_tbr)+"\n")
        # tr_tbr.append(td_tbr)

# print(tr_tbr)
