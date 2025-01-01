# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : proxy.py
@Project            : Crawler_2022
@CreateTime         : 2022/2/28 23:32
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2022/2/28 23:32
@Version            : 1.0
@Description        : B站樵夫视频
    # 免费代理IP地址：https://img.kuaidaili.com/free/inha/4484/
"""
import requests


# 免费IP
url = 'https://www.baidu.com'
proxy = {
    'http': 'http://221.216.138.178:9000'
}

resp = requests.get(url, proxies=proxy)
resp.encoding = 'utf-8'
print(resp.text)


# 第三方代理接入，付费后通过API接口，得到IP地址

# if __name__ == '__main__':
#     pass
