# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : match_20_normal.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/15 18:00
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/15 18:00 
@Version            : 1.0
@Description        : None
"""
from urllib.parse import urlencode
import hashlib
import requests
import time

"""
关键的JS代码，得到Payload
t = Date.parse(new Date());
var list = {
    "page": window.page,
    "sign": window.sign(window.page + '|' + t.toString()),
    "t": t,
};
"""


def get_sign(page, ts):
    sign = hashlib.md5((str(page) + "|" + str(ts) + 'D#uqGdcw41pWeNXm').encode()).hexdigest()
    return sign

all_total = 0
for page in range(1, 6):
    ts = int(time.time()) * 1000
    payload = {
        'page': page,
        'sign': get_sign(page, ts),
        't': ts
    }
    url = "https://match.yuanrenxue.cn/api/match/20?" + urlencode(payload)
    print(url)

    headers = {
        'user-agent': 'yuanrenxue.project',
        'cookie': 'sessionid=ntkvbzoagc6tpauaugwk3b0jdrdbuba9'
    }
    resp = requests.get(url, headers=headers)
    # print(resp.text)

    datas = resp.json()['data']
    print(datas)

    p_total = 0
    for data in datas:
        p_total = p_total + data['value']

    all_total = all_total + p_total

print(all_total)
