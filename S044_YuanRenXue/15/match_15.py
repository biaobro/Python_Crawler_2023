# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : match_15.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/8 21:41
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/8 21:41 
@Version            : 1.0
@Description        : None
"""
import requests
import time
from urllib.parse import urlencode
import pywasm
import random
import math


# t1 = parseInt(Date.parse(new Date()) / 1000 / 2);
# t2 = parseInt(Date.parse(new Date()) / 1000 / 2 - Math.floor(Math.random() * (50) + 1));
# return window.q(t1, t2).toString() + '|' + t1 + '|' + t2;

def get_m():
    t1 = int(int(time.time()) / 2)
    t2 = int(int(time.time()) / 2) - math.floor(random.random() * 50 + 1)
    # pywasm.on_debug()
    runtime = pywasm.load('main.wasm')
    r = runtime.exec('encode', [t1, t2])
    m = str(r) + '|' + str(t1) + '|' + str(t2)
    return m

total = 0
for page in range(1, 6):
    p_total = 0
    payload = {
        'm': get_m(),
        'page': page,
    }
    headers = {
        'user-agent': 'yuanrenxue.project',
        'referer': 'https://match.yuanrenxue.cn/match/15',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'cookie': 'sessionid=zep84w7nriruop5atai0ol4kyptyi2dz; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1680943810,1680945172,1680950014,1680959269; qpfccr=true; no-alert3=true; tk=8511286153795358991; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1680943953,1680950033,1680959333; yuanrenxue_cookie=1680963508|5NOrPp5eGZLAK52uUOJvtM797T8P2hh7997nPpLhHown2jUgRFQY3A9p3m2WQfKxYyPCIjK2zL5ytlAgPkeQF4SVUWNdIBLjMJ179pN1XIYlMEH; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1680963723; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1680965055'
    }
    url = 'https://match.yuanrenxue.cn/api/match/15?' + urlencode(payload)
    print(url)
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    values = resp.json()['data']

    for value in values:
        p_total = p_total + value['value']

    total = total + p_total

print(total)
