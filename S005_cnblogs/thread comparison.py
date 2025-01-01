# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : thread.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/26 16:44
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/26 16:44 
@Version            : 1.0
@Description        : None
"""
import cnblogs
import threading
import time


def single_thread():
    print("single thread start")
    for url in cnblogs.urls:
        cnblogs.craw(url)
    print("single thread end")


def multi_thread():
    print("multi thread start")
    threads = []
    for url in cnblogs.urls:
        threads.append(threading.Thread(target=cnblogs.craw, args=(url,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("multi thread end")


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("single thread cost : ", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi thread cost : ", end - start, "seconds")
