# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : icbc_metal_xpath.py
@Project            : S026_ICBC
@CreateTime         : 2023/3/10 9:31
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/10 9:31 
@Version            : 1.0
@Description        : None
"""
import re
import requests
from urllib.parse import quote, urlencode
from lxml import etree

url_listpage = quote('https://www.icbc.com.cn/ICBC/网上黄金/贵金属资讯/市场快报/')

# 这个id 可以在静态页面中提取得到
index_page_id = '1438058343720960016'
payload = {
    'currentColumnId': index_page_id,
    'summaryColumnId': '',
    'displayTopPostings': 0,
    'needDisplayChildrenPostings': False,
    'author': '',
    'enablePager': True,
    'page': 1,
    'size': 60,  # 默认是20，总共3页，所以直接用60
    'isUseDomain': False,
    'domainName': ''
}

url_subpage = 'https://papi.icbc.com.cn/cmspage/columns/webpart/webservice/channelSummaryList?' + urlencode(payload)
resp = requests.get(url_subpage)

gold_trends, gold_rates, gold_prices = [], [], []
silver_trends, silver_rates, silver_prices = [], [], []
market = {}

postings = resp.json()['data']['postings']
for posting in postings:
    try:
        date = re.findall(r"\d+", posting['name'])[0]
        url = "https://www.icbc.com.cn/" + posting['path']
        print(date, url)

        resp = requests.get(url)
        resp.encoding = 'utf-8'

        # etree.parse(filePath) 用于加载本地HTML
        et = etree.HTML(resp.text)
        text = et.xpath('//*[@id="mypagehtmlcontent"]//text()')
        text = ''.join(text).strip()

        # findall 的返回是个列表，包含1个元组，元组内是匹配到的 group
        regex = r"价格(\D+)(.*?%)，收于(.*?)美元\/盎司"
        groups = re.findall(regex, text)
        gold, silver = groups[0], groups[1]
        print(gold, silver)
        gold_trend, gold_rate, gold_price = gold[0], gold[1], gold[2]
        silver_trend, silver_rate, silver_price = silver[0], silver[1], silver[2]
        market.update({date: ','.join(gold) + ',' + ','.join(silver)})
    except Exception as e:
        print(e, "no info on this page.")
print(market)

