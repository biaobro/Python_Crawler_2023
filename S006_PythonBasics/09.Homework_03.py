# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 09.Homework_03.py
@Project            : Crawler_2023
@CreateTime         : 2023/2/1 13:48
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/1 13:48 
@Version            : 1.0
@Description        : None
"""
import threading

def task(row_list):
    num_list = [int(row.split(",")[-1]) for row in row_list]
    result = sum(num_list)
    print(result)

def run():
    file_obj = open('data.txt', mode='r', encoding='utf-8')
    
    # 读1行，跳过表头
    file_obj.readline()
    
    row_list = []
    for line in file_obj:
        row_list.append(line.strip())
        if len(row_list) == 100:
            t = threading.Thread(target=task, args=(row_list,))
            t.start()

            # 创建新的空列表，如果用 row_list.clear() 会把已经得到的数据清空
            row_list = []
    if row_list:
        t = threading.Thread(target=task, args=(row_list,))
        t.start()
    file_obj.close()


if __name__ == '__main__':
    run()
