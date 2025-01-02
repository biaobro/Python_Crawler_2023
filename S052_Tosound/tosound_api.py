# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : tosound_api.py
@Project            : S052_Tosound
@CreateTime         : 2023/4/24 19:04
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/24 19:04 
@Version            : 1.0
@Description        : None
"""
import time

import requests
import base64
import re

# JS 源代码
"""
    var file_index = href.lastIndexOf("file") + 5;
    var token = window.btoa(href.substring(file_index, href.length));
    var preview_url = href + '&token=' + token + '&sound=audio.mp3';
"""

headers = {
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

url = 'https://www.tosound.com/search/word-%E5%A9%B4%E5%84%BF%E5%95%BC%E5%93%AD%E7%B4%A0%E6%9D%90/page-'
resp = requests.get(url, headers=headers)

target = 'class="soundcard col-xl-3 col-md-4 col-sm-6 mb-4"'
regex_tbr = 'class="soundcard col-lg-3 mb-4"'
updateHtml = re.sub(regex_tbr, target, resp.text)

# print(updateHtml)

regex_cards = r"(?<=<div class=\"soundcard col-xl-3 col-md-4 col-sm-6 mb-4\">)[\s\S]*?(?=<div class=\"soundcard col-xl-3 col-md-4 col-sm-6 mb-4\">)"
cards = re.findall(regex_cards, updateHtml)

for idx, card in enumerate(cards):
    regex_title = r'<a class="h6 text-white font-weight-bold" target="_blank".*>(.*)<\/a>'
    title = re.findall(regex_title, card)[0]

    regex_source = r'来源：(.*)<\/div>'
    source = re.findall(regex_source, card)[0]

    regex_ftype = r'"音频格式">(.*)<\/a>'
    ftype = re.findall(regex_ftype, card)[0]

    regex_size = r'"文件大小">(.*)<\/a>'
    size = re.findall(regex_size, card)[0]

    regex_bitrate = r'"比特率">(.*)<\/a>'
    bitrate = re.findall(regex_bitrate, card)[0]

    regex_desc = r'描述：<\/span>([\s\S]*?)<\/div>'
    desc = re.findall(regex_desc, card)[0].strip()

    regex = r"https:\/\/.*?mp3"
    href = re.findall(regex, card)[0]
    # print(href)
    try:
        file_index = href.rindex("file") + 5
    except:
        file_index = -1 + 5

    tbs = href[file_index:]

    b = base64.encodebytes(tbs.encode("utf8"))
    token = b.decode("utf8").strip()
    preview_url = href + '&token=' + token + '&sound=audio.mp3'
    # print(preview_url)

    print(title, ftype, size, bitrate, desc)

    filename = str(idx) + "." + ftype
    with open(filename, 'wb') as f:
        f.write(requests.get(preview_url, headers=headers).content)

    time.sleep(5)
