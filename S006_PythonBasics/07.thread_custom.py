# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 07.thread_custom.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/31 18:55
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/31 18:55 
@Version            : 1.0
@Description        : None
"""
import threading


class MyThread(threading.Thread):
    def run(self):
        print('the thread is being processed.', self._args)


t = MyThread(args=(100,))
t.start()
