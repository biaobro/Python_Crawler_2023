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

import requests

# 这个接口需要从 html 中提取信息
url = "https://www.storyblocks.com/audio/search/baby-crying"


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

session = requests.Session()
resp = session.get(url, headers=headers)
html = resp.text


# 每页上48个音频 item，先用正则得到 item
# 最后1个需要认为构造，否则只能匹配到47个
html = re.sub(",\"selectedSearchFilterOptions", ",{\"stockItem", html)

# 匹配到48个结果就对了
regex_item = r"{\"stockItem\":(.*?)(?={\"stockItem\")"
items = re.findall(regex_item, html)

# 从每个 item 中再匹配具体信息
for item in items:
    regex_title = r"title\":\"(.*?)\""
    title = re.findall(regex_title, item)[0].strip().lower()

    if "cry" not in title:
        if "cries" not in title:
            print("no keyword in title, skip it")
            continue

    regex_duration = r"duration\":(\d+)"
    duration = re.findall(regex_duration, item)[0]

    # "https:\/\/dm0qx8t0i9gc9.cloudfront.net\/previews\/audio\/BsTwCwBHBjzwub4i4\/newborn-baby-crying_fJaO1SEu_NWM.mp3"
    regex_previewUrl = r"previewUrl\":\"(.*?)\""
    previewUrl = re.findall(regex_previewUrl, item)[0].replace("\\", "")

    print(previewUrl)

    filename = previewUrl.split("/")[-1]
    print(filename)

    with open(filename, "wb") as f:
        f.write(session.get(previewUrl, headers=headers).content)

    break



