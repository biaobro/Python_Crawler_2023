# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 14.beautifulsoup.py
@Project            : Crawler_2022
@CreateTime         : 2022/1/23 11:38
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2022/1/23 11:38 
@Version            : 1.0
@Description        : B站IT私塾
"""
from bs4 import BeautifulSoup
import re


def main():
    file = open("./baidu.html", 'rb')
    html = file.read().decode('utf-8')
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs.title.string)
    # print(bs.a)
    # print(bs.head)
    # print(bs.a.attrs)
    # print(bs.a.string)

    # should consider comment
    # print(type(bs.a.string))
    # print(bs.name)

    # 遍历
    # print(bs.head.contents[3])

    # find_all

    # 用 tag 名称查找
    # r_list = bs.find_all('a')

    # 正则表达式
    # r_list = bs.find_all(re.compile('a'))

    # 函数
    # r_list = bs.find_all(name_is_exist)

    # 用 id 查找
    # r_list = bs.find_all(id='u1')

    # 用 值 查找
    # r_list = bs.find_all(href="http://www.hao123.com")

    # 用 string 查找
    # r_list = bs.find_all(text='hao123')
    # r_list = bs.find_all(text=re.compile('\\d'))
    
    # limit 限制返回结果数
    # r_list = bs.find_all('a', limit=3)
    # print(r_list)

    # css 选择器
    # r_list = bs.select('title')

    # css 按 类名 查找
    # r_list = bs.select(".mnav")

    # css 按 id 查找
    # r_list = bs.select("#u1")

    # css 按标签+类目 查找
    # r_list = bs.select('a[class="bri"]')

    # css 子标签
    # r_list = bs.select('head > title')

    # css 兄弟标签
    r_list = bs.select('.mnav ~ .bri')

    for item in r_list:
        print(item)
        print(item.get_text())


def name_is_exist(tag):
    return tag.has_attr("name")


if __name__ == '__main__':
    main()
