# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 03.thread_start.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/31 18:16
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/31 18:16 
@Version            : 1.0
@Description        : None
"""
import threading

loop = 1000000
number = 0


def _add(count):
    global number
    for i in range(count):
        number += 1


t = threading.Thread(target=_add, args=(loop,))
t.start() # 线程已经准备完毕，等待CPU来调度，具体时间由CPU决定
t.join() # 等待当前线程任务执行完毕后才向下执行

# 等待子线程结束后，才运行
# 表现为 number 一定是 1000000
print(number)
