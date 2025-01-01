# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : ygp_01.py
@Project            : S024_YGP
@CreateTime         : 2023/3/8 11:07
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/8 11:07 
@Version            : 1.0
@Description        : None
"""
import json
import random
import time
from urllib.parse import urlencode, unquote
import hashlib
import uuid
import requests


def get_timestamp():
    return str(int(time.time() * 1000))


def get_random_str(length=16):
    # ky 是 js 代码中提供的常量字符串
    ky = "zxcvbnmlkjhgfdsaqwertyuiop0987654321QWERTYUIOPLKJHGFDSAZXCVBNM"
    res = ''.join([random.choice(ky) for _ in range(length)])
    return res


def sort_by_key(params_str):
    t = ''
    if len(params_str) > 0:
        lst = params_str.split('&')
        lst.sort()
        t = unquote('&'.join(lst))
    return t


payload = {
    "type": "trading-type",
    "publishStartTime": "",
    "publishEndTime": "",
    "siteCode": "44",
    "secondType": "A",
    "projectType": "",
    "thirdType": "",
    "dateType": "",
    "total": 0,
    "pageNo": 1,
    "pageSize": 10,
    "openConvert": "false"
}

encoded_params = urlencode(payload)
print('encoded_params', encoded_params)
decoded_params = sort_by_key(encoded_params)
print('decoded_params', decoded_params)

fix_str = "k8tUyS$m"
random_str = get_random_str()
time_stamp = get_timestamp()
sha_target = random_str + fix_str + decoded_params + time_stamp
print('sha_target', sha_target)
sha_res = hashlib.sha256(sha_target.encode('utf-8')).hexdigest()
print('sha_res', sha_res)

headers = {
    'Content-Type': 'application/json',
    'Host': 'ygp.gdzwfw.gov.cn',
    'Origin': 'https://ygp.gdzwfw.gov.cn',
    'Referer': 'https://ygp.gdzwfw.gov.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Dgi-Req-App': 'ggzy-portal',
    'X-Dgi-Req-Nonce': random_str,
    'X-Dgi-Req-Signature': sha_res,
    'X-Dgi-Req-Timestamp': time_stamp
}

# uuid.uuid() 得到类型是 'uuid.UUID'，需要转成 str
uid, sid = str(uuid.uuid4()), str(uuid.uuid4())
cookies = {
    '_horizon_sid': uid,
    '_horizon_uid': sid,
}

url_data = "https://ygp.gdzwfw.gov.cn/ggzy-portal/search/v1/items"

resp = requests.post(
    url_data,
    headers=headers,

    # 这里也要记得将 字典格式转换成 json 字符串，不要空格美化
    data=json.dumps(payload, separators=(',', ':')),
    cookies=cookies)
print(resp.json()['data'])
