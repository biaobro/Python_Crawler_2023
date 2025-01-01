# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 08.process_start_join.py
@Project            : Crawler_2023
@CreateTime         : 2023/2/1 16:55
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/1 16:55 
@Version            : 1.0
@Description        : None
"""
import multiprocessing
import time
import threading


def func(param):
    time.sleep(1)
    print(f"thread {param} in sub process")

def task(param):
    for i in range(10):
        t = threading.Thread(target=func, args=(i,))
        t.start()
    print(f"there are {len(threading.enumerate())} threads in this sub process.")
    time.sleep(2)

    print('task', param)


if __name__ == '__main__':
    # windows 下只有 spawn 模式
    multiprocessing.set_start_method("spawn")

    p = multiprocessing.Process(target=task, args=('xxx',))

    p.daemon = False
    p.start()

    # 如果 daemon 为 true, 主线程结束，程序就结束
    print("if daemon is True, main process will not wait sub process. you won't see output from sub process.")
