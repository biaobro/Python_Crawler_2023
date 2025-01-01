# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : cookie.py
@Project            : Crawler_2022
@CreateTime         : 2022/2/28 22:15
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2022/2/28 22:15
@Version            : 1.0
@Description        : B站樵夫视频
    # 重点
    1，登录，获取cookie
    2，用 session 保存 cookie
"""
import requests

url_host = 'https://www.17k.com/'
url_login = 'https://passport.17k.com/ck/user/login'
url_shelf = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'  # appkey 看起来是JS代码里写死的，看图片


def main():
    session = requests.session()

    # 登录
    user_info = {
        'loginName': '18621942161',
        'password': 'wazg@2020'
    }
    resp_login = session.post(url_login, data=user_info)
    # print(resp.text)

    resp_shelf = session.get(url_shelf)
    books = resp_shelf.json()['data']
    for book in books:
        print(book)


if __name__ == '__main__':
    main()
