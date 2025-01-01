# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 02.singleton.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/31 18:06
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/31 18:06 
@Version            : 1.0
@Description        : How to create singleton
"""
import threading


class Singleton:
    instance = None
    lock = threading.RLock()

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            if cls.instance:
                return cls.instance
            cls.instance = object.__new__(cls)
            return cls.instance


def task():
    obj = Singleton('x')
    print(obj)


for i in range(10):
    t = threading.Thread(target=task)
    t.start()
