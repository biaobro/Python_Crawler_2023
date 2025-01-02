# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : storyblocks_page.py
@Project            : S054_StoryBlocks
@CreateTime         : 2023/4/25 18:15
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/25 18:15 
@Version            : 1.0
@Description        : None
"""
import re
import time

import requests

# 这个接口需要从 html 中提取信息
url = "https://www.storyblocks.com/audio/search/baby-crying"

session = requests.Session()

for page in range(1, 3):
    # 这个接口可以直接返回json 数据
    url_api = f"https://www.storyblocks.com/api/audio/search?searchTerm=baby crying&search-origin=pagination&duration_min=&duration_max=&sort=most_relevant&sortOrder&page={page}&results_per_page=48&artist_ids=&portal_artist_ids=&search_similar_id="
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    resp = session.get(url_api, headers=headers)

    data = resp.json()['data']
    items = data['stockItems']
    # print(len(items))

    # 从每个 item 中再匹配具体信息
    for item in items:
        title = item['stockItem']['title'].strip().lower()

        if "cry" not in title:
            if "cries" not in title:
                print(f"no keyword in title {title}, skip it")
                continue

        duration = item['stockItem']['duration']

        previewUrl = item['stockItem']['previewUrl']
        print(previewUrl)

        filename = previewUrl.split("/")[-1]
        print(filename)

        with open(filename, "wb") as f:
            f.write(session.get(previewUrl, headers=headers).content)

        time.sleep(3)