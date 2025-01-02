# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : shanbay.py
@Project            : S066_ShanBay_扇贝单词
@CreateTime         : 2023/6/11 18:53
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/6/11 18:53 
@Version            : 1.0
@Description        : None
"""
import json

import requests
import execjs

# 在登录态下才能获取到数据，网页操作路径
# 登录态需要更新参数 cookie
headers = {
    'authority': 'apiv3.shanbay.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'cookie': '_ga=GA1.2.1683952659.1701592766; _gat=1; sajssdk_2015_cross_new_user=1; sessionid="e30:1r9i1q:j8bdJUyxlqrk3wGoscp751pOofU"; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU1NzEzMDEzLCJleHAiOjE3MDI0NTc1MDAsImV4cF92MiI6MTcwMjQ1NzUwMCwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJQaG9uZV9hODE2ODc1Y2EwYzU4ZGNlIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiI3YTY1ZGI1MDkxYjgxMWVlOTIyYTU2ODk1NGQ4MTNmMSJ9.zUaa_76afFWN5kyKCytV1MhiLTCtMo62QQ6jbGoXbGI; csrftoken=570d7df12aed59f4d6c43bb018690d00; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22grgxbq%22%2C%22first_id%22%3A%2218c2ed5179f7ad-0b5f39cb941e42-16525634-1128960-18c2ed517a0dd5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%AB%99%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%7D%2C%22%24device_id%22%3A%2218c2ed5179f7ad-0b5f39cb941e42-16525634-1128960-18c2ed517a0dd5%22%7D',
    'origin': 'https://web.shanbay.com',
    'pragma': 'no-cache',
    'referer': 'https://web.shanbay.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    # 'x-csrftoken': '70cc037c28fd38cf481361b1ef2a8f57',
}

# 以前都是用字典，元组这种写法也可以
params = (
    ('ipp', '10'),
    ('page', '1'),
)

# js 逆向思路，根据 api 请求信息，搜索 "unlearned_items"
ctx = execjs.compile(open('webpack.js', 'r', encoding='utf-8').read())

books = {
    '托福必备词汇': 'juuxc'
}

# 封装请求地址
url = f"https://apiv3.shanbay.com/wordsapp/user_material_books/{books['托福必备词汇']}/learning/words/unlearned_items"
print(url)

# 发起请求
resp_api = requests.get(url, headers=headers, params=params)

# 打印响应码
print(resp_api)

# 从返回的json中拿到数据
data = resp_api.json()['data']

# 调用js代码，decrypt数据
resp_js = json.loads(ctx.call('decrypt', data))
print(resp_js)

for word in resp_js['objects']:
    print(word['vocab_with_senses']['word'])