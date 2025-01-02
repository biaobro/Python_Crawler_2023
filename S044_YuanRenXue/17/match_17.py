# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : match_17.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/10 14:40
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/10 14:40 
@Version            : 1.0
@Description        : None
"""
import httpx
client = httpx.Client(http2=True)

url = "https://match.yuanrenxue.cn/api/match/17"
headers = {
    'user-agent': 'yuanrenxue.project',
    'cookie': 'sessionid=637u0zgwp6nq5lmu2yfh13u59qwfk3z7'
}

all_total = 0
for page in range(1,6):
    url = "https://match.yuanrenxue.cn/api/match/17?page=" + str(page)
    resp = client.get(url, headers=headers)

    values = resp.json()['data']
    print(values)

    p_total = 0
    for value in values:
        p_total = p_total + value['value']
    all_total = all_total + p_total

print(all_total)
