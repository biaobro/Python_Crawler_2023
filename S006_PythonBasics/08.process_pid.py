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
import os


def task(param):
    print(f'pid of sub process is {os.getpid()}, my parent process pid is {os.getppid()}' )
    print('task', param)


if __name__ == '__main__':
    print('pid of main process is ', os.getpid())
    # windows 下只有 spawn 模式
    multiprocessing.set_start_method("spawn")

    p = multiprocessing.Process(target=task, args=('xxx',))
    p.daemon = False
    p.start()

    print("the sub process has been finished. now back to main process.")
