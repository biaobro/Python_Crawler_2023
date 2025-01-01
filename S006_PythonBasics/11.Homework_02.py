# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 11.Homework_01.py
@Project            : Crawler_2023
@CreateTime         : 2023/2/1 18:50
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/1 18:50 
@Version            : 1.0
@Description        : None
"""
import os
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager
import time


def task(file_name):
    ip_set = set()
    total_count = 0
    ip_count = 0
    file_path = os.path.join("logs", file_name)
    file_obj = open(file_path, mode='r', encoding='utf-8')
    for line in file_obj:
        if not line.strip():
            continue
        user_ip = line.split(" - - ", maxsplit=1)[0].split(",")[0]
        total_count += 1
        if user_ip in ip_set:
            continue
        ip_count += 1
        ip_set.add(user_ip)
    time.sleep(1)
    return {"total": total_count, "ip": ip_count}


def outer(info, file_name):
    def done(res, *args, **kwargs):
        info[file_name] = res.result()
    return done


def run():
    info = {}
    pool = ProcessPoolExecutor(4)

    for file_name in os.listdir("logs"):
        future = pool.submit(task, file_name)

        # 这个回调函数 是被主进程执行的，所以 info 天然就是1份
        future.add_done_callback(outer(info,file_name))

    pool.shutdown(True)
    for k, v in info.items():
        print(k, v)


if __name__ == '__main__':
    run()
