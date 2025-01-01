# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 05.thread_setDaemon.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/31 18:37
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/31 18:37 
@Version            : 1.0
@Description        : None
"""
import threading
import time


def task(arg):
    time.sleep(5)
    print('task')


t = threading.Thread(target=task, args=(11,))

# 旧版本的写法是t.setDaemon(True/False)
# True 表示 主线程结束时，子线程也自动关闭
# False 表示 主线程要等待子线程执行完毕，才能结束
t.daemon = True
t.start()

print('end')