#!/usr/bin/python3
# Coding: UTF-8 
"""
# Created On: 2021/4/10 22:13
# Author: biaobro
# Project: Crawler
# File Name: crawler_bilibili.py
# Description: 
"""
import json
import os
import csv
import requests
import datetime

# open 必须有配套的close， 要么使用with
# 生成文件 并添加表头
csv_headers = ['url_self_wrapped', 'url_other_wrapped', 'mid', 'name', 'sex', 'face', 'sign', 'rank', 'level',
               'jointime', 'moral', 'silence', 'birthday',
               'coins', 'following', 'follower']
with open(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + '.csv', 'w',
          newline='', encoding='utf-8') as csv_file:
    csv_file_writer = csv.writer(csv_file)
    csv_file_writer.writerow(csv_headers)


# html header
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "referer": "https://space.bilibili.com/25",
    "origin": "https://space.bilibili.com"
}

session = requests.session()
session.headers = headers

# 自己信息
# 得到的是 json 格式
url_self = "https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp"

# 关联信息
url_other = "https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp"


def get_info(uid):
    global csv_file, json_data_self, json_data_other

    # 注意这个写法
    url_self_wrapped = url_self.format(uid)
    html = session.get(url_self_wrapped)

    if html.json()['code'] == 0:
        json_data_self = html.json()['data']
        print(json_data_self)
    else:
        print("error code" + html.json()['code'])
        exit()

    url_other_wrapped = url_other.format(uid)
    html = session.get(url_other_wrapped)
    if html.json()['code'] == 0:
        json_data_other = html.json()['data']

    # get_img(uid, json_data['face'])

    # csv 中文编码需要用 'utf-8-sig'
    with open(csv_file.name, 'a', newline='', encoding='utf-8-sig') as f:
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerow([url_self_wrapped, url_other_wrapped,
                             json_data_self['mid'], json_data_self['name'], json_data_self['sex'],
                             json_data_self['face'],
                             json_data_self['sign'], json_data_self['rank'], json_data_self['level'],
                             json_data_self['jointime'],
                             json_data_self['moral'], json_data_self['silence'], json_data_self['birthday'],
                             json_data_self['coins'],
                             json_data_other['following'], json_data_other['follower']])


def get_img(uid, url):
    if not os.path.exists('data'):
        os.mkdir('data')
    img = session.get(url, headers=headers).content
    with open('data/{}.jpg'.format(uid), 'wb') as f:
        f.write(img)


def main():
    for i in range(1, 3):
        print(str(i) + "-" * 20)
        get_info(i)


if __name__ == '__main__':
    main()
