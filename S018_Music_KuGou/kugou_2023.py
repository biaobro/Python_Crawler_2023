# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : kugou_2023.py
@Project            : S018_kugou
@CreateTime         : 2023/2/8 15:30
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/8 15:30 
@Version            : 1.0
@Description        : None
"""
import os
import time

import requests
from bs4 import BeautifulSoup
import json
import re

current_path = os.getcwd()
if not os.path.exists('data'):
    os.mkdir('data')

headers = {
    "Referer": "https://www.kugou.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

url_rank = "https://www.kugou.com/yy/html/rank.html"

# session 会自动保存 cookie
session = requests.Session()

# .text 得到文本
html = session.get(url_rank, headers=headers).text

# 得到 eaaid，可以从li标签的属性中提取，也可以从a标签中提取
# <li class=" " title="小鬼 - 花好月圆夜" data-index="0" data-eid="7zj68109">
# https://www.kugou.com/mixsong/7zicdve4.html
regex_eaaid = r"(?<=data-eid=\")(.*?)(?=\">)"
encode_album_audio_ids = re.findall(regex_eaaid, html)

for rank, eaa_id in enumerate(encode_album_audio_ids):
    # 跳转到歌曲详情页面
    url_song_detail = 'https://wwwapi.kugou.com/yy/index.php'
    params = {
        "r": "play/getdata",  # 固定值
        "callback": "jQuery191020418999164404728_1619018555322", # 随便写，服务端不校验
        "dfid": "1IQfTm0o6h7c3YmmBB4Qpy0P",  # cookie 的一部分，随便写，服务端不校验
        "appid": '1014',  # 固定值
        "mid": "7191cecd52885e73d850fcd4dca35104",  # cookie 的一部分，随便写，服务端不校验
        "platid": "4",  # 固定值
        "encode_album_audio_id": eaa_id,
        "_": str(round(time.time() * 1000))
    }

    song_detail = session.get(url_song_detail, params=params, headers=headers).text

    # 返回值是个文本，不是json 格式
    # 这里使用了最基本的字符串find 用法，然后截取。也可以直接使用 正则表达式
    start = song_detail.find('{"status"')
    end = song_detail.find('}})') + len('}}')
    song_json = json.loads(song_detail[start:end])
    # print(song_json)

    # song_duration = song_json['data']['timelength']
    # song_filesize = song_json['data']['filesize']
    # song_img = song_json['data']['img']
    # song_author_name = song_json['data']['author_name']
    song_name = song_json['data']['song_name']
    # song_lyrics = song_json['data']['lyrics']
    # song_bitrate = song_json['data']['bitrate']
    song_play_url = song_json['data']['play_url']
    # print(song_duration, song_filesize, song_img, song_author_name,
    #       song_name, song_lyrics, song_bitrate, song_play_url)

    with open("kugou/{}.mp3".format(song_name), 'wb') as f:
        f.write(session.get(song_play_url).content)
    print("{:0>2d} {}.mp3 下载完成".format(rank+1, song_name))
    break

if __name__ == '__main__':
    print(os.getcwd())


def parse_by_bs4(html):
    soup = BeautifulSoup(html, 'html.parser')

    # 选择div 标签下的所有 li 标签
    # div 标签的class是 pc_temp_songlist pc_rank_songlist_short
    # 另1种写法是soup.find("div", attrs={"class": "xxxx"})
    song_list = soup.select(".pc_temp_songlist.pc_rank_songlist_short li")
    for song in song_list:
        # 通过[]获取a标签的属性，如果是获取a标签文本，则是.text 方法
        rank = song.select('.pc_temp_num')[0].text.strip().strip("\n")
        title = song.select('a')[0]['title'].split('-')[1].strip().strip("\n")
        singer = song.select('a')[0]['title'].split('-')[0].strip().strip("\n")
        href = song.select('a')[0]['href']
        duration = song.select('.pc_temp_time')[0].text.strip().strip("\n")
        print(title, singer, rank, href, duration)
