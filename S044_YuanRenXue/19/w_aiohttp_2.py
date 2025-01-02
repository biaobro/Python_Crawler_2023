# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : w_aiohttp_2.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/14 13:30
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/14 13:30 
@Version            : 1.0
@Description        : None
"""
import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

        async with session.get('https://match.yuanrenxue.cn/api/match/19') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            # text()函数相当于requests中的r.text，r.read()相当于requests中的r.content
            html = await response.text()
            print("Body:", html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())