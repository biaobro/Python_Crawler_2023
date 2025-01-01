# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : zzzmh.py
@Project            : S025_ZZZMH
@CreateTime         : 2023/3/9 15:04
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/9 15:04 
@Version            : 1.0
@Description        : None
"""
import json
import re
import time
from urllib.parse import urlencode
import requests
import execjs

# referer 是必须的
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'referer': 'https://bz.zzzmh.cn/',
    'content-type': 'application/json;charset=UTF-8'
}

js_python = execjs.compile(open('app.js', 'r', encoding='utf-8').read())


def get_pic_infos(page_num=1):
    url_page = "https://api.zzzmh.cn/bz/v3/getData"
    payload_page = {
        "size": 24,
        "current": page_num,
        "sort": 0,
        "category": 0,
        "resolution": 0,
        "color": 0,
        "categoryId": 0,
        "ratio": 0
    }
    resp = requests.post(url_page, headers=headers, data=json.dumps(payload_page, separators=(',', ':')))
    if resp.json()['msg'] == 'success':
        result = resp.json()['result']
    else:
        raise ValueError('not get valid response')

    pics_str = js_python.call('parse', result)
    with open(f"data/page_{page_num}.text", 'w', encoding='utf-8') as f:
        f.write(pics_str)

    pics_dict = json.loads(pics_str)
    return pics_dict['list']


def get_cookies():
    # 获取 cookie
    payload_cookies = {
        'domain': 'bz.zzzmh.cn',
        'callback': '_gfp_s_',
        # 这个client 是在 index.html 中静态提供的，目前看到是不变的
        'client': 'ca-pub-6647994087975800'
    }
    url_cookie = "https://partner.googleadservices.com/gampad/cookie.js?" + urlencode(payload_cookies)
    resp = requests.get(url_cookie, headers=headers)

    # (?<=\"_value_\":) 表示以 \"_value_\": 开头，但是结果中不要 \"_value_\":
    regex_cookie = r"(?<=\"_value_\":)(.*?),"
    __gads, __gpi = re.findall(regex_cookie, resp.text)
    return {'__gads': __gads, '__gpi': __gpi}


# 这里要注意的是，即使是手动点击图片下载，也会在连续到18张左右触发 500 error
def get_pic(pics, cookies):
    # 在图片ID上补这2个不同的code，发起请求，会从response headers 中得到大图展示，或者这下载地址
    show_code = '21'
    download_code = '29'

    # 获取图片
    for idx, pic in enumerate(pics):
        pic_id = pic['i']
        url_pic = "https://api.zzzmh.cn/bz/v3/getUrl/" + pic_id + download_code

        # 这个请求会返回1个302，同时在 Response Headers 中包含了跳转的地址
        resp = requests.get(url_pic, headers=headers, cookies=cookies, allow_redirects=False)
        url_location = resp.headers.get('location')

        headers['Content-Disposition'] = 'attachment'
        resp = requests.get(url_location, headers=headers, cookies=cookies)
        with open(f"data/{'1' + str(idx).zfill(2)}_{pic_id}.jpg", mode='wb') as f:
            f.write(resp.content)
            print(pic_id + ' has been saved.')

        # 请求太快会被限制
        time.sleep(30)


if __name__ == '__main__':
    pic_list = get_pic_infos()
    cookies = get_cookies()
    get_pic(pic_list, cookies)
