# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : match_01.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/8 17:14
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/8 17:14 
@Version            : 1.0
@Description        : None
"""
import requests
import execjs
from urllib.parse import urlencode

ctx = execjs.compile(open('match_01.js', 'r', encoding='utf-8').read())

headers = {
    'user-agent': 'yuanrenxue.project',
    "Cookie": "qpfccr=true; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1680943810,1680945172,1680950014; no-alert3=true; tk=8511286153795358991; sessionid=868dkylwgr4karp9jg6nrazrik1tj3i0; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1680943953,1680950033; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1680950033; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1680951355"
}

total = 0
count = 0

for i in range(1, 6):
    p_total = 0
    p_count = 0

    m = ctx.call('get_m')
    payload = {
        'page': i,
        'm': m,
    }
    url = "https://match.yuanrenxue.cn/api/match/1?" + urlencode(payload)
    # print(url)

    resp = requests.get(url)
    # print(resp.text)
    values = resp.json()['data']
    print(values)

    for value in values:
        p_total = p_total + value['value']

    p_count = p_count + len(values)
    print(p_total, p_count)

    total = total + p_total
    count = count + p_count

print(f'total:{total}, count:{count}, average:{total / count}')
