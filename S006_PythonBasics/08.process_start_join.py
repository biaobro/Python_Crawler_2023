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


def task(param):
    print('task', param)


if __name__ == '__main__':
    # windows 下只有 spawn 模式
    multiprocessing.set_start_method("spawn")

    p = multiprocessing.Process(target=task, args=('xxx',))
    p.start()

    # 和 thread 类似，也是等待 p 进程执行完毕后才继续
    p.join()

    print("the sub process has been finished. now back to main process.")
