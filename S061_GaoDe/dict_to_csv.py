# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : dict_to_csv.py
@Project            : S061_GaoDe
@CreateTime         : 2023/5/10 16:23
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/5/10 16:23 
@Version            : 1.0
@Description        : None
"""


# 方法1 和 方法4

def dict_to_csv_m1(dictData):
    import pandas as pd
    df = pd.DataFrame(dictData)
    df.to_csv('data.csv', index=False, header=True)


def dict_to_csv_m2(dictData):
    import csv
    # data = {'A': 'X1', 'B': 'X2', 'C': 'X3'}
    with open('data.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=dictData.keys())
        writer.writeheader()
        writer.writerow(dictData)


def dict_to_csv_m3(dictData):
    '''
    返回一个 CSV 字符串，而不是写进一个 CSV 文件，使用pandas.DataFrame.to_csv() 函数，不需要文件路径参数。返回值是字典的 CSV 字符串表示
    :param dictData:
    :return:
    '''
    import pandas as pd

    data = [{'A': 'X1', 'B': 'X2', 'C': 'X3'},
            {'A': 'Y1', 'B': 'Y2', 'C': 'Y3'}]

    df = pd.DataFrame(data)
    my_csv_string = df.to_csv(index=False)

    print(my_csv_string)


def dict_to_csv_m4(dictData):
    '''
    输出csv 文件，每行一个*(key, value)*对，没有标题行
    :param dictData:
    :return:
    '''
    import csv
    # data = {'A': 42, 'B': 41, 'C': 40}
    # 在写作模式下打开文件，并使用newline='' 参数来防止空行
    with open('data.csv', 'w', newline='') as f:
        # 创建一个CSV写入器对象
        writer = csv.writer(f, fieldnames=dictData.keys())
        # 遍历字典中的（键，值）对，使用 [dict.items()]方法对字典中的(key, value)对进行迭代
        for row in dictData.items():
            # 通过在writer.writerow() 方法中传递，一次写一个(key, value) 元组
            writer.writerow(row)


def dict_to_csv_m5(dictData):
    '''
    不用第三方库
    :param dictData:
    :return:
    '''
    salary = [{'Name': 'Alice', 'Job': 'Data Scientist', 'Salary': 122000},
              {'Name': 'Bob', 'Job': 'Engineer', 'Salary': 77000}, {'Name': 'Carl', 'Job': 'Manager', 'Salary': 119000}]

    with open('data.csv', 'w') as f:
        f.write(','.join(dictData[0].keys()))
        f.write('n')
        for row in dictData:
            f.write(','.join(str(x) for x in row.values()))
            # 在每一行的后面，你放置换行符'n'
            f.write('n')
