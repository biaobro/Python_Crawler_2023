#!/usr/bin/python3
# Coding: UTF-8
"""
# Created On: 2021/4/20 23:22
# Author: biaobro
# Project: Crawler
# File Name: crawler_kugou.py
# Description:
"""
import requests
from bs4 import BeautifulSoup
import re
import json
import os

file_path = os.getcwd()
if not os.path.exists('data'):
    os.mkdir('data')

headers = {"Referer": "https://www.kugou.com/",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}

url_outside = "https://www.kugou.com/yy/html/rank.html"
html_outside = requests.get(url_outside, headers=headers)

# 用beautifulsoup解析,得到包含排行信息的列表
soup_outside = BeautifulSoup(html_outside.text, 'html.parser')
lis = soup_outside.select('.pc_temp_songlist.pc_rank_songlist_short li')

# 可以构造1个 rank 为键key,名称为值value 的字典
# for li in lis:
#     rank = li.select('.pc_temp_num')[0].text.strip().replace(" ", "").replace("\n", "")
#     title = li.select('a')[0].text
#     length = li.select(' .pc_temp_time')[0].text.strip().replace(" ", "").replace("\n", "")
#     href = li.select('a')[0]['href']
#     print(rank, title, length, href)


# regex_hash = r"\"Hash\":\"(.*?)\""
# hashes = re.findall(regex_hash, html_outside.text)
# for hash in hashes:
#     print(hash)

regex_songs = r"global.features = (.*?);"

# re.findall() 的结果是列表
# 列表取出第一个元素的结果是字符串
# 字符串想要再转成列表, 用json.loads
song_visit_infos = json.loads(re.findall(regex_songs, html_outside.text)[0])

hash_code = ''
album_id = ''
for i in range(len(song_visit_infos)):
    # print(song_visit_infos[i])
    hash_code = song_visit_infos[i]['Hash']
    # name = song_visit_infos[i]['FileName']
    # time_length = song_visit_infos[i]['timeLen']
    # size = song_visit_infos[i]['size']
    album_id = song_visit_infos[i]['album_id']
    # encrypt_id = song_visit_infos[i]['encrypt_id']
    # print(name, hash_code, time_length, size, album_id, encrypt_id)

    url_song_detail = 'https://wwwapi.kugou.com/yy/index.php'
    params = {
        "r": "play/getdata",
        "callback": "jQuery191020418999164404728_1619018555322",
        "hash": hash_code,
        "dfid": "1IQfTm0o6h7c3YmmBB4Qpy0P",
        "mid": "7191cecd52885e73d850fcd4dca35104",
        "platid": "4",
        "album_id": album_id,
        "_": "1619018555323"
    }

    song = requests.get(url_song_detail, params=params, headers=headers)
    print("song.text",song.text)
    start = song.text.find('{"status"')
    end = song.text.find('}})') + len('}}')
    song_json = json.loads(song.text[start:end])
    print(song_json)

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

    with open("data/{}.mp3".format(song_name), 'wb') as f:
        f.write(requests.get(song_play_url).content)
    print("{:0>2d} {}.mp3 下载完成".format(i, song_name))







