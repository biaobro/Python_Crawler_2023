# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : dangdang_book.py
@Project            : S058_DangDang
@CreateTime         : 2023/5/9 10:29
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/5/9 10:29 
@Version            : 1.0
@Description        : 当当网貌似连反爬都没有
"""
import csv
import json
import os.path
import random
import re
import time
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

url_web = "http://bang.dangdang.com/books/bestsellers"


class DangDangWang:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'referer': 'http://bang.dangdang.com/books/',
        }
        self.cookies = {
            'ddscreen': '2',
            'dest_area': 'country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0',
            '__permanent_id': '20230509102818473107204771046229195',
            '__visit_id': '20230509102818500342872650220599196',
            '__out_refer': '1683599299 |! | cn.bing.com |! |; __rpm = |...1683599323555',
            '__trace_id': '20230509102843968402835273545506433',
        }

    def get_data(self, page):
        print(f'now in page {page}')

        # 获取网页数据
        url = f"http://bang.dangdang.com/books/bestsellers/1-{page}"
        resp = requests.get(url, headers=self.headers, cookies=self.cookies)
        resp.encoding = 'gbk'

        # 使用BeautifulSoup 解析 HTML
        soup = BeautifulSoup(resp.text, 'lxml')

        # 找到图书列表项
        # 右键，Copy - Copy Selector
        items = soup.select("div.bang_list_box > ul > li")

        # 循环处理每个列表项
        for item in items:
            title = item.select('.name > a')[0].get('title').strip()
            author = item.select('.publisher_info')[0].select_one('a').get('title').strip()
            publish_time = item.select('.publisher_info')[1].select_one('span').text
            price = item.select('.price_n')[0].text.strip()

            # 这个是 comment page 的url，实际的 comment content 是从该page 的返回中提取信息
            # 然后又发出1个 xhr(ajax) 请求得到的
            url_comment_page = item.select_one('.star > a').get('href')
            print(url_comment_page)

            comment = ''
            for i in range(1):
                resp = requests.get(url=url_comment_page, headers=self.headers, cookies=self.cookies)
                info = json.loads(re.findall('var prodSpuInfo = (.*?);', resp.text)[0])
                print(info)

                productId = info.get('productId')
                categoryPath = info.get('categoryPath')

                url_base = "https://product.dangdang.com/index.php?"
                params = {
                    'r': 'comment/list',
                    'productId': productId,
                    'categoryPath': categoryPath,
                    'mainProductId': productId,
                    'mediumId': '0',
                    'pageIndex': 1,
                    'sortType': 1,
                    'filterType': 1,
                    'isSystem': 1,
                    'tagId': 0,
                    'tagFilterCount': 0,
                    'template': 'publish'
                }
                url_comment_list = url_base + urlencode(params)
                print(url_comment_list)
                while True:
                    try:
                        resp = requests.get(url_comment_list, headers=self.headers, cookies=self.cookies)
                        print('+'*20)
                        data = resp.json()['data']['list']['html']
                        soup = BeautifulSoup(data, 'lxml')
                        break
                    except:
                        time.sleep(random.uniform(4, 6))
                comment = '\r\n'.join([a.get_text().strip() for a in soup.select('.describe_detail a')])

            # 保存数据
            self.save_data(title, author, publish_time, price, comment)

            # 打印结果
            print(f'book name : {title}')
            print(f'book author : {author}')
            print(f'publish time : {publish_time}')
            print(f'comment : {comment}')
            print(f'price : {price}')
            print('---', end=' ')
            print(time.strftime('%H:%M:%S', time.localtime(time.time())))

    def save_data(self, title, author, publish_time, price, comment):
        with open('data.csv', mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([title, author, publish_time, price, comment])

    def main(self):
        # 判断文件是否存在
        start = time.time()
        if not os.path.exists('data.csv'):
            with open('data.csv', mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['title', 'author', 'publish_time', 'price', 'comment'])
        # 待爬取的页面数量
        page_count = 2
        for page in range(1, page_count):
            self.get_data(page)
            time.sleep(random.uniform(4, 6))
        end = time.time()
        print(end - start)


if __name__ == '__main__':
    ddw = DangDangWang()
    ddw.main()
