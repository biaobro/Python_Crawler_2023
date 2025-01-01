#!/usr/bin/python3
# Coding: UTF-8 
"""
# Created On: 2021/4/10 17:35
# Author: biaobro
# Project: Crawler
# File Name: crawler_wangyi_covid.py
# Description: 
"""
from lxml import etree
import time
import requests
import lxml
import openpyxl
import json
import re

# 要用pip 手动安装：pip install python-rapidjson
# pycharm 自动安装的是 rapidjson
import rapidjson

wb = openpyxl.Workbook()
sheet = wb.active

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}


# 这个函数爬不到数据，因为网页上的数据是实时从后端获取的，改用直接访问网页请求
def get_data():
    url = "https://wp.m.163.com/163/page/news/virus_report/index.html?_nw_=1&_anw_=1"
    html = requests.get(url, headers=headers)
    html.encoding = "utf-8"
    soup = etree.HTML(html.text)
    cover_data = soup.xpath('//div[@class="cover_data_china noNewsScroll"]/div[starts-with(@class,"cover")]')
    current_time = soup.xpath('//div[@class="cover_time"]/text()')
    print(current_time)
    for cover in cover_data:
        title = cover.xpath('h4/text()')[0]
        number = cover.xpath('div[@class="number"]/text()')
        print(title, number)


def get_data_realtime():
    url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=323609977928"

    # 这里返回的html直接就是json 格式的，content-type:application/json;charset=UTF-8
    html = requests.get(url, headers=headers)

    # html.json() 转换为字典
    print(html.json()['data']['chinaTotal']['total'])

    # 13位时间戳
    current_time = html.json()['timestamp']
    print(current_time)
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_time / 1000))
    print(local_time)

    for k, v in html.json()['data']['chinaTotal']['total'].items():
        print(k, v)


def get_data_by_day():
    sheet.append(["date",
                  "thatday_variance_confirm", "thatday_variance_suspect", "thatday_variance_heal",
                  "thatday_variance_dead", "thatday_variance_storeConfirm", "thatday_variance_severe",
                  "thatday_statistics_confirm", "thatday_statistics_suspect", "thatday_statistics_heal",
                  "thatday_statistics_dead", "thatday_statistics_severe", "thatday_statistics_input",
                  "ext_data", "last_update_time"])

    url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=323612150287"
    html = requests.get(url, headers=headers)
    # print(html.json()['data']['chinaDayList'])

    for day_detail in html.json()['data']['chinaDayList']:
        date = day_detail['date']
        thatday_variance_confirm = day_detail['today']['confirm']
        thatday_variance_suspect = day_detail['today']['suspect']
        thatday_variance_heal = day_detail['today']['heal']
        thatday_variance_dead = day_detail['today']['dead']
        thatday_variance_storeConfirm = day_detail['today']['storeConfirm']
        # thatday_variance_input = day_detail['today']['input']
        thatday_variance_severe = day_detail['today']['severe']

        thatday_statistics_confirm = day_detail['total']['confirm']
        thatday_statistics_suspect = day_detail['total']['suspect']
        thatday_statistics_heal = day_detail['total']['heal']
        thatday_statistics_dead = day_detail['total']['dead']
        thatday_statistics_severe = day_detail['total']['severe']
        thatday_statistics_input = day_detail['total']['input']

        ext_data = day_detail['extData']
        last_update_time = day_detail['lastUpdateTime']
        # print(date, thatday_variance, thatday_statistics, ext_data, last_update_time)
        sheet.append([date,
                      thatday_variance_confirm, thatday_variance_suspect, thatday_variance_heal,
                      thatday_variance_dead, thatday_variance_storeConfirm, thatday_variance_severe,
                      thatday_statistics_confirm, thatday_statistics_suspect, thatday_statistics_heal,
                      thatday_statistics_dead, thatday_statistics_severe, thatday_statistics_input,
                      ext_data, last_update_time])
    wb.save("a.xlsx")


def get_news_2022():
    # 2023年页面改版，新闻改为动态获取了，无法从静态页面中直接解析
    # url = "https://wp.m.163.com/163/page/news/virus_report/index.html?_nw_=1&_anw_=1"

    url = "https://ent.163.com/special/00035080/virus_report_data.js?_=1675850876063&callback=callback"

    html = requests.get(url, headers=headers)
    html.encoding = "utf-8"
    print(html.text)
    tree = etree.HTML(html.text)
    news_list = tree.xpath('//*[@id="time_lists"]/li')
    print(len(news_list))
    for news in news_list:
        news_time = news.xpath("./div/text()")
        news_title = news.xpath('./a/div/text()')
        print(news_time, news_title)


def get_news_2023():

    url = "https://ent.163.com/special/00035080/virus_report_data.js?_=1675850876063&callback=callback"

    html = requests.get(url, headers=headers)
    # html.encoding = "utf-8"
    # print(html.text)

    # 不带 []
    # regex_news_List = r'(?<=list:\[)([\s\S]*?)(?=\])'

    # 带[]
    regex_news_List = r"(?<=list:)(\[[\s\S]*?)(?<=\])"
    news_list = re.findall(regex_news_List, html.text)[0].strip()

    # 这样提取到的数据，形式是列表，两端是[]
    # 但实质是字符串，需要强制转换为 list
    # 不能用 list()，得到的是1整个 list
    # eval() 是把 字符串两端的引号去掉，真正得到包含多个元素的 list
    news_list = eval(news_list)

    # news 是字典类型
    for news in news_list:
        title = news['title']
        time = news['time']

        # print(news)
        print(time, title)


if __name__ == '__main__':
    # get_data_realtime()
    # get_news_2023()
    get_data_by_day()
