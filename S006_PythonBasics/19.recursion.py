# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 19.recursion.py
@Project            : S006_tech
@CreateTime         : 2023/3/3 22:35
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/3 22:35 
@Version            : 1.0
@Description        : None
"""

import os

path_local = r'Ex_a'


def func(path, layer):
    lst = os.listdir(path)
    for name in lst:
        real_path = os.path.join(path, name)
        if os.path.isdir(real_path):
            print("|--" * layer + name)
            func(real_path, layer+1)
        else:
            print("|--" * layer + name)

            # 修改文件
            # ##open(real_path, mode='w').write("1")


if __name__ == '__main__':
    func(path_local, 1)
