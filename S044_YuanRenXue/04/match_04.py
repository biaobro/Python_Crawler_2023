# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : match_04.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/9 9:44
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/9 9:44 
@Version            : 1.0
@Description        : None
"""
import requests
import re
import base64
import hashlib
from match_04_code import relations


def get_j_key(key, value):
    # JS 代码中使用请求中返回的 key 和 value，得到样式需要被替换为 display:none 的 img
    # 所以同样的，在Python中需要处理 key 和 value，然后相应地跳过样式 display:none 的 img

    # 第一步：Python 实现 JS 代码逻辑
    # js代码 :
    # j_key = '.' + hex_md5(btoa(data.key + data.value).replace(/=/g, ''))
    # $(j_key).css('display', 'none');

    # Python base64 用于替代 JS 中的 windows.btoa()
    j_key = base64.encodebytes((key + value).encode("utf8"))
    j_key = j_key.decode("utf8").strip()
    j_key = j_key.replace('=', '')

    # Python hex_md5 用于替代 JS 中的 hex_md5
    md5 = hashlib.md5()
    md5.update(j_key.encode('utf-8'))
    j_key = md5.hexdigest()
    # print(j_key)
    return j_key


def get_number(j_key, info):
    # 第二步：读取 data 对应得到 数字
    # 每页10个 td，每个td对应1个数字，里若干个 img
    regex_tds = r"<td>.*?<\/td>"
    tds = re.findall(regex_tds, info)

    # 每个页面上的10个数字之和
    p_total = 0
    for td in tds:
        digits = []
        offsets = []

        # 得到 image 的Base64 Data
        regex_imgs = r'<img.*?>'
        imgs = re.findall(regex_imgs, td)

        for img in imgs:
            # 如果 img 包含 j_key，也就是将要被替换为 display:none 的样式，就跳过，不做进一步处理
            if j_key in img:
                continue
            else:
                # 得到 base64 编码
                regex_base64 = r'(?<=src=").*?(?=")'
                data = re.findall(regex_base64, img)[0]

                # 根据映射关系得到Base64编码对应的数字
                digit = relations.index(data)

                # 得到 style 以判断位置
                regex_style = r'(?<=style=").*?(?=")'
                style = re.findall(regex_style, img)[0]

                # 直接得到偏移值，用eval 将字符串转换为数字
                regex_offset = r'(?<=left:).*?(?=px)'
                offset_rel = int((eval(re.findall(regex_offset, img)[0])) / 11.5)

                digits.append(digit)
                offsets.append(offset_rel)

        # 根据数字位数 初始化1个对应长度的数组
        count = 0
        number_str = [0] * len(digits)

        # 填充数组，数组下标 +
        for digit, offset in zip(digits, offsets):
            number_str[count + offset] = digit
            count += 1

        # print(number)
        # 将字符串转换为数字
        number = eval(''.join(str(_) for _ in number_str))
        print(number)
        p_total = p_total + number
    print('-'*30)
    return p_total


def get_page(num):
    # 发起请求
    url = "https://match.yuanrenxue.cn/api/match/4?page=" + str(num)
    resp = requests.get(url)

    # 解析请求
    data = resp.json()
    info = data['info']
    key = data['key']  # "8uv59kt2hI"
    value = data['value']  # "Wrf9uj2kIK"

    j_key = get_j_key(key, value)
    p_total = get_number(j_key, info)
    return p_total


total = 0
for page in range(1, 6):
    total = total + get_page(page)
print(total)
