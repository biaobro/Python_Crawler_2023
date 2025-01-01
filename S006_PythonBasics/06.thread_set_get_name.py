# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 06.thread_set_get_name.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/31 18:42
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/31 18:42 
@Version            : 1.0
@Description        : None
"""
import threading

def task(arg):
    name = threading.current_thread().name
    print(name)


for i in range(10):
    t = threading.Thread(target=task, args=(11,))
    t.name = "日出东方-{}".format(i)
    t.start()
