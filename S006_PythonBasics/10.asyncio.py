# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 10.asyncio.py
@Project            : Crawler_2023
@CreateTime         : 2023/2/1 18:29
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/1 18:29 
@Version            : 1.0
@Description        : None
"""

# 协程 是1个线程实现IO遇到阻塞就切换
import asyncio

async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)

async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)

tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2()),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))