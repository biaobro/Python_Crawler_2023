# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 18.writeToExcel.py
@Project            : Crawler_2022
@CreateTime         : 2022/1/23 19:14
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2022/1/23 19:14 
@Version            : 1.0
@Description        : B站IT私塾
"""
import xlwt
import xlsxwriter


# xlwt 不支持 xlws, 只支持到 xls
def xlwtcheck():
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    # worksheet.write(0, 0, 'hello')  # 字体默认 Arial
    for i in range(0, 9):
        for j in range(0, i+1):
            worksheet.write(i, j, '%d * %d = %d' % (i+1, j+1, (i+1) * (j+1)))
    workbook.save('xlwt.xls')


def xlsxcheck():
    workbook = xlsxwriter.Workbook('xlsxwriter.xlsx')
    worksheet = workbook.add_worksheet('sheet1')
    worksheet.write(0, 0, 'world')  # 字体默认 宋体
    workbook.close()


if __name__ == '__main__':
    xlwtcheck()
    xlsxcheck()
