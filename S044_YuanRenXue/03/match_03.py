# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : match_03.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/14 20:26
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/14 20:26 
@Version            : 1.0
@Description        :
Highlight: 这道题的关键在于保持 headers 字段的顺序发起请求，顺序不对，都得不到响应！！！！！！
通过session.headers属性来设置请求头有两个好处，一是请求头字典元素不会被打乱，二是只用最初在这里设置一次，之后的请求都不用重新设置请求参数，这也是session维持会话的优势
通过post、get等方法里传入headers参数是比较常用的携带请求头的方式，但是这些方法会自动打乱传入的请求头字典元素顺序
"""
import requests

session = requests.Session()
session.headers = {
    'Content-Length': '0',
    'Accept': '*/*',
    'Referer': 'https://match.yuanrenxue.cn/match/3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'yuanrenxue.project',
    'Cookie': 'sessionid=twym6wkrzkth35dl0jb5b8qrfe6i1sy4',
}

all_values = []
for page in range(1, 6):
    session.post("https://match.yuanrenxue.cn/jssm")
    url_api = 'https://match.yuanrenxue.cn/api/match/3?page=' + str(page)
    resp = session.get(url_api)
    values = resp.json()['data']
    # print(values)

    all_values = all_values + values

print(all_values)

# 统计1个列表中出现次数最多的元素
print(max(all_values, key=all_values.count))
