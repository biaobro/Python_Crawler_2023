# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : baudu_pic.py
@Project            : S055_BaiDu_Pic
@CreateTime         : 2023/5/3 10:52
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/5/3 10:52
@Version            : 1.0
@Description        : None
"""
import re
import sys
import urllib
import requests
import os
# import cv2
from glob import glob
import time

pic_types = {"1": "flip", "2": "index"}


def get_page_url(keyword, times, page_number, pic_type):
    """
    :param keyword: 要搜索的关键字
    :param times:
    :param page_number:
    :param pic_type: 要搜索的图片类型
    :return: 根据输入参数，得到待请求的 url
    """
    page = times * page_number
    # print("Source Keyword : ",keyword)
    keyword = urllib.parse.quote(keyword, safe='/')
    # print("Converted Keyword : ",keyword)
    url = "http://image.baidu.com/search/" + pic_type + "?tn=baiduimage&ie=utf-8&word=" + keyword + "&pn=" + str(page)
    print(url)
    return url


def get_pic_urls(urlPage):
    try:
        html = requests.get(urlPage).text
    except Exception as e:
        print(e)
        pic_urls = []
        return pic_urls

    # Regular expression,
    regex_pics = '"objURL":"(.*?)",'

    # store all the url list of current page
    pic_urls = re.findall(regex_pics, html, re.S)
    print("There are {} pic links".format(len(pic_urls)))
    return pic_urls


def get_pics(pic_urls, save_path):
    print("There are {} downloadable pics after deduplication".format(len(pic_urls)))

    print("\nDownloading start...")
    start_time = time.time()
    for idx, pic_url in enumerate(pic_urls):
        try:
            resp = requests.get(pic_url, timeout=5)
            fileName = save_path + '/' + str(idx + 1) + '.jpg'

            with open(fileName, 'wb') as f:
                f.write(resp.content)
                print("Successful download the %s pic: %s" % (str(idx), pic_url))
        except Exception as e:
            print("Failed download the %s pic: %s" % (str(idx), pic_url))
            print(e)
            continue
    end_time = time.time() - start_time
    print("Download finished within : {:.0f}m {:.0f}s ...".format(end_time // 60, end_time % 60))


if __name__ == '__main__':
    # 输入要搜索的关键字
    keyword = input("Please input a keyword : ")

    # 根据关键字，创建图片保存路径
    save_path = './baidu_download/' + keyword

    # You have to use makedirs
    # mkdir function create folder in existing folder
    # it will raise an error cause the parent folder doesn't exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 提供可选的 pic_types, end="" 表示输出不换行，不指定时默认为 "\n"
    print(pic_types, end="")
    pic_type = pic_types.get(input("\nPlease select the type :"))

    # 得到图片类型
    print("The pic_type is : {}".format(pic_type))

    # baidu 页面设定，每次下拉加载20个图片
    page_number = 20

    # 用来控制下拉次数
    total_times = 0

    # initialize the variables
    times = 0
    tbd_pic_urls = []

    while 1:
        if times > total_times:
            break
        print("the {} request data".format(times + 1))
        url = get_page_url(keyword, times, page_number, pic_type)
        pic_urls = get_pic_urls(url)
        times += 1
        if len(pic_urls) != 0:
            tbd_pic_urls.extend(pic_urls)
    print("Total {} pics will be downloaded".format(len(tbd_pic_urls)))

    get_pics(list(set(tbd_pic_urls)), save_path)
