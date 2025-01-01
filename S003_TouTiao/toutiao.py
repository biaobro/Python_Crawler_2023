# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : toutiao.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/22 20:01
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/22 20:01 
@Version            : 1.0
@Description        : None
        # pip3.11.exe install PyExecJS
"""
import execjs
import requests
from urllib.parse import urlencode

with open('construct_env.js', mode='r', encoding='utf-8') as f:
    js = f.read()

JS = execjs.compile(js)

payload = {
    'channel_id': '3189399007',
    'min_behot_time': '0',
    'refresh_count': '1',
    'category': 'pc_profile_channel',
    'client_extra_params': '{"short_video_item":"filter"}',
    'aid': '24',
    'app_name': 'toutiao_web',
}

base_url = "https://www.toutiao.com/api/pc/list/feed?"

# client_extra_params 的参数部分整体要用 '' 括起来
# 冒号 : 不需要被编码，所以需要再替换回来
# tbp : to be packed
tbp_url = base_url + urlencode(payload).replace('%3A', ':')
print(tbp_url)

signature = JS.call("get_sign", tbp_url)
print(signature)
tbp_url = f"{tbp_url}&_signature={signature}"

response = requests.get(
    url=tbp_url,
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
)

print(response.text)

