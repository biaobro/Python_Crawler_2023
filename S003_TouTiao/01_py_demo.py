# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 01_py_demo.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/23 13:24
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/23 13:24 
@Version            : 1.0
@Description        : None
"""

import os
import subprocess


res = subprocess.getoutput('node 01_js_demo.js')

print(res)