# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 09.Homework_01.py
@Project            : Crawler_2023
@CreateTime         : 2023/2/1 12:52
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/1 12:52 
@Version            : 1.0
@Description        : add_done_callback
"""
import string
import random
import threading
from concurrent.futures import ThreadPoolExecutor


def generate_data():
    with open('data.txt', mode='w', encoding='utf-8', ) as f:
        for i in range(10000):
            sub_str = ''
            for j in range(20):
                sub_str += random.choice(string.ascii_uppercase)
            num1 = random.randint(1, 10)
            num2 = random.randint(10, 100)
            final_str = sub_str + ',' + str(num1) + ',' + str(num2) + '\n'
            f.write(final_str)


def count(n):
    with open('data.txt', mode='r', encoding='utf-8', ) as f:
        start = 1 + (n - 1) * 1000
        end = start + 100 + 1
        res = 0
        for line in f.readlines()[start:end]:
            num = int(line.split(",")[2])
            res += num
    return res


def summary(response):
    print(response.result())


if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)
    future_list = []
    for i in range(1, 10 + 1):
        future = pool.submit(count, i)

        # 这种方法没有办法实现将线程结果相加
        future.add_done_callback(summary)

