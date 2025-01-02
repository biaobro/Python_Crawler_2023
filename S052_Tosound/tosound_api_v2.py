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
import csv

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

csvHeaders = ['filename', 'title', 'author', 'source', 'ftype', 'duration', 'size', 'bitrate', 'channel', 'samplerate',
              'bitdepth', 'desc']
with open('data_0425_1208.csv', 'a', newline='', encoding='utf-8-sig') as fcsv:
    # 提前预览列名
    csvWriter = csv.writer(fcsv)

    # 写入列名
    csvWriter.writerow(csvHeaders)

    for page in range(1, 200):
        url = 'https://www.tosound.com/search/word-%E5%A9%B4%E5%84%BF%E5%95%BC%E5%93%AD%E7%B4%A0%E6%9D%90/page-'
        if page != 1:
            url = url + str(page)
        resp = requests.get(url, headers=headers)

        target = 'class="soundcard col-xl-3 col-md-4 col-sm-6 mb-4"'
        regex_tbr = 'class="soundcard col-lg-3 mb-4"'
        updateHtml = re.sub(regex_tbr, target, resp.text)

        # print(updateHtml)

        # 每个 page 对应 12个 card
        regex_cards = r"(?<=<div class=\"soundcard col-xl-3 col-md-4 col-sm-6 mb-4\">)[\s\S]*?(?=<div class=\"soundcard col-xl-3 col-md-4 col-sm-6 mb-4\">)"
        cards = re.findall(regex_cards, updateHtml)

        for idx, card in enumerate(cards, start=1):
            # 先获取信息
            regex_id = r"sound=\"(.*?)\""
            soundId = re.findall(regex_id, card)[0]

            # 请求信息
            url_detail = f"https://www.tosound.com/index.php?app=sound&ac=detail&sound={soundId}&item=info&translate=true"
            resp_infos = requests.get(url_detail, headers=headers).text

            # 提取信息
            regex_title = r'<h4>([\s\S]*?)<\/h4>'
            title = re.findall(regex_title, resp_infos)[0]

            # 判断，如果标题中不包含 哭，或者 cry 就跳过，不再继续
            if "哭" not in title:
                if "cry" not in title:
                    continue

            regex_author = r'作者：<\/td><td>(.*?)<\/td>'
            author = re.findall(regex_author, resp_infos)[0].strip()

            regex_source = r'来源：<\/td><td>([\s\S]*?)<a'
            source = re.findall(regex_source, resp_infos)[0].strip()

            regex_ftype = r'音频格式<\/td><td>(.*?)<\/td>'
            ftype = re.findall(regex_ftype, resp_infos)[0]

            regex_duration = r'声音时长<\/td><td>(.*?)<\/td>'
            duration = re.findall(regex_duration, resp_infos)[0]

            regex_size = r'文件大小<\/td><td>(.*?)<\/td>'
            size = re.findall(regex_size, resp_infos)[0]

            regex_bitrate = r'比特率<\/td><td>(.*?)<\/td>'
            bitrate = re.findall(regex_bitrate, resp_infos)[0]

            try:
                regex_channel = r'声道<\/td><td>(.*?)<\/td>'
                channel = re.findall(regex_channel, resp_infos)[0]
            except:
                channel = ""

            try:
                regex_samplerate = r'采样率<\/td><td>(.*?)<\/td>'
                samplerate = re.findall(regex_samplerate, resp_infos)[0]
            except:
                samplerate = ""

            try:
                regex_bitdepth = r'位深度<\/td><td>(.*?)<\/td>'
                bitdepth = re.findall(regex_bitdepth, resp_infos)[0]
            except:
                bitdepth = ""

            regex_desc = r"描述：<\/td><td>([\s\S]*?)<\/td>"
            desc = re.findall(regex_desc, resp_infos)[0].strip()

            # 然后获取音频文件
            regex_url = r"https:\/\/.*?mp3"
            url_short = re.findall(regex_url, card)[0]

            # 得到 Token
            try:
                file_index = url_short.rindex("file") + 5
            except:
                file_index = -1 + 5

            tbs = url_short[file_index:]
            b = base64.encodebytes(tbs.encode("utf8"))
            token = b.decode("utf8").strip()
            preview_url = url_short + '&token=' + token + '&sound=audio.mp3'
            # print(preview_url)

            # 确定文件名称
            filename = str(page).zfill(3) + "_" + str(idx).zfill(3) + "_" + soundId + "." + ftype

            # 保存文件信息
            record = [filename, title, author, source, ftype, duration, size, bitrate, channel, samplerate, bitdepth,
                      desc, url_short, preview_url]
            print(record)
            csvWriter.writerow(record)

            # 保存文件
            # with open(filename, 'wb') as fmp3:
            #     fmp3.write(requests.get(preview_url, headers=headers).content)

            time.sleep(1)
