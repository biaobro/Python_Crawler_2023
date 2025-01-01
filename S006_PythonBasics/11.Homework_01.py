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

def task(file_name, count_dict):
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
    count_dict[file_name] = {"total":total_count, "ip":ip_count}
    time.sleep(1)

def run():
    pool = ProcessPoolExecutor(4)
    with Manager() as manager:
        count_dict = manager.dict()

        for file_name in os.listdir("logs"):
            pool.submit(task, file_name, count_dict)

        pool.shutdown(True)
        for k,v in count_dict.items():
            print(k,v)

if __name__ == '__main__':
    run()
