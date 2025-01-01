# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 15.regex.py
@Project            : Crawler_2022
@CreateTime         : 2022/1/23 16:10
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2022/1/23 16:10 
@Version            : 1.0
@Description        : B站IT私塾
"""
import re


# 正则表达式 判断字符串是否符合指定标准
# 创建模式对象
# 建议在被匹配的字符串前面加上 r,不用担心被转义
def regexcheck():
    pattern = re.compile('AA')

    # search 方法只返回第1个匹配对象,
    # response = pattern.search('BBCAADDEEAA')

    # 可以简化写法
    # response = re.findall('AA', 'BBCAADDEEAA')

    # 匹配规则
    # response = re.findall('[D-E]', 'sdfEAb')
    # response = re.findall('[D-K]+', 'sdfEAbEF')

    # 1st param :
    # 2nd param :
    # 3rd param :
    # sub : 在参数3中,找到参数1,用参数2替换
    # response = re.sub('a', 'A', 'asdfEAbEF')

    # 建议在被匹配的字符串前面加上 r,不用担心被转义
    # r 的用法
    response = "'\aabd-\'"
    response_r = r"'\aabd-\'"
    print(response, response_r)


if __name__ == '__main__':
    regexcheck()
