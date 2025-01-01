# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 17.urllib_basic.py
@Project            : Crawler_2022
@CreateTime         : 2022/1/22 14:28
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2022/1/22 14:28 
@Version            : 1.0
@Description         : urllib
"""
import urllib.error
import urllib.request
import urllib.parse


def httpbinpost():
    data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
    response = urllib.request.urlopen("https://httpbin.org/post", data=data)
    print(response.read().decode("utf-8"))


def httpbinget():
    # every exception should be taken into account
    # create an exception manually by timeout set
    try:
        response = urllib.request.urlopen("https://httpbin.org/get", timeout=0.01)
        print(response.read().decode("utf-8"))
    except Exception as e:
        print(e)


def statuscodecheck():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.99 Safari/537.36'}
    code418 = "https://douban.com"
    code200 = "https://www.baidu.com"

    data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
    url = "https://httpbin.org/post"

    # get 418 while no headers
    req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')

    # urlopen input could be address or http request object
    response = urllib.request.urlopen(req)
    print(response.read().decode("utf-8"))
    print(response.status)
    print(response.getheaders())
    print(response.getheader('Content-Length'))


def main():
    # baseurl = "https://movie.douban.com/top250?start=?"
    # datalist = getData(baseurl)
    # savepath = ".\\豆瓣电影Top250.xlsx"
    response = urllib.request.urlopen("https://www.baidu.com")
    # print(response)  # HTTPResponse
    print(response.read().decode('utf-8'))


def getData(baseurl):
    datalist = []
    return datalist


def saveData(savepath):
    pass


if __name__ == '__main__':
    statuscodecheck()
