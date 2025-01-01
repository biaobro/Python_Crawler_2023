# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 08.process_basic.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/31 18:16
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/31 18:16 
@Version            : 1.0
@Description        : None
"""
# Thread 线程是CPU可以调度的最小单元，是真正工作的单位
# Process 进程是资源分配的最小单元，1个进程可以包含多个进程，多个进程共享资源
# 由于GIL全局锁的存在，1个进程中同1时刻只有1个线程可以被CPU调度
# 默认在程序执行时，会创建1个进程，内部再创建1个线程
# 进程适用于计算密集型任务
# 线程适用于IO密集型任务，如爬虫、文件操作
# 直观上看，多进程消耗的资源要多于多线程

# GIL 是CPython 解释器特有的1个东西。字典、列表等对象的线程数据安全，正是得益于GIL锁的存在

import multiprocessing
import requests
import time

video_list = [
    ('Whale',
     'https://mazwai.com/videvo_files/video/free/2019-05/small_watermarked/190416_08_Whales_Drone_004_preview.webm'),
    ('Waves', 'https://mazwai.com/videvo_files/video/free/2018-01/small_watermarked/171124_H1_006_preview.webm'),
    ('Waterfall', 'https://mazwai.com/videvo_files/video/free/2017-12/small_watermarked/171124_B1_HD_001_preview.webm')
]


def task(file_name, video_url):
    res = requests.get(video_url)
    with open(file_name, mode='wb') as f:
        f.write(res.content)
    print(time.time())


if __name__ == '__main__':
    print(time.time())
    for name, url in video_list:
        t = multiprocessing.Process(target=task, args=(name, url))
        t.start()
