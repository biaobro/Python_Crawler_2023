"""
# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
#File               : umeitu_bs4.py
#Project            : Crawler_2022
#CreateTime         : 2022/2/19 22:49
#Author             : biaobro
#Software           : PyCharm
#Last Modify Time   : 2022/2/19 22:49
#Version            : 1.0
#Description        : B站樵夫视频

# 知识点
    1，requests
    2，BeautifulSoup 解析html

# 思路
    0，umeitu 无需登录，请求时连 header-UserAgent 都不需要，目测没有任何反爬措施，可以作为很好的爬虫入门
    1，umeitu 这个网站的架构是列表页->图片列表，点击图片进入高清大图页
    2，列表页本身会存在多页，【美女写真】达到了164页，具体的高清大图页也会存在多页
    3，index_1 和 page_1 都不可用，后续页码都是从2开始
    4，封装了2个函数，1个用于获取详情页上的高清大图，另一个用于获取列表页
    5，爬全网：在get_indexpage 中循环调用get_detail， 然后在main 中循环调用 get_indexpage
    6，网站的请求路径是：缩略图列表页 -> 对应人物的大图页面

# 重点
    1，BeautifulSoup的使用，页面元素的查找和定位
    2，标签的属性

# 问题点
    1，需改善【尾页】的查询效率
    2，目前为单线程，图片1张张依次获取，低效
"""

import requests
import re
from bs4 import BeautifulSoup
import os
import aiohttp
import asyncio

# global variables
url_host = "https://www.umeitu.com"
tags = "/tags/graphis"
url_index = url_host + tags + '/'


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = response.text
    await session.close()
    return result


async def request(url):
    print('Waiting for', url)
    result = await get(url)
    print('Get response from', url, 'Result:', result)


tasks = [asyncio.ensure_future(request(url_index)) for _ in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))


# 请求【大图】图片地址，并保存图片
# hr : high resolution
async def get_mm_page(url_mm_page):
    print("url_mm_page : ", url_mm_page)
    # url 示例：
    # 首页：https://www.umeitu.com/img/52419.html
    # 第2页：https://www.umeitu.com/img/52419_2.html
    regex_page_num = r"\d+_?\d+"
    page_num = re.findall(regex_page_num, url_mm_page)[0]
    if "_" not in page_num:
        page_num = page_num + "_" + str(1)

    # 发送请求
    resp = await get(url_mm_page)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')

    # 找到页面上高清大图的地址，因为地址中包含有无规律字符串，所以必须先得到html 页面
    # 再从 html 页面中得到大图地址
    url_mm_img = soup.find("div", attrs={"class": "vipimglist"}).find("img").get("src")
    print("url_mm_img : ", url_mm_img)

    get_mm_img(url_mm_img)


# 直接请求图片 url，拿到响应并保存
async def get_mm_img(url_mm_img):
    # 请求图片，以页码作为文件名保存
    async with requests.get(url_mm_img) as req:
        return await req.content


async def save_mm_img(img_content, file_name):
    if not os.path.exists("images"):
        os.mkdir("images")
    async with open("images/umeitu_%s.jpg" % file_name, 'wb') as f:
        f.write(img_content)
        print("umeitu_%s.jpg saved done !" % file_name)


# 请求列表页，得到每张【小图】图片的对应的页面地址
def get_index_page(url_index):
    # send request
    resp = requests.get(url_index)
    resp.encoding = 'utf-8'

    # parse the html
    soup = BeautifulSoup(resp.text, 'html.parser')

    # find the link of each preview image
    mm_list = soup.find_all("div", attrs={"class": "tit"})
    for mm in mm_list:
        # 找到每个 mm 对应的图片数量，内容格式：38P [秀人XiuRen] No.4612 吴雪瑶
        pic_count = int(mm.find("a").string.split("P")[0])
        url_mm = url_host + mm.find("a").get("href")
        # 从1开始 而不是从0
        for count in range(1, pic_count + 1):
            if count == 1:
                get_mm_page(url_mm)
                url_mm = re.sub(r"\.html", "_1.html", url_mm)
            else:
                url_mm = re.sub(r"(?<=_)(\d+)", str(count), url_mm)
                get_mm_page(url_mm)


        # 测试控制，只爬取第1个人物对应的全部高清大图
        break

    # 如果有index_2 等等，则继续爬，可以实现爬全网的目的了，慎用
    lastpage = find_lastpage(resp)
    if lastpage is not None:
        for pagenum in range(2, int(lastpage) + 1):
            url_index_next = url_host + tags + "_" + str(pagenum) + "/"
            print(url_index_next)

            # 测试控制，只爬取第1个列表页面
            break
            get_index_page(url_index_next)


# 继续抽象，因为在列表页 和 详情页 都需要判断是否有下一页，或者最后一页的页码
def find_lastpage(resp):
    regex_pattern = re.compile(r'<a href=.*?(\d*)\/\">尾页', re.S)
    try:
        last_page_num = regex_pattern.search(resp.text).group(1)
        print("尾页页码为 : ", last_page_num)
        return int(last_page_num)
    except:
        return None


if __name__ == '__main__':
    # 受2个 break 的控制，目前只爬取第1页上第1个mm 的图片
    get_index_page(url_index)
