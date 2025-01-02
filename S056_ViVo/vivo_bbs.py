# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : vivo_bbs.py
@Project            : S056_ViVo
@CreateTime         : 2023/5/8 11:27
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/5/8 11:27 
@Version            : 1.0
@Description        : None
"""
import requests
import time
import json
import execjs
import pandas as pd

ctx = execjs.compile(open("app.js", 'r').read())

url = "https://bbs.vivo.com.cn/api/community/index"


def get_page(page):
    ts = int(time.time() * 1000)
    nonce = ctx.call("get_nonce", ts)

    payload = {
        "lastId": "",
        "pageNum": page,
        "pageSize": 10,
        "imgSpecs": ["t577x324", "t577x4096"],
        "timestamp": ts,
        "nonce": nonce
    }

    # 这条必须写
    headers = {'content-type': 'application/json;charset=UTF-8'}

    resp = requests.post(url, headers=headers, data=json.dumps(payload))

    datas = resp.json()['data']['list']

    data_list = []
    for data in datas:
        bbsName = data['author']['bbsName']
        name = data['forum']['name']
        summary = data['summary']
        tid = data['tid']
        data_list.append({
            'bbsName': bbsName,
            'name': name,
            'summary': summary,
            'tid': tid
        })
    return data_list


if __name__ == '__main__':
    data_all = []
    for idx in range(2):
        data = get_page(idx)
        data_all.extend(data)

    df = pd.DataFrame(data_all)
    print(df)
    df.to_csv('data.csv',encoding='utf-8')



