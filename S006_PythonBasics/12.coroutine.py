"""
# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
#File               : coroutine.py
#Project            : Crawler_2022
#CreateTime         : 2022/2/24 23:07
#Author             : biaobro
#Software           : PyCharm
#Last Modify Time   : 2022/2/24 23:07
#Version            : 1.0
#Description        : None
"""
import time


def func():
    print("I love you.")

    # sleep 让当前线程处于阻塞状态，CPU是不为我们工作的
    time.sleep(3)
    print("I do love you")


import asyncio


# time.sleep(3) 属于同步操作，会中断异步操作
async def afunc1():
    print("hello ,this is tom")
    # time.sleep(3)

    # await 让CPU去切换到其他操作
    await asyncio.sleep(3)
    print("hello ,this is tom")


async def afunc2():
    print("hello ,this is jerry")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("hello ,this is jerry")


async def afunc3():
    print("hello ,this is hank")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("hello ,this is hank")


# 将代码放到main函数
async def main():
    # 写法1
    # f1 = afunc1()
    # await f1

    # 写法2
    tasks = [
        asyncio.create_task(afunc1()),
        asyncio.create_task(afunc2()),
        asyncio.create_task(afunc3()),
    ]
    await asyncio.wait(tasks)


# input 程序也是处于阻塞状态
# requests.et(url) 在网络请求返回之前，程序也是处于阻塞状态
# 一般来讲，当程序处于IO操作的时候，线程都会处于阻塞状态
# 协程 就是当程序遇到IO操作时，可以选择性地切换到其他任务上
if __name__ == '__main__':
    # func()

    # g = afunc1()
    # print(g)  # g 是 coroutine 对象
    # asyncio.run(g)

    # f1 = afunc1()
    # f2 = afunc2()
    # f3 = afunc3()
    # tasks = [f1, f2, f3]
    # t1 = time.time()
    # asyncio.run(asyncio.wait(tasks))
    # t2 = time.time()
    #
    # # 直接使用 time.sleep 时，耗时9s多，即4+2+3
    # # 改用 await asyncio.sleep 后，耗时4s多，即耗时最长的那个
    # print(t2 - t1)
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)
