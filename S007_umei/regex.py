# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 15.regex.py
@Project            : Crawler_2023
@CreateTime         : 2023/2/4 22:45
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/4 22:45 
@Version            : 1.0
@Description        : None
"""

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

# regex = r"(\d*?)_?(\d+)"
regex = r"(?<=_)(\d+)"
# regex = r"\d+_?\d+"

test_str = "https://www.umeitu.com/img/52419_1.html"

subst = "3"

# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0, re.MULTILINE)
# result = re.findall(regex, test_str)

if result:
    print(result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
