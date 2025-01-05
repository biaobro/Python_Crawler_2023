# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : async.py
@Project            : S009_Asyncio_Demo
@CreateTime         : 2025/1/5 10:24
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/1/5 10:24 
@Version            : 1.0
@Description        : None
"""

import aiohttp
import asyncio


def do_requests(session):
    return session.get('https://baidu.com')


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(0, 10):
            tasks.append(do_requests(session))

        results = await asyncio.gather(*tasks)
        for r in results:
            print('baidu.com =>', r.status)


if __name__ == '__main__':
    asyncio.run(main())
