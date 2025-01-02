# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : w_aiohttp_1.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/14 13:10
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/14 13:10 
@Version            : 1.0
@Description        : None
"""
import asyncio
import aiohttp
import json


async def html(url: str) -> str:
    code = 'utf-8'
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'cookie': 'sessionid=4gjc34du341pmcs3lmvljedgpbmgd69k'
    }
    async with aiohttp.ClientSession() as session:
        # 老版本aiohttp没有verify参数，如果报错卸载重装最新版本
        async with session.get(url, headers=headers, timeout=10, verify_ssl=False) as r:
            # text()函数相当于requests中的r.text，r.read()相当于requests中的r.content
            resp = await r.text()
            return resp

datas = []
for page in range(1, 6):
    url = 'https://match.yuanrenxue.cn/api/match/19?page=' + str(page)
    loop = asyncio.get_event_loop()
    task = loop.create_task(html(url))
    loop.run_until_complete(task)
    # 对需要ssl验证的网页，需要250ms左右等待底层连接关闭
    loop.run_until_complete(asyncio.sleep(0.25))
    data = json.loads(task.result())['data']
    # print(data)
    datas = datas + data
    # loop.close()

all_total = 0
for data in datas:
    # print(data)
    all_total = all_total + data['value']
print(all_total)
