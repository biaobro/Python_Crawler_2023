# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : match_13.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/9 16:38
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/9 16:38 
@Version            : 1.0
@Description        : None
"""
import requests
import re

url = "https://match.yuanrenxue.cn/match/13"

headers = {
    'user-agent': 'yuanrenxue.project',

    # 在 header 里不要单独加 cookie:session
    # 'cookie':'sessionid=4gjc34du341pmcs3lmvljedgpbmgd69k'
}

session = requests.Session()

# 需要单独向 session 添加这个 sessionid，以请求第4页。第5页
session.cookies['sessionid'] = '4gjc34du341pmcs3lmvljedgpbmgd69k'

# 第1个请求会返回一段 JS 代码，这段代码可以得到 yuanrenxue_cookie
resp = session.get(url, headers=headers)
print(session.cookies)

# 提取 JS 代码
regex_cookie = r"(?<=cookie=).*?(?=\+';)"
cookie = re.findall(regex_cookie, resp.text)[0]

# 执行 JS 代码，得到 cookie
cookie = cookie.replace('(', '').replace(')', '')
cookie = eval(cookie)
cookie = cookie.split('=')[1]
# print(cookie)

# 向 session 中添加 cookie
session.cookies['yuanrenxue_cookie'] = cookie

all_total = 0
for page in range(1, 6):
    url = "https://match.yuanrenxue.cn/api/match/13?page=" + str(page)
    print(url)

    # 请求 api 接口
    resp = session.get(url, headers=headers)

    # 拆解数据
    datas = resp.json()['data']
    p_total = 0
    for data in datas:
        val = data['value']
        p_total = p_total + val
    all_total = all_total + p_total
print(all_total)
