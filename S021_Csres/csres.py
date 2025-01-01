# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : csres.py
@Project            : S021_csres
@CreateTime         : 2023/2/24 23:42
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/24 23:42 
@Version            : 1.0
@Description        : None
"""
import requests
from lxml import etree

urls = [
    f"http://wap.csres.com/sort/chtype/F01_{page}.html"
    for page in range(1, 14 + 1)
]

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
                  'Safari/537.36 '
}


def craw(url):
    resp = requests.get(url, headers=header)
    return resp.text


def parse(html):
    et = etree.HTML(html)
    trs = et.xpath("//thead[@class='th1']/tr")
    res = ''
    count = 0
    for idx, tr in enumerate(trs):
        count = count + 1
        if idx == 0:
            continue

        serial_num = tr.xpath("./td[1]/a/font/text()")[0]
        name = tr.xpath("./td[2]/a/font//text()")[0]
        department = tr.xpath("./td[3]/font/text()")[0].strip()
        date = tr.xpath("./td[4]/font/text()")[0]
        status = tr.xpath("./td[5]/font/text()")[0]
        # print(serial_num, name, department, date, status)
        # with open('data.csv', 'a+', encoding='GBK') as f:
        #     f.write('{},{},{},{},{}\n'.format(serial_num, name, department, date, status))
        res = res + '{},{},{},{},{}\n'.format(serial_num, name, department, date, status)
    return res


