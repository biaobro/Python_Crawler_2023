# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : poco_js.py
@Project            : S057_PoCo
@CreateTime         : 2023/5/8 12:39
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/5/8 12:39 
@Version            : 1.0
@Description        : None
"""
import json
import requests
import time
import execjs

ctx = execjs.compile(open('lib.js', 'r', encoding='utf-8').read())

url_web = "https://web-api.poco.cn/"
url_xhr = "https://web-api.poco.cn/v1_1/rank/get_homepage_recommend_list"

ts_10bit = int(time.time())

# js 中如果包含 JSON.stringify，接收的参数形式为 字典
param_dict = {"start": 0, "length": 20, "works_category": "0", "time_point": ts_10bit}

# js 中如果不包含 JSON.stringify，接收的参数形式为 字符串，
# 如果是字符串，要么将空格都手动去掉，而且 ts_10bit 需要转成字符串形式
# o = '{"start":0,"length":20,"works_category":"0","time_point":'+str(ts_10bit)+'}'

# 要么就在做 json.dumps 时指定 separators 参数
param_str = json.dumps(param_dict, separators=(',', ':'))
sign_code = ctx.call('get_sign_code', param_str)
print(sign_code)

# Highlight: 这里要注意 post 提交 formData的形式
# 第1：字符串一行写不下，需要换行时，第1行末尾和第2行开头 都需要补引号
# 第2：字典键值对中的 值部分，也需要用引号包起来
# 第3：param 参数，因为是字典形式，外部不需要用引号包裹
formData = {
    'req': '{"version": "1.1.0", "app_name": "poco_photography_web", "os_type": "weixin", "is_enc": 0, "env": "prod", '
           '"ctime": "'+str(int(time.time()*1000))+'", "param": '+param_str+', "sign_code": "'+sign_code+'"}',
    'host_port': 'https://web-api.poco.cn'
}
print(formData)

# headers 不传也能成功
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Referer': 'https://photo.poco.cn/?classify_type=1&works_type=medal',
    # 'Origin': 'https://photo.poco.cn'
}
resp = requests.post(url_xhr, headers=headers, data=formData)
# print(resp.text)

data_list = resp.json()['data']['list']
for data in data_list:
    print(data)
