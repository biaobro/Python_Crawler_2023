# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : umeitu_aiohttp.py
@Project            : S007_umei
@CreateTime         : 2025/1/5 14:50
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/1/5 14:50 
@Version            : 1.0
@Description        : None


# 知识点
    1，aiohttp proxy
    2，BeautifulSoup 解析html

# 思路
    0，umeitu 无需登录，请求时连 header-UserAgent 都不需要，目测没有任何反爬措施，可以作为很好的爬虫入门
    1，umeitu 这个网站的架构是人物列表页->图片列表，点击图片进入高清大图页
    2，列表页本身会存在多页，【美女写真】达到了164页，具体的高清大图页也会存在多页
    3，index_1 和 page_1 都不可用，后续页码都是从2开始
    4，封装了2个函数，1个用于从列表页提取出详情页地址，另一个用于从详情页提取图片并保存
    5，爬全网：放开循环限制
    6，网站的请求路径是：缩略图列表页 -> 对应人物的大图页面

# 重点
    1，aiohttp
"""

import os
import asyncio
import re

import aiohttp
from bs4 import BeautifulSoup
import aiofiles

url_host = "https://www.umeitu.com"


# 1. 获取页面 HTML 内容
# aiohttp 不会自动走系统开的 VPN
# 但是这个 umei 网站又只能翻墙访问
# 所以需要显式地指定 proxy，代理走 clash，端口是7890，其他代理端口不同
async def fetch(session, url):
    async with session.get(url, proxy="http://127.0.0.1:7890") as response:
        return await response.text()


# 2. 解析 HTML 页面，获取图片 URL
async def parse_mm_list(url, session):
    html = await fetch(session, url)
    soup = BeautifulSoup(html, 'html.parser')
    img_tags = soup.find_all("div", attrs={"class": "tit"})

    for img_tag in img_tags:
        # 找到每个 mm 对应的图片数量，内容格式：38P [秀人XiuRen] No.4612 吴雪瑶
        pic_count = int(img_tag.find("a").string.split("P")[0])
        mm_page_1st = url_host + img_tag.find("a").get("href")

        # 提取图片的 URL
        # 第1页的地址和其他页地址格式不同，所以直接赋值
        # 第1页地址格式 https://www.umeitu.com/img/53772.html
        mm_pages = [mm_page_1st]

        # 循环添加剩下的页码页面
        # 其他页地址格式 https://www.umeitu.com/img/53772_2.html
        for count in range(2, pic_count + 1):
            url_mm_page = mm_page_1st.replace('.html', f'_{count}.html')
            mm_pages.append(url_mm_page)

        # 上面的方法是从列表页 人物介绍信息中提取图片数量，但会存在不准确的情况
        # 所以更准确的是进到第1个详情页，提取尾页页码

        # 只取第1个mm 的子页面
        print(mm_pages)
        break

    return mm_pages


# 3. 下载图片
async def download_image(session, mm_page, folder):
    # 首页和其他页 url 格式不同，这里做个判断。如果 url 里没有包含下划线，则补上 _1
    regex_page_num = r"\d+_?\d+"
    page_num = re.findall(regex_page_num, mm_page)[0]
    if "_" not in page_num:
        page_num = page_num + "_" + str(1)

    try:
        html = await fetch(session, mm_page)
        soup = BeautifulSoup(html, 'html.parser')
        mm_img = soup.find("div", attrs={"class": "vipimglist"}).find("img").get("src")

        # 获取图片响应
        async with session.get(mm_img) as response:
            # 图片内容
            img_data = await response.read()
            # 获取图片名称
            # 1. 从图片链接中提取 文件名，含后缀
            img_name = os.path.basename(mm_img)

            # 2. 提取文件后缀名
            suffix = os.path.splitext(img_name)[-1]

            # 3. 用页面链接中的页码，加上文件后缀名，得到文件名
            img_name = page_num + suffix
            img_path = os.path.join(folder, img_name)

            # 保存图片到指定文件夹
            async with aiofiles.open(img_path, 'wb') as f:
                await f.write(img_data)
            print(f"下载 {img_name} 完成")
    except Exception as e:
        print(f"下载 {img_name} 失败: {e}")


# 4. 主程序
async def main():
    tags = "/tags/graphis/"
    url = url_host + tags
    folder = 'images'  # 存储图片的文件夹
    if not os.path.exists(folder):
        # 方式1，只创建最后1级目录，如果指定了中间目录，但是中间目录不存在，则报错
        os.mkdir(folder)

        # 方式2，如果指定了中间目录，则连中间目录一起创建
        # exist_ok 表示目录不存在时创建，目录存在时也不会抛出异常
        os.makedirs(folder, exist_ok=True)  # 创建文件夹

    async with aiohttp.ClientSession() as session:
        # 获取该页面的图片链接
        mm_pages = await parse_mm_list(url, session)

        # 下载所有图片
        tasks = []
        for mm_page in mm_pages:
            task = download_image(session, mm_page, folder)
            tasks.append(task)

        # 等待所有下载任务完成
        await asyncio.gather(*tasks)


# 启动爬虫
if __name__ == '__main__':
    asyncio.run(main())
