"""
# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
#File               : lottery_selenium.py
#Project            : Crawler_2022
#CreateTime         : 2022/2/21 20:58
#Author             : biaobro
#Software           : PyCharm
#Last Modify Time   : 2022/2/21 20:58
#Version            : 1.0
#Description        : B站樵夫视频
    # 说明
    1，selenium 方式获取数据目测要比 requests + bs4 慢不少
    2，切换【最近100期】有不同的实现方式，可以 selenium 拟人操作，也可以通过XHR找到链接
    3，driver 的路径现在是写死的。和浏览器版本不匹配会无法使用。
    4，命令行安装 .\pip.exe install --index-url https://mirrors.aliyun.com/pypi/simple/ matplotlib
"""
import csv
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
import os

import init_webdriver

folder_name = r'..\\'
file_name = r'chromedriver.exe'

# 500彩票，双色球，历史数据
url = 'https://datachart.500.com/ssq/history/history.shtml'

# 【最近100期】按钮对应的链接，页面代码里不显示，但可以通过XHR捕获得到
# 可以直接请求这个地址，获取数据，也可以selenium 点击按钮
url_limit = 'https://datachart.500.com/ssq/history/newinc/history.php?limit=100&sort=0'


def getData():
    driver_path = init_webdriver.driver_seek(folder_name, file_name)
    if driver_path is None:
        driver_path = r'..\\'
        init_webdriver.driver_download(driver_path)

    options = webdriver.ChromeOptions()
    # options.add_argument(r"--headless")
    # options.add_argument(r"user-data-dir=data")

    # 初始化浏览器
    browser = webdriver.Chrome(service=ChromeService(driver_path), options=options)

    # 地址必须带协议，否则报错参数不正确
    browser.get(url)
    time.sleep(1)

    # 点击【最近100期】按钮
    browser.find_element(By.XPATH,
                         '//*[@id="container"]/div/table/tbody/tr[1]/td/div/div[1]/div/table/tbody/tr/td[2]/a[3]').click()

    # 找到1000行 tr，注意这里是 find_elements
    tr_list = browser.find_elements(By.CLASS_NAME, 't_tr1')

    # 从 tr 中找出 td
    # tr 行，定义行列表
    tr_tbr = []

    for tr in tr_list:
        td_list = tr.find_elements(By.TAG_NAME, 'td')

        # td 单元格，定义单元格列表
        td_tbr = []

        for td in td_list:
            td_tbr.append(td.text.replace(',', ''))
        print(td_tbr)
        tr_tbr.append(td_tbr)

    # print(tr_tbr)
    browser.quit()

    csv_header = ['期号',
                  '红球号码_1', '红球号码_2', '红球号码_3', '红球号码_4', '红球号码_5', '红球号码_6',
                  '蓝球',
                  '快乐星期天',
                  '奖池奖金(元)',
                  '一等奖_注数', '一等奖_奖金',
                  '二等奖_注数', '二等奖_奖金',
                  '总投注额(元)', '开奖日期']
    
    if not os.path.exists("data"):
        os.mkdir("data")

    # 写入csv
    with open(r'data/ssq_history_100.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(csv_header)
        for row in tr_tbr:
            writer.writerow(row)


def analyzeData():
    df = pd.read_csv(r'data/ssq_history_100.csv', index_col='期号')

    # 取出红球号码，iloc是按照索引，左闭右开
    red_ball = df.iloc[:, 0:6]

    # 取出篮球号码
    blue_ball = df.iloc[:, 6]

    # 统计每个号码出现的次数
    # flatten 把二维数组拍扁成一维数组
    red_ball_count = pd.value_counts(red_ball.values.flatten())
    print(red_ball_count)

    blue_ball_count = pd.value_counts(blue_ball.values.flatten())
    print(blue_ball_count)

    # 图形化展示
    # 方式1
    # fig, ax = plt.subplots(2, 1)
    # ax[0].pie(red_ball_count, labels=red_ball_count.index, radius=1, wedgeprops={'width': 0.3})
    # ax[0].pie(blue_ball_count, labels=blue_ball_count.index, radius=0.5, wedgeprops={'width': 0.2})

    # 方式2
    plt.pie(red_ball_count, labels=red_ball_count.index, radius=1, wedgeprops={'width': 0.3})
    plt.pie(blue_ball_count, labels=blue_ball_count.index, radius=0.5, wedgeprops={'width': 0.2})
    plt.show()


if __name__ == '__main__':
    # getData()
    analyzeData()
