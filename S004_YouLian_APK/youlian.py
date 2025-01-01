# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : youlian.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/29 22:40
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/29 22:40
@Version            : 1.0
@Description        : None
"""
import hashlib
import time
import requests


def get_pw_encrypted(pw_plaintext):
    obj = hashlib.md5()
    obj.update(pw_plaintext.encode('utf-8'))
    pw_encrypted = obj.hexdigest()
    return pw_encrypted


def get_x_sign(phone, pw_encrypted, timestamp):
    # 固定为空
    token = ""

    # 13 位时间戳
    reqTime = timestamp

    # 固定值
    nonce_str = "123456"
    nonce_str_sub_2 = nonce_str[2:]

    # 变量，从入参中获取
    body_str = f"phone={phone}&password={pw_encrypted}"

    # 拼接
    encrypt_string = f"{token}{reqTime}{nonce_str_sub_2}{body_str}"

    obj = hashlib.md5()
    obj.update(encrypt_string.encode('utf-8'))
    x_sign = obj.hexdigest()
    return x_sign


def login(phone, pw_plaintext):
    pw_encrypted = get_pw_encrypted(pw_plaintext)
    timestamp = str(int(time.time() * 1000))
    x_sign = get_x_sign(phone, pw_encrypted, timestamp)

    headers = {
        'X-App': 'native',
        'X-Noncestr': '123456',
        'X-OS': 'partnerApp_android',
        'X-Req-Time': timestamp,
        'X-Sign': x_sign,
        'X-Token': '',
        'X-UserID': '',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'chinayltx.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0'
    }
    form_data = {
        'phone': phone,
        'password': pw_encrypted
    }
    url_login = 'https://chinayltx.com/app/api/v1/partnerLogin/login'
    res = requests.post(url_login, headers=headers, data=form_data)
    print(res.content.decode('utf-8'))


if __name__ == '__main__':
    phone = '18621942161'
    pw_plaintext = '123456'
    login(phone, pw_plaintext)
