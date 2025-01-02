# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : match_20_jsrpc.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/15 23:06
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/15 23:06 
@Version            : 1.0
@Description        : None
"""
import ast
import requests


def get_params(page):
    params = {
        "group": "match20",
        "name": "yuanrenxue",
        "action": "ShiGuang",
        "param": str(page)
    }
    try:
        res = requests.post("http://localhost:12080/go", params=params)
        res = res.json()
        print(res)

        # 这个写法是把
        # '{"page":"1","sign":"df47c82c991462661cfc3642369039a3","t":1681818656000,"status":0}'
        # 转换成
        # {'page': '1', 'sign': 'df47c82c991462661cfc3642369039a3', 't': 1681818656000, 'status': 0}
        # 否则直接按json 或 字典方式是读不出来的
        params = ast.literal_eval(res.get("data"))
        print(params)
        return params
    except:
        return False


get_params(1)

