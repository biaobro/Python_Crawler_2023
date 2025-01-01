# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : players.py
@Project            : S022_Hupu
@CreateTime         : 2023/3/6 22:58
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/6 22:58 
@Version            : 1.0
@Description        : None
"""
import requests
from lxml import etree

url = "https://nba.hupu.com/stats/players"

resp = requests.get(url)

et = etree.HTML(resp.text)

trs = et.xpath('//*[@id="data_js"]/div[4]/div/table/tbody/tr')

with open('players.csv', mode='w', encoding='utf-8-sig') as f:
    for idx, tr in enumerate(trs):
        if idx != 0:
            order = tr.xpath('./td[1]/text()')[0]
            name = tr.xpath('./td[2]/a/text()')[0]
            team = tr.xpath('./td[3]/a/text()')[0]
            point = tr.xpath('./td[4]/text()')[0]
            print(order, name, team, point)
            f.write(f"{order},{name},{team},{point}\n")
        else:
            f.write(f"排名,球员,球队,得分\n")
