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

# 程序执行时会启动1个进程，进程中有1个主线程，用于执行t之外的代码
# 表现为这里打印的是随机数字，而不是1000000
print(number)
