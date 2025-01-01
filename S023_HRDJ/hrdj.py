# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : hrdj.py
@Project            : S023_HRDJ
@CreateTime         : 2023/3/7 14:16
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/7 14:16 
@Version            : 1.0
@Description        : None
"""
import hashlib
import json
import time
import execjs
import requests


def js_encrypt(input_str):
    with open('app.js', 'r', encoding='utf-8') as f:
        app_js = f.read()
    ctx = execjs.compile(app_js)
    function = 'i("%s")' % input_str
    res = ctx.eval(function)
    print(res)
    return res


headers = {
    "Content-Type": "application/json;charset=UTF-8",
}
phoneNum = '18621942161'
password = "qwer1234"
encrypt_pwd = js_encrypt(password)

timestamp = int(time.time() * 1000)
tenant = 1
fix_str = "JzyqgcoojMiQNuQoTlbR5EBT8TsqzJ"
encrypt_group = js_encrypt(phoneNum + encrypt_pwd + str(timestamp) + str(tenant) + fix_str)

payload_login = {
    'phoneNum': phoneNum,
    'pwd': encrypt_pwd,
    't': timestamp,
    'tenant': tenant,
    'sig': encrypt_group
}

url_phonePwdLogin = "https://user.hrdjyun.com/wechat/phonePwdLogin"
resp = requests.post(url_phonePwdLogin, data=json.dumps(payload_login), headers=headers).json()

token = resp['data']['token']
print(token)

data_no_rank = {"no": "dy0026", "data": {}}
data_rank_2 = {"no": "dy1011", "data": {"rankType": "2"}}
data_param = json.dumps(data_no_rank, separators=(',', ':'))
salt = "kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$"

# json.dumps 把python 字典转换为json 字符串格式，
# 和 JS 中的 JSON.stringify() 函数不同的是， Python 中的这个转换会为了美观自动补空格
# 所以需要增加 separators 参数
data = "param=" + data_param + "&timestamp=" + str(int(time.time() * 1000)) + "&tenant=1&salt=" + salt
print(data)
data_sha = hashlib.sha256(data.encode('utf-8')).hexdigest()
print(data_sha)

url_data = "https://ucp.hrdjyun.com:60359/api/dy"
payload = {
    # 传参的时候要对引号做转义
    "param": data_param.replace('"', '\"'),
    "sign": data_sha,
    "tenant": str(tenant),
    "timestamp": int(time.time() * 1000),
    "token": token
}

resp = requests.post(url_data, data=json.dumps(payload), headers=headers).text
print(resp)
