# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : sync.py
@Project            : S009_Asyncio_Demo
@CreateTime         : 2025/1/5 10:26
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/1/5 10:26 
@Version            : 1.0
@Description        : None
"""

import requests


def do_requests():
    resp = requests.get('https://baidu.com')
    print('baidu.com =>', resp.status_code)


def main():
    for _ in range(0, 10):
        do_requests()


if __name__ == '__main__':
    main()


# 控制台运行 time python sync.py
