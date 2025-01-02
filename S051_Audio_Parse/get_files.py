# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : get_files.py
@Project            : S051_Audio_Parse
@CreateTime         : 2023/4/24 18:33
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/24 18:33 
@Version            : 1.0
@Description        : None
"""
import os


def get_files(foldername):
    for filepath,dirnames,filenames in os.walk(foldername):
        for filename in filenames:
            print(filename)


if __name__ == '__main__':
    folder = r"F:\Python\BB-Crawler-2023\S052_Tosound\Wav\baby\pixabay"
    get_files(folder)
