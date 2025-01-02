# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : wallhaven_etree_xpath_single_thread.py
@Project            : S049_WallHaven
@CreateTime         : 2023/4/24 12:05
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/24 12:05 
@Version            : 1.0
@Description        : xpath 的效率要比 re 明显慢很多
"""
import requests
from lxml import etree

url = "https://wallhaven.cc/hot?page=" + '1'
resp = requests.get(url)
print(resp.text)

# 其实页面上有直接提供高清图地址，不需要点击到详情页面再获取
et = etree.HTML(resp.text)

# 同样是img 标签下的属性， data-src 可以拿到，而 src 拿不到
# 经过排查发现，页面“检查”查看源代码 src 是有值的，但是通过 requests 得到的text 中src 是空字符串
# 网上有人说：浏览器有容错机制，对于不规范的html标签，会进行修正，所以你在控制台看到的页面结构，和你用代码请求到的页面结构可能是不一样的。
small_imgs = et.xpath('//*[@id="thumbs"]/section[1]/ul/li/figure/img/@data-src')
print(len(small_imgs))

for img in small_imgs:
    print(img)
    filename = img.split('/')[-1]
    print(filename)
    with open(f"{filename}", 'wb') as f:
        f.write(requests.get(img).content)
    break
