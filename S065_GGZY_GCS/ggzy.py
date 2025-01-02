# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : ggzy.py
@Project            : S065_GGZY_GCS_金昌市公共资源交易网
@CreateTime         : 2023/6/11 16:31
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/6/11 16:31 
@Version            : 1.0
@Description        : None
"""
import requests
import execjs

ctx = execjs.compile(open('app.js', 'r', encoding='utf-8').read())

url = "https://ggzy.jcs.gov.cn/pro-api-construction/construction/bidder/bidSection/list?"

payload = {
    'pageNum': 1,
    'pageSize': 20,
    'releaseTime': '',
    'search': '',
    'informationType': 'ANNOUNCEMENT',
    'departmentId': '',
    'projectType': 'SZFJ',
    'informationName': 'ZBGG'
}

# 注意 get 提交参数用的参数名是 params, 而不是 data
resp = requests.get(url, params=payload)
items = resp.json()['rows']

for item in items:
    print(item)
    projectId = str(item['projectId'])

    eProjectId = ctx.call('c', projectId)
    eProjectType = ctx.call('c', 'ZBGG')

    url = f"https://ggzy.jcs.gov.cn/website/anno/index?projectId={eProjectId}&projectInfo={eProjectType}"
    print(url)

    break
