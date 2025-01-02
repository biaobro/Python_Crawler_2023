# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : match_12.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/8 21:20
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/8 21:20 
@Version            : 1.0
@Description        : 用Python的Base64 包，实现了 JS中的 btoa
"""
import requests
import base64
from urllib.parse import urlencode

url_template = "https://match.yuanrenxue.cn/api/match/12?page=1&m=eXVhbnJlbnh1ZTE="

headers = {
    'user-agent': 'yuanrenxue.project',
    'cookie':'qpfccr=true; sessionid=868dkylwgr4karp9jg6nrazrik1tj3i0; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1680943810,1680945172,1680950014,1680959269; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1680943953,1680950033,1680959333; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1680959333; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1680960716'
}

total = 0
for page in range(1, 6):
    p_total = 0

    # 用于替代 JS 中的 windows.btoa()
    m = base64.encodebytes(('yuanrenxue' + str(page)).encode("utf8"))
    m = m.decode("utf8").strip()

    payload = {
        'page': page,
        'm': m,
    }
    url = "https://match.yuanrenxue.cn/api/match/12?" + urlencode(payload)
    print(url)

    resp = requests.get(url, headers=headers)
    print(resp.text)

    values = resp.json()['data']
    # print(values)

    for value in values:
        p_total = p_total + value['value']

    total = total + p_total

print(total)

